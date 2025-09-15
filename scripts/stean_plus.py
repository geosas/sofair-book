import requests
import json
import os
import pandas as pd  # nécessites les librairies  openpyxl, xlrd pour ouvrir le xlsx
import shapely
from shapely.geometry import Point, LineString, Polygon
import sys


class instanceST():
    def __init__(self, urlServer, username, password):
        self.urlServer = urlServer
        self.username = username
        self.password = password
        self.token = ""
              
# Transactions avec le serveur ###########################################################################        
    def connexion(self):
        print("Connexion", self.username, " à ",self.urlServer)
        json_data = json.dumps({"username":self.username,"password":self.password})
        response = requests.post(url=self.urlServer + "login", headers= {'Content-Type': 'application/json'}, data=json_data)
        if response.status_code == 200:
            print("Connexion OK à ", self.urlServer,"\n") 
            self.token = response.json()["token"]

    def log_out(self):
        print("Déconnexion de ",self.urlServer)
        response = requests.get(url=self.urlServer + "logout")
        if response.status_code == 200:
            print("Déconnexion OK de ", self.urlServer,"\n")

    def getInfo(self, objet, options):
        url= "%s%s?$%s"% (self.urlServer, objet, options)
        response = requests.get(url=url)
        objet_json = response.json()['value']
        if len(objet_json) == 1:
            return objet_json
        else:
            if len(objet_json) > 1:
                print("Objets trouvés selon le filtre -> ", options)
            else:
                print("Aucun objet trouvé selon le filtre -> ", options)
            return -1
    
    def getIdObjet(self, objet, name):
        #print("recherche id de :", objet, name)
        r=requests.get(url="%s%s?$filter=name eq '%s'"% (self.urlServer, objet, name))
        #print(r.status_code)
        objet_json=r.json()['value']
        if len(objet_json) != 1:
            print("l'objet", objet, name," n'a pas pu être trouvé")
            return -1
        else:
            #print("id :",objet_json[0]['@iot.id'])
            return objet_json[0]['@iot.id']

    def postCsvFile(self, fileName, datas):
        files = {
            'json': (None, json.dumps(datas), 'application/json'),
            'file': (os.path.basename(fileName), open(fileName, 'rb'), 'application/octet-stream')
        }
        headers = { 'Authorization': "Bearer {}".format(self.token) }
        response = requests.post(self.urlServer + "CreateObservations", headers=headers, files=files)
        return response

    def post_data_serveur(self, objet, data):
        print('Post Data')
        for i in data:
            self.test_json=i
            json_data = json.dumps(i)
            lien="%s/%s" % (self.urlServer,objet)
            r = requests.post(url=lien,headers= {'Content-Type': 'application/json','Authorization': "Bearer {}".format(self.token)}, data=json_data)
            if r.status_code == 201:
                print("Post OK")
            else:
                print("error: ", r.text)
                break

    def get_data(self,url_x):
        print("Get Data")
        df_all=pd.DataFrame()  
        r=requests.get(url=url_x)
        data=r.json()
        df_all = pd.concat([df_all, pd.DataFrame(data['value'])])
        while '@iot.nextLink' in data:
            print("next link")    
            r=requests.get(url=data['@iot.nextLink'])
            data=r.json()
            df_all = pd.concat([df_all, pd.DataFrame(data['value'])])
        return df_all

    # Traitement de données ###########################################################################     
      
    def readTableConf(self,chemin,onglet):
        print("Lecture de l'onglet " + onglet + " du fichier de configuration " + chemin)
        self.confSrc = pd.read_excel(chemin, sheet_name=onglet)

        # suppression des lignes vides
        if self.confSrc.isnull().values.any() == True: 
            print("Attention! Détection de valeurs manquantes dans l'onglet " + onglet)
            print("Suppression UNIQUEMENT des lignes vides")
            self.confSrc.dropna(how='all', inplace=True)

        # Suppression des doublons
        if self.confSrc.duplicated(subset=['name']).values.any() == True: 
            print("Attention! Détection de doublons dans l'onglet " + onglet)
            print("Suppression des doublons")
            self.confSrc.drop_duplicates(subset=['name'], inplace=True)
            
        self.confSrc.reset_index(drop=True, inplace=True)
    
    def checkDoublon(self, name, objet):
        print("check if exist", objet)
        objetValue = self.get_data(self.urlServer + objet)
        if len(objetValue) == 0:
            print("Table vierge pour", objet)
            return name
        else:
            objetNew = [x for x in name if x not in objetValue['name'].values]   
            objetOk = [x for x in name if x in objetValue['name'].values]
            print(objet, 'déjà publié :',objetOk,"\n")
            print(objet, 'nouveau :',objetNew)
            return objetNew
    
# Création des Json des entités ###########################################################################    
          
    def featureOfInterest_create(self, featureOfInterest_table):
        print("\n Publication des FeaturesOfInterest")
        featureOfInterestSrc = featureOfInterest_table
        featureOfInterestSrc = featureOfInterestSrc.drop_duplicates("name")
        featureOfInterestUnique = self.checkDoublon(featureOfInterestSrc['name'].values,"FeaturesOfInterest")
        featureOfInterest = []
        if len(featureOfInterestUnique)==0:
            print("pas de nouveau FeatureOfInterest à publier")
        else:
            featureOfInterestNew = featureOfInterestSrc[featureOfInterestSrc['name'].isin(featureOfInterestUnique)]
            featureOfInterestNew = featureOfInterestNew.fillna("")
            for idx,row in featureOfInterestNew.iterrows():
                print(row['name'])
                featureOfInterest.append({
					"name": row['name'],
					"description": row['description'],
					"encodingType": "application/vnd.geo+json",
					"feature": {
							"type": row['feature.type'].capitalize(),
                            "coordinates": json.loads(row['feature.coordinates'])
                            }
				})
        return(featureOfInterest)
    
    def sensor_create(self, sensor_table):
        print("\n Publication des Sensors")
        sensorSrc = sensor_table#[sensor_table['datastream name'].isin(datastream_table['name'])]
        sensorSrc = sensorSrc.drop_duplicates("name")
        sensorUnique = self.checkDoublon(sensorSrc['name'].values,"Sensors")
        sensor = []
        if len(sensorUnique)==0:
            print("pas de nouveau Sensor à publier")
        else:
            sensorNew = sensorSrc[sensorSrc['name'].isin(sensorUnique)]
            sensorNew = sensorNew.fillna("")
            for idx,row in sensorNew.iterrows():
                print(row['name'])
                sensor.append({
    				"name": row['name'],
    				"description": row['description'],
    				"encodingType": row['encodingType'],
    				"metadata": row['metadata'],
    				"properties": {
    						"Vmin": row['Vmin'],
                            "Vmax": row['Vmax'],
                            "Accuracy": row['Accuracy']
                            }
				})
        return(sensor)

    def observedProperty_create(self,observedProperty_table):
        print("\n Publication des observed properties")
        obspSrc = observedProperty_table
        obspSrc = obspSrc.drop_duplicates("name")
        obspUnique = self.checkDoublon(obspSrc['name'].values,"ObservedProperties")
        obsp = []
        if len(obspUnique)==0:
            print("pas de nouveau ObservedPropertY à publier")
        else:           
            obspNew = obspSrc[obspSrc['name'].isin(obspUnique)]
            obspNew = obspNew.fillna("")
            for idx,row in obspNew.iterrows():
                print(row['name'])
                obsp.append({
				"name": row['name'],
				"description": row['description'],
				"definition": row['definition'],
                "properties":{
                        "family": row['Family']
                            }
				})       
        return(obsp)

    def thing_create(self, thing_table):
        print("\n Publication des things")
        thingSrc = thing_table
        thingSrc = thingSrc.drop_duplicates("name")
        thing = []
        thingUnique = self.checkDoublon(thingSrc['name'].values,"Things")
        if len(thingUnique)==0:
            print("pas de nouveau Things à publier")
        else:
            thingNew = thingSrc[thingSrc['name'].isin(thingUnique)]
            thingNew = thingNew.fillna("")
            for idx,row in thingNew.iterrows():
                print(row['name'])
                thing.append({
                    "name": row['name'],
                    "description": row['description'],
                    "properties": {
                        "picture": row['picture']
                        },
                    "Locations": [
                        {
                            "name": row['name'],
                            "description": row['description'],
                            "encodingType": "application/geo+json",
                            "location": {
                                "type": row['type'].capitalize(),
                                "coordinates": json.loads(row['coordinates'])
                                },
                            } 
                    ]
                })

        return(thing)
    
    def datastream_create(self,datastream_table, observedProperty_table, sensor_table, thing_table, featureOfInterest_table):
        print("\n Publication des datastreams")
        datastreamUnique = self.checkDoublon(datastream_table['name'].values,"Datastreams")
        datastream=[]
        if len(datastreamUnique)==0:
            print("pas de nouveau datastream à publier")
        else:
            datastreamNew = datastream_table[datastream_table['name'].isin(datastreamUnique)]
            datastreamNew = datastreamNew.fillna("")
            for idx,row in datastreamNew.iterrows():
                print(row['name'])
                a = (row['name'].split(sep='_'))
                idThing = self.getIdObjet("Things",a[0])
                idSensor = self.getIdObjet("Sensors",a[1])
                idObsp = self.getIdObjet("ObservedProperties",a[2])
                if self.getIdObjet("FeaturesOfInterest",row['featureOfInterest']) == -1:
                    # FOI par défaut
                    idFOI = 1
                    print(idFOI)
                else:
                    idFOI = self.getIdObjet("FeaturesOfInterest",row['featureOfInterest'])
                if (idSensor == -1 or idObsp == -1 or idThing == -1 or idFOI == -1):
                    break
                datastream.append({
                    "name": row['name'],#.replace("_", " "),
                    "description": row['description'],
                    "observationType": row["observationType"],
                    "unitOfMeasurement": {
                        "name": row['unitOfMeasurement.name'],
                        "symbol": row['unitOfMeasurement.symbol'],
                        "definition": row['unitOfMeasurement.definition']
                    },
                    "Sensor": {"@iot.id": idSensor },
                    "ObservedProperty": {"@iot.id": idObsp },
                    "Thing": {"@iot.id": idThing },
                    "FeatureOfInterest": {"@iot.id": idFOI}
                }) 

        return(datastream)