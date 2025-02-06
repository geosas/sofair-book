# **Sensor**  

## **1. Définition** 
Une **Sensor** est un instrument qui observe, ou mesure, une propriété ou un phénomène dans le but de produire une estimation de sa valeur.  

```{tip}
Dans le cas d'un observatoire, un **Sensor** est le plus souvent:
* un capteur
* une analyse physico-chimique
* une valeur calculée à partir de mesures.
```

## **2. Propriètés**  
Une **Thing** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **name** | Étiquette correspondant à un **Sensor**, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| **description** | Courte description du **Sensor**. | Chaine de caractères  | Obligatoire |
| **encoding type** | Défini le type de métadonnée. | html ou pdf ou SensorML | Obligatoire |
| **metadata** | Description détaillée du capteur, lien vers la documentation | dépend de encoding type. | Obligatoire |
| **properties**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON  | Optionnel |

### **2.1. name** (obligatoire) 
Le champ **name** correspond à une étiquette/un identifiant le **Sensor**, généralement sous la forme d’un nom descriptif court.

***Recommandations***  

Il est recommandé de faire apparaitre le type du capteur et le modèle (informations techniques).

***Exemples***  

* OTT Thalimede  
* Wimesure Pt100  
* Turbidimeter Ponsel

### **2.2. description** (obligatoire)  

Le champ **description** contient une courte description le **Sensor**.

***Recommandations***  

* Il est recommandé d'expliciter le **Sensor**, surtout dans le cas d'utilisattion d'un codage. 

***Exemples***  

* Analyseur en ligne de phosphore
* releve de niveau d'eau sur echelle limnimetrique
* Capteur d'oxygène dissous dans l'eau et de température de l'eau  

#### **2.3. encoding type** (obligatoire)  

Le champ **encoding type** se référe à des valeurs prédéfinies (html ou pdf ou SensorML) et défini le codage des métadonnées.

***Recommandations***  

* Dans le cas d'un **sensor**, l'encodage se référe au type de documentation, le plus souent une URL ou un PDF. 

***Exemples***  

* html
* PDF

#### **2.4. metadata** (obligatoire)  

Le champ **metadata** indique la source de la description détaillée du **sensor**.

***Recommandations***  

* Lien vers le site constructeur ou un fichier PDF. 

***Exemples***  

* https://www.pme.com/wp-content/uploads/PME-miniDOT-Manual-2021.pdf
* https://vanessen.com/images/PDFs/Diver-ProductManual-en.pdf  

#### **2.5. properties** (optionel)  

Le champ **properties** est un objet JSON (paires/clé-valeur). Elles sont définies à la conception et permet de mieux caractériser un **Sensor**.  

***Recommandations***

* Il peut être intéressant de renseigner les caractéristique stechniques du capteurs.

***Exemples***  

* ORE AgrHyS

```json
{
  "Vmax": "Niveau  10m ou 50m ou 100m
  Température -80°C
  Conductivité 120 mS/cm",
  "Vmin": "Niveau 0 m
  Température -20°C
  Conductivité 0 µS/cm",
  "Accuracy": "Niveau  précision +/- 0,2% de la pleine échelle Température précision +/- 0,2°C
  Conductivité +/- 0,1% de la valeur mesurée"
}
```
### **3. Exemples de Sensor**   

```json
{
    "@iot.selfLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Sensors(8)",
    "@iot.id": 8,
    "name": "Diver CTD",
    "description": "Capteur de niveau, de conductivité électrique et de témpérature de l'eau",
    "encodingType": "application/pdf",
    "metadata": "https://vanessen.com/images/PDFs/Diver-ProductManual-en.pdf",
    "properties": {
        "Vmax": "Niveau  10m ou 50m ou 100m
        Température -80°C
        Conductivité 120 mS/cm",
        "Vmin": "Niveau 0 m
        Température -20°C
        Conductivité 0 µS/cm",
        "Accuracy": "Niveau  précision +/- 0,2% de la pleine échelle Température précision +/- 0,2°C
        Conductivité +/- 0,1% de la valeur mesurée"
    },
    "Datastreams@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Sensors(8)/Datastreams",
    "MultiDatastreams@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Sensors(8)/MultiDatastreams"
}

```
