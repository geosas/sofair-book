## ObservedProperty  

## **1. Définition** 
Une **propriété observée** spécifie ou définie le phénomène d'une observation.

```{tip}
Dans le cas d'un observatoire, cette propriété peut-être:
* Une grandeur physique
* Une observation humaine
* ...
```

## **2. Propriètés**  
Une **propriété observée** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| *name* | Étiquette correspondant à un *propriété observée*, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| *definition* | Courte définition du *propriété observée* ou lien vers thésaurus | Chaine de caractères  | Obligatoire |
| *description*  | Courte descriptin de la *propriété observée*.| Chaine de caractères  | Obligatoire |
| *properties* | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Optionnel |

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
