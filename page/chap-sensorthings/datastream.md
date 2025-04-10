## Datastream  

## **1. Définition** 
Un **datastream ** représente un flux de données regroupant une collection d'observations mesurant la même propriété observée et produites par le même capteur.

```{tip}
Dans le cas d'un observatoire, ce flux de données fait souvent référence à une valeur physique mesurée émise par un capteur ou une centrale de mesure.
```

## **2. Propriètés**  
Une **datastream** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **name** | Étiquette correspondant à un **datastream**, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| **description** | Courte description du **datastream**. | Chaine de caractères  | Obligatoire |
| **unitOfMeasurement** | Un objet JSON contenant trois paires clé-valeur. La propriété name présente le nom complet de l'unité de mesure ; la propriété symbol indique la forme textuelle du symbole de l'unité ; et la propriété definition contient l'URI définissant l'unité de mesure. | JSON Object  | Obligatoire |
| **observationType**  | Le type d'observation (avec un type de résultat unique) utilisé par le service pour coder les observations. | ValueCode  | Obligatoire |
| **properties**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON  | Optionnel |
| **observedArea**  | Etendue spatiale de toutes les FeaturesOfInterest appartenant aux observations associées à ce flux de données. Zone géopgraphique | GM_Envelope (GeoJSON Polygon)  | Optionnel |
| **phenomenonTime**  | Intervalle temporel des temps de **phénomène** de toutes les observations appartenant à ce flux de données. | TM_Period (ISO 8601 Time Interval)  | Optionnel |
| **resultTime**  | L'intervalle temporel des temps de **résultat** de toutes les observations appartenant à ce flux de données. | TM_Period (ISO 8601 Time Interval)  | Optionnel |


### **2.1. name** (obligatoire) 
Le champ **name** correspond à

***Recommandations***  

Il est recommandé de ...

***Exemples***  

* exemple
* 

### **2.2. description** (obligatoire)  

Le champ **description** contient une courte description le **truc**.

***Recommandations***  

* Il est recommandé d'expliciter le **truc**, ...

***Exemples***  

* ...

#### **2.3. properties** (optionel)  

Le champ **properties** est un objet JSON (paires/clé-valeur). Elles sont définies à la conception et permet de mieux caractériser un **Sensor**.  

***Recommandations***

* Il peut être intéressant de renseigner les caractéristique stechniques du capteurs.

***Exemples***  

* ORE AgrHyS

```json
{
"cles": " valeur"
}
```

### **3. Exemples de Sensor**   

```json
{
"cles": " valeur"
}
```

