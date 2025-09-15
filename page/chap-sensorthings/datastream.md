## Datastream

## **1. Définition**

Un **datastream** représente un flux de données regroupant une collection d'observations mesurant la même propriété observée et produites par le même capteur.

```{tip}
Dans le cas d'un observatoire, ce flux de données fait souvent référence à une valeur physique mesurée émise par un capteur ou une centrale de mesure.
```

## **2. Propriétés**

Un **datastream** possède des paramètres obligatoires et des propriétés optionnelles.

| Nom                   | Définition                                                                                                                                                                                                                                                              | Format                             | Exigences   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ----------- |
| **name**              | Étiquette correspondant à un **datastream**, généralement un nom descriptif court.                                                                                                                                                                                      | Chaine de caractères               | Obligatoire |
| **description**       | Courte description du **datastream**.                                                                                                                                                                                                                                   | Chaine de caractères               | Obligatoire |
| **unitOfMeasurement** | Un objet JSON contenant trois paires clé-valeur. La propriété _name_ présente le nom complet de l'unité de mesure ; la propriété _symbol_ indique la forme textuelle du symbole de l'unité ; et la propriété _definition_ contient l'URI définissant l'unité de mesure. | JSON Object                        | Obligatoire |
| **observationType**   | Le type d'observation (avec un type de résultat unique) utilisé par le service pour coder les observations.                                                                                                                                                             | ValueCode                          | Obligatoire |
| **properties**        | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur.                                                                                                                                                                         | Objet JSON                         | Optionnel   |
| **observedArea**      | Etendue spatiale de toutes les FeaturesOfInterest appartenant aux observations associées à ce flux de données. Zone géographique                                                                                                                                        | GM_Envelope (GeoJSON Polygon)      | Optionnel   |
| **phenomenonTime**    | Intervalle temporel des temps de **phénomène** de toutes les observations appartenant à ce flux de données.                                                                                                                                                             | TM_Period (ISO 8601 Time Interval) | Optionnel   |
| **resultTime**        | L'intervalle temporel des temps de **résultat** de toutes les observations appartenant à ce flux de données.                                                                                                                                                            | TM_Period (ISO 8601 Time Interval) | Optionnel   |

### **2.1. name** (obligatoire)

Le champ **name** décrit de façon unique et simple un flux de données.

**_Recommandations_**

Dans le cas d'un observatoire, il fait référence à la variation d'une variable d'observation (ex. : grandeur physique)

**_Exemples_**

- Outlet Exutoire_OTT Thalimede_stream level, ici est fait référence au niveau d'eau mesuré par un capteur OTT Thalimed position sur un exutoire.

### **2.2. description** (obligatoire)

Le champ **description** contient une courte description le **datastream**.

**_Recommandations_**

- Un peu à l'image de **name** mais plus détaillé.

### **2.3. unitOfMeasurement** (obligatoire)

Le champ **unitOfMeasurement** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser un **datastream**.

**_Recommandations_**

- L'ojet JSON peut comporter le nom de l'unité mesurée, le symbole en SI et un lien vers un thésaurus.

**_Exemples_**

- ORE AgrHyS

```json
{
"unitOfMeasurement": {
    "name": "mètre",
    "symbol": "m",
    "definition": "https://www.bipm.org/en/si-base-units/metre"
}
```

### **2.4. observationType** (obligatoire)

Le champ **observationType** est un code prédéfini du type d'observation (avec un type de résultat unique), qui est utilisé par le service pour coder les observations.

**_Recommandations_**

- Dans le cas d'un observation, OM_Measurement et OM_Observation sont généralement utilisés. Voir [tableau des codes](https://docs.ogc.org/is/18-088/18-088.html#tab-value-codes-obstypes).

### **2.5. properties** (optionnel)

Le champ **properties** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser un **datastream**.

### **2.6. observedArea** (optionnel)

Le champ **observedArea** permet de définir une zone géographique selon un polygone au format GeoJSON.

### **2.7. phenomenonTime** (optionnel)

Le champ **phenomenonTime** est un intervalle de temps.

### **2.8. resultTime** (optionnel)

Le champ **resultTime** est un intervalle de temps.

## **3. Exemples de Datastream**

```json
{
  "@iot.selfLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Datastreams(1)",
  "@iot.id": 1,
  "name": "Outlet E30_OTT Thalimede_stream level",
  "description": "Outlet E30 stream level",
  "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
  "unitOfMeasurement": {
    "name": "mètre",
    "symbol": "m",
    "definition": "https://www.bipm.org/en/si-base-units/metre"
  },
  "observedArea": null,
  "phenomenonTime": "2001-09-07T09:00:00Z/2024-06-26T12:00:00Z",
  "resultTime": "2001-09-07T09:00:00Z/2024-06-26T12:00:00Z",
  "properties": null,
  "Thing@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Datastreams(1)/Thing",
  "Sensor@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Datastreams(1)/Sensor",
  "ObservedProperty@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Datastreams(1)/ObservedProperty",
  "Observations@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Datastreams(1)/Observations",
  "FeatureOfInterest@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Datastreams(1)/FeatureOfInterest"
}
```
