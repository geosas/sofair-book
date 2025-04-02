## Location  

## **1. Définition** 
Une **Location** indique la positin d'une **Thing**. 

```{tip}
Dans le cas d'un observatoire, un **Location** fait référence généralment à des coordonnées GPS.
```

## **2. Propriètés**  
Une **Location** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **name** | Étiquette correspondant à une **Location**, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| **description** | Courte description de **Location**. | Chaine de caractères  | Obligatoire |
| **encodingType** | Le type d'encodage de la propriété **Location**. | application/geo+json  | Obligatoire |
| **location** | Le type d'emplacement est défini par **encodingType**.| Objet JSON  | Obligatoire |
| **properties**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON  | Optionnel |

### **2.1. name** (obligatoire) 
Le champ **name** est un nom court faisant référence à une **Thing**.

***Recommandations***  

Dans d'un observatoire, la **Thing** et la **Location** étant étroitement liées, les noms peuvent être identiques.

### **2.2. description** (obligatoire)  

Le champ **description** contient une courte description de la **Location**.

***Recommandations***  

Dans d'un observatoire, la **Thing** et la **Location** étant étroitement liées, les description peuvent être identiques.


#### **2.3. location** (optionel)  

Le champ **location** est un objet JSON (paires/clé-valeur). Elles sont définies à la conception et permet de mieux caractériser un **Sensor**.  

***Recommandations***

* C'est l'endroit préviligié pour renseigner des coordonnées GPS.

***Exemples***  

* ORE AgrHyS

```json
name: "Piezometer PK2",
description: "Piezometre du bassin versant de Kerrolland",
encodingType: "application/geo+json",
location: {
    type: "Point",
    coordinates: [
        -2.8396371,
        48.0121575
    ]
}
```

