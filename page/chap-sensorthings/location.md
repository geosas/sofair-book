## Location  

## **1. Définition** 
Une **Laction ** indique la positin d'une **Thing**. 

```{tip}
Dans le cas d'un observatoire, un **Location** fait référence généralment à des coordonnées GPS.
```

## **2. Propriètés**  
Une **truc** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **name** | Étiquette correspondant à une **Location**, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| **description** | Courte description de **Location**. | Chaine de caractères  | Obligatoire |
| **encodingType** | Le type d'encodage de la propriété **Location**. | application/geo+json  | Obligatoire |
| **location** | Le type d'emplacement est défini par **encodingType**.| Objet JSON  | Obligatoire |
| **properties**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON  | Optionnel |

### **2.1. name** (obligatoire) 
Le champ **name** correspond à ...

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

