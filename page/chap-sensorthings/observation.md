## **Observation**  

## **1. Définition** 
Une **observation** est l'action de mesurer ou de déterminer la valeur d'une propriété. Elle représente une lecture unique par un capteur d'une propriété observée.
Un dispositif physique, un capteur, envoie des observations à un flux de données spécifique (datastream).  

```{tip}
Dans le cas d'un observatoire, une **observation** est souvent:
* une valeur mesurée par un capteur.
* une analyse  physicochimqique
* une mesure manuuelle
```

## **2. Propriètés**  
Une **observation** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **phenomenonTime** | L'instant ou la période où l'**observation** se produit.| Temps ou  interval de temps | Obligatoire |
| **result** | La valeur de l'**observation**. | N'importe lequel (dépend du type d'observation défini dans le flux de données associé)  | Obligatoire |
| **resultTime**  | L'heure à laquelle le résultat de l'observation a été généré. | Chaîne de temps ISO 8601  | Obligatoire |
| **resultQuality**  | Décrit la qualité du résultat. | Chaîne de temps ISO 8601  | Optionel |
| **validTime**  | La période pendant laquelle le résultat peut être utilisé. | Chaîne de temps ISO 8601  | Optionel |
| **parameters**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON  | Optionel |

### **2.1. phenomenonTime** (obligatoire) 
Le champ **phenomenonTime** correspond au l'instant où la mesure  a été effectuée.

***Exemple***  

```{json}
"phenomenonTime": "2001-09-07T09:06:00+02:00"
```

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


