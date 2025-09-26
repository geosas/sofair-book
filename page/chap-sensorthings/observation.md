## Observation

### 1. Définition

Une **observation** est l'action de mesurer ou de déterminer la valeur d'une propriété. Elle représente une lecture unique par un capteur d'une propriété observée.
Un dispositif physique, un capteur, envoie des observations à un flux de données spécifique (_datastream_).

```{tip}
Dans le cas d'un observatoire, une **observation** correspond le plus souvent à :

- une valeur mesurée par un capteur
- une mesure manuelle
- une analyse physicochimqique

```

### 2. Propriétés

Une **observation** possède des paramètres obligatoires et des propriétés optionnelles.

| Nom                | Définition                                                                                      | Format                                                                                 | Exigences   |
| ------------------ | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------- |
| **phenomenonTime** | L'instant ou la période où l'**observation** se produit.                                        | Temps ou intervalle de temps                                                             | Obligatoire |
| **result**         | La valeur de l'**observation**.                                                                 | N'importe lequel (dépend du type d'observation défini dans le flux de données associé) | Obligatoire |
| **resultTime**     | L'heure à laquelle le résultat de l'observation a été généré.                                   | Chaîne de temps ISO 8601                                                               | Obligatoire |
| **resultQuality**  | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON                                                                             | Optionel    |
| **validTime**      | La période pendant laquelle le résultat peut être utilisé.                                      | Chaîne de temps ISO 8601                                                               | Optionel    |
| **parameters**     | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON                                                                             | Optionel    |

#### 2.1. phenomenonTime (obligatoire)

Le champ **phenomenonTime** correspond au l'instant où la mesure a été effectuée.

**_Exemple_**

```json
"phenomenonTime": "2001-09-07T09:06:00+02:00"
```

#### 2.2. result (obligatoire)

Le champ **result** contient la valeur de l'**observation**. Elle peut prendre n'importe quelle forme.

**_Recommandations_**

- Dans le cas d'un observatoire c'est souvent une valeur numérique.

**_Exemple_**

```json
"result": "0.231"
```

#### 2.3. resultTime (obligatoire)

Le champ **resultTime** est l'instant exact de la capture d'observation.

**_Exemple_**

```json
{
  "resultTime": "2023-03-01T01:45:01+01:00"
}
```

#### 2.4. resultQuality (optionnel)

Le champ **resultQuality** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser une **observation**.

**_Recommandations_**

- C'est l'endroit possible pour qualifier la mesure ou l'observation.

#### 2.5. validTime (optionnel)

Le champ **validTime** définit une période de validité de l'**observation**.

**_Exemple_**

```json
{
  "validTime": "2024-12-14T11:58:27.330797+01:00"
}
```

#### 2.6. parameters (optionnel)

Le champ **parameters** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser une **observation**.

### 3. Exemple d'observation

```json
{
  "@iot.selfLink": "https://sensorthings.geosas.fr/test//v1.1/Observations(1)",
  "@iot.id": 1,
  "phenomenonTime": "2023-03-01T01:30:01+01:00",
  "result": 200,
  "resultTime": "2023-03-01T01:30:01+01:00",
  "resultQuality": null,
  "validTime": "2024-12-14T11:58:27.330797+01:00",
  "parameters": null,
  "Datastream@iot.navigationLink": "https://sensorthings.geosas.fr/test//v1.1/Observations(1)/Datastream",
  "MultiDatastream@iot.navigationLink": "https://sensorthings.geosas.fr/test//v1.1/Observations(1)/MultiDatastream",
  "FeatureOfInterest@iot.navigationLink": "https://sensorthings.geosas.fr/test//v1.1/Observations(1)/FeatureOfInterest"
}
```
