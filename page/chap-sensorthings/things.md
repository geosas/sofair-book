## Thing

### 1. Définition

Une **Thing** est comme un objet du monde physique (objets physiques) ou du monde de l’information (objets virtuels) qui peut être identifié et intégré dans des réseaux de communication.

```{tip}
Dans le cas d'un observatoire, tout dépend du grain de précision souhaité, une **Thing** peut faire référence à :

- un point ou une zone de mesure,
- une centrale de mesure,
- un capteur,
- ...
```

### **2. Propriétés**

Une **Thing** possède des paramètres obligatoires et des propriétés optionnelles.

| Nom             | Définition                                                                                      | Format               | Exigences   |
| --------------- | ----------------------------------------------------------------------------------------------- | -------------------- | ----------- |
| **name**        | Étiquette correspondant à une **Thing**, généralement un nom descriptif court.                  | Chaine de caractères | Obligatoire |
| **description** | Courte description de la **Thing**.                                                             | Chaine de caractères | Obligatoire |
| **properties**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON           | Optionnel   |

#### 2.1. name (obligatoire)

Le champ **name** correspond à une étiquette ou à un identifiant de la **Thing**, généralement sous la forme d’un nom descriptif court.

**_Recommandations_**

Il est recommandé de faire apparaitre le type du capteur ainsi que le nom du site.

**_Exemples_**

```json
"name": "Station météo Campbell EFELE"
```
```json
"name": "Naizin Kervidy Exutoire"
```
#### 2.2. description (obligatoire)

Le champ **description** contient une courte description de la **Thing**.

**_Recommandations_**

- Il est recommandé d'expliciter la **Thing**, pour éviter l'utilisattion d'acronymes.

**_Exemples_**

```json
"description": "Station météo Campbell personnalisée, équipée du data logger Campbell CR1000"
```
```json
"description": "Exutoire du bassin versant de Kervidy à Naizin"
```

#### 2.3. properties (optionnel)

Le champ **properties** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser une **Thing**.

**_Recommandations_**

- Le standard SensorThings ne donne aucune indication concernant les noms des propriètés que l'on peut associer à l'objet Things. On peut donc considérer que le choix de ces noms de proriètés est totalement libre. Cependant, il y a un intérêt à opter pour des noms admis par la communauté du web. Par exemple, [schema.org](https://schema.org/Thing) ou [W3C](https://www.w3.org/TR/vocab-ssn/) proposent des vocabulaires couvrant les entités, les relations entre les entités et les actions pouvant être utlisés comme des propriètés des objets SensorThings.

**_Exemples_**
- Observatoire urbain de Beauregard à Rennes

Pour cet observatoire, les propriètés [elevation](https://schema.org/elevation) et [image](https://schema.org/image) ont été choisies dans les vocabulaires décrits dans [https://schema.org](https://schema.org). 

```json
"properties": {
        "elevation": 55.6,
        "image": "https://geosas.fr/cityorchestra/img/pdm/ST1-1.jpg"
}
```

Dans les 2 exemples suivants, les noms de propriètés ont été choisis librement.

- SOERE PRO EFELE

```json
 "properties": {
  "projet": "https://geosas.fr/web/?page_id=2476",
  "manuel d'utilisation": "https://s.campbellsci.com/documents/fr/product-brochures/b_cr1000.pdf",
  "date de mise en place": "Septembre 2013"
}
```

- ORE AgrHyS

```json
 "properties": {
  "region": "B_Naizin",
  "domaine": "NAIZIN",
  "station": "KERVIDY_B_EXU"
}
```

### 3. Exemples

Cet exemple montre le contenu intégral d'une **thing** après injection dans le service SensorThings. Seuls les champs **name**, **description** et **proriètés** ont été renseignés par l'opérateur. Tous les autres champs **@iot.id**, **@iot.selfLink**, **Locations@iot.navigationLink**, **HistoricalLocations@iot.navigationLink**, **Datastreams@iot.navigationLink** et **Datastreams@iot.navigationLink** ont été générés automatiquent par le service.

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
