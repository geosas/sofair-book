## ObservedProperty

### 1. Définition

Une **propriété observée** spécifie ou définit le phénomène d'une observation.

```{tip}
Dans le cas d'un observatoire, cette propriété peut-être :

- une grandeur physique,
- une observation humaine,
- ...
```

### 2. Propriétés

Une **propriété observée** possède des paramètres obligatoires et des propriétés optionnelles.

| Nom           | Définition                                                                                      | Format               | Exigences   |
| ------------- | ----------------------------------------------------------------------------------------------- | -------------------- | ----------- |
| _name_        | Étiquette correspondant à un **propriété observée**, généralement un nom descriptif court.      | Chaine de caractères | Obligatoire |
| _definition_  | Courte définition de la **propriété observée** ou lien vers thésaurus                           | Chaine de caractères | Obligatoire |
| _description_ | Courte description de la **propriété observée**.                                                | Chaine de caractères | Obligatoire |
| _properties_  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Optionnel            |

#### 2.1. name (obligatoire)

Le champ **name** correspond au nom du phénomène observé au sens générique.

**_Recommandations_**

Le nom étant un nom court et générique, il est recommandé d'ajouter des propiétés optionnelles.

#### 2.2. description** (obligatoire)

Le champ **description** contient une courte description la **propriété observée**.

**_Exemples_**

- Mesure du niveau du cours d'eau
- Concentration en carbone organique dissous de l'eau
- ...

#### 2.3. properties (optionnel)

Le champ **properties** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser un **Sensor**.

**_Recommandations_**

- Il peut être intéressant de préciser l'unité de mesure utilisée.

**_Exemples_**

- Le nom de l'unité
- Le symbole au format SI
- La définition de l'unité
- etc..

### 3. Exemples de ObservedProperty

```json
{
  "name": "electric conductivity",
  "description": "Mesure de la conductivité électrique du cours d'eau",
  "definition": "http://opendata.inrae.fr/thesaurusINRAE/c_14004",
  "properties": {
    "family": "physico-chimie",
    "unit-name": "Mesure de la conductivité électrique du cours d'eau",
    "unit-symbol": "µS/cm",
    "unit-definition": "https://fr.wikipedia.org/wiki/Conductivit%C3%A9_%C3%A9lectrique"
  }
}
```
