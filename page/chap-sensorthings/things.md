# **Things**  

## **Définition** 
Une **Thing** comme un objet du monde physique (objets physiques) ou du monde de l’information (objets virtuels) qui peut être identifié et intégré dans des réseaux de communication.
```{tip}
Dans le cas d'un observatoire, tout dépend du grain de précision souhaité, une **Thing** peut faire référence à:
* un point ou une zone de mesure.
* une centrale de mesure.
* un capteur.
```

## **Propriètés**  
Une **Thing** posséde des paramètres obligatoires et des propriétés optionnelles.

|  Nom |  Définition | Format | Exigences |
|---|---|---|---|
| **name** | Étiquette correspondant à une **Thing**, généralement un nom descriptif court.| Chaine de caractères  | Obligatoire |
| **description** | Courte description de la **Thing**. | Chaine de caractères  | Obligatoire |
| **properties**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON  | Optionnelle |

Tableau 1. Les différentes propriétés de l’entité **Thing**.

### 1. **name** (obligatoire) 
Le champ **name** correspond à une étiquette/un identifiant de la **Thing**, généralement sous la forme d’un nom descriptif court.

***Recommandations***  

Il est recommandé de faire apparaitre le type du capteur ainsi que le nom du site.

***Exemples***  

* Station météo Campbell EFELE  
* Kerbenez Puits E30  
* Naizin Kervidy Exutoire  

### 2. **description** (obligatoire)  

Le champ **description** contient une courte description de la **Thing**.

***Recommandations***  

* Il est recommandé d'expliciter la **Thing**, surtout dans le cas d'utilisattion d'acronymes. 

***Exemples à suivre***  

* Station météo Campbell personnalisée, équipée du data logger Campbell CR1000
* Exutoire du bassin versant du Puits
* Exutoir à Naizin Kervidy

#### 3. **properties** (optionel)  

Le champ **properties** est un objet JSON (paires/clé-valeur). Elles sont définies à la conception et permet de mieux caractériser une **Thing**.  

***Recommandations***

* Pas de réelles recommandations. Les propriètés étant non standardisées, ne pas les considérer comme un élément descriminant pouvant être utilisé dans une requête. Nécessite également de bien documenter pour informer les utlisateurs de leurs existances.

**Exemples***  

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
### **Exemples Thing**   

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
