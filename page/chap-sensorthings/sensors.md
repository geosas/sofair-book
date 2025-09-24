## **Sensor**

### **1. Définition**

Un **Sensor** est un instrument qui observe ou mesure, une propriété ou un phénomène dans le but de produire une estimation de sa valeur.

```{tip}
Dans le cas d'un observatoire, un **Sensor** est le plus souvent :

- un capteur,
- une analyse physico-chimique,
- une valeur calculée à partir de mesures.
```

### **2. Propriétés**

Un **Sensor** possède des paramètres obligatoires et des propriétés optionnelles.

| Nom               | Définition                                                                                      | Format                   | Exigences   |
| ----------------- | ----------------------------------------------------------------------------------------------- | ------------------------ | ----------- |
| **name**          | Étiquette correspondant à un **Sensor**, généralement un nom descriptif court.                  | Chaine de caractères     | Obligatoire |
| **description**   | Courte description du **Sensor**.                                                               | Chaine de caractères     | Obligatoire |
| **encoding type** | Définit le type de métadonnée.                                                                  | HTML ou PDF ou SensorML  | Obligatoire |
| **metadata**      | Description détaillée du capteur, lien vers la documentation                                    | dépend de encoding type. | Obligatoire |
| **properties**    | Objet JSON contenant les propriétés annotées par l’utilisateur sous forme de paires clé-valeur. | Objet JSON               | Optionnel   |

#### **2.1. name** (obligatoire)

Le champ **name** correspond à une étiquette/un identifiant le **Sensor**, généralement sous la forme d’un nom descriptif court.

**_Recommandations_**

Il est recommandé de faire apparaitre le type du capteur et le modèle (informations techniques).

**_Exemples_**

- OTT Thalimede
- Wimesure Pt100
- Turbidimeter Ponsel

#### **2.2. description** (obligatoire)

Le champ **description** contient une courte description le **Sensor**.

**_Recommandations_**

- Il est recommandé d'expliciter le **Sensor**, surtout dans le cas d'utilisattion d'un codage.

**_Exemples_**

- Analyseur en ligne de phosphore
- Relève de niveau d'eau sur échelle limnimétrique
- Capteur d'oxygène dissous dans l'eau et de température de l'eau

#### **2.3. encoding type** (obligatoire)

Le champ **encoding type** se réfère à des valeurs prédéfinies (HTML ou PDF ou SensorML) et définit le codage des métadonnées.

**_Recommandations_**

- Dans le cas d'un **sensor**, l'encodage se réfère au type de documentation, le plus souent une URL ou un PDF.

**_Exemples_**

- HTML
- PDF

#### **2.4. metadata** (obligatoire)

Le champ **metadata** indique la source de la description détaillée du **sensor**.

**_Recommandations_**

- Lien vers le site constructeur ou un fichier PDF.

**_Exemples_**

- https://www.pme.com/wp-content/uploads/PME-miniDOT-Manual-2021.pdf
- https://vanessen.com/images/PDFs/Diver-ProductManual-en.pdf

#### **2.5. properties** (optionnel)

Le champ **properties** est un objet JSON (paires clé-valeur). Elles sont définies à la conception et permettent de mieux caractériser un **Sensor**.

**_Recommandations_**

- Il peut être intéressant de renseigner les caractéristiques techniques du capteur.

**_Exemples_**

- ORE AgrHyS

```json
{
  "Vmax": "Niveau  10m ou 50m ou 100m
  Température -80°C
  Conductivité 120 mS/cm",
  "Vmin": "Niveau 0 m
  Température -20°C
  Conductivité 0 µS/cm",
  "Accuracy": "Niveau  précision +/- 0,2% de la pleine échelle Température précision +/- 0,2°C
  Conductivité +/- 0,1% de la valeur mesurée"
}
```

### **3. Exemples de Sensor**

```json
{
    "@iot.selfLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Sensors(8)",
    "@iot.id": 8,
    "name": "Diver CTD",
    "description": "Capteur de niveau, de conductivité électrique et de témpérature de l'eau",
    "encodingType": "application/pdf",
    "metadata": "https://vanessen.com/images/PDFs/Diver-ProductManual-en.pdf",
    "properties": {
        "Vmax": "Niveau  10m ou 50m ou 100m
        Température -80°C
        Conductivité 120 mS/cm",
        "Vmin": "Niveau 0 m
        Température -20°C
        Conductivité 0 µS/cm",
        "Accuracy": "Niveau  précision +/- 0,2% de la pleine échelle Température précision +/- 0,2°C
        Conductivité +/- 0,1% de la valeur mesurée"
    },
    "Datastreams@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Sensors(8)/Datastreams",
    "MultiDatastreams@iot.navigationLink": "https://sensorthings.geosas.fr/agrhys/v1.1/Sensors(8)/MultiDatastreams"
}

```
