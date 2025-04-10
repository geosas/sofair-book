## FeatureOfInterest  

## **1. Définition** 
Un **FeatureOfInterest ** défini ou décrit un intérêt commun d'observation. C'est une sorte de filtre.

```{tip}
Dans le cas d'un observatoire, un **FeatureOfInterest** peut-être:  
* un site
* une station météo
* Toutes les observations d'une m^me valeur physique mesurée
* etc
```

## **2. Propriètés**  
Une **FeatureOfInterest** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **name** | Étiquette correspondant à un **truc**, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| **description** | Courte description du **truc**. | Chaine de caractères  | Obligatoire |
| **encodingType**  | Type d'encodage de la propriété de l'élémen (voir le [tableau](https://docs.ogc.org/is/18-088/18-088.html#tab-encodingtype-codes).| ValueCode  | Obligatoire |
| **feature**  | Type d'encodage de la propriété de l'élémen (voir le [tableau](https://docs.ogc.org/is/18-088/18-088.html#tab-encodingtype-codes).| ValueCode  | Obligatoire |
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

