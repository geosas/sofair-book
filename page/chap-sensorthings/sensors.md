# **Sensors**  

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
| **metadata** (obligatoire)** | Description détaillée du capteur, lien vers la documentation | dépend de encoding type. | Obligatoire |
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

Le champ **properties** est un objet JSON (paires/clé-valeur). Elles sont définies à la conception et permet de mieux caractériser une **Thing**.  

***Recommandations***

* Pas de réelles recommandations. Les propriètés étant non standardisées, ne pas les considérer comme un élément descriminant pouvant être utilisé dans une requête. Nécessite également de bien documenter pour informer les utlisateurs de leurs existances.

***Exemples***  

* SOERE PRO EFELE
```json
{ 
  "projet": "https://geosas.fr/web/?page_id=2476",  
  "manuel d'utilisation": "https://s.campbellsci.com/documents/fr/product-brochures/b_cr1000.pdf",
  "date de mise en place": "Septembre 2013" 
}
```

* ORE AgrHyS
```json
{ 
  "region": "B_Naizin", 
  "domaine": "NAIZIN", 
  "station": "KERVIDY_B_EXU" 
}
```
### **3. Exemples de Thing**   

```json
{
  "@iot.id": 1
  "@iot.selfLink": "https://sensorthings.geosas.fr/efele/v1.0/Things(1)",
  "name": "Station météo Campbell EFELE",
  "description": "Station météo Campbell personnalisée, équipée du data logger Campbell CR1000 ",
  "properties": { 
       "projet": "https://geosas.fr/web/?page_id=2476", 
       "manuel d'utilisation": "https://s.campbellsci.com/documents/fr/product-brochures/b_cr1000.pdf", 
       "date de mise en place": "Septembre 2013" 
  }
  "Locations@iot.navigationLink": "https://sensorthings.geosas.fr/efele/v1.0/Things(1)/Locations",
  "HistoricalLocations@iot.navigationLink": "https://sensorthings.geosas.fr/efele/v1.0/Things(1)/HistoricalLocations",
  "Datastreams@iot.navigationLink": "https://sensorthings.geosas.fr/efele/v1.0/Things(1)/Datastreams",
  "MultiDatastreams@iot.navigationLink": "https://sensorthings.geosas.fr/efele/v1.0/Things(1)/MultiDatastreams"
}
```
