## Les entités SensorThings

Le modèle de données SensorThings API repose sur plusieurs entités clés permettant de structurer et d'interroger les informations et données diffusées par les services conformes à ce standard. Ces différentes entités sont interconnectées, facilitant ainsi l'organisation des objets physiques, des types d'observation, des mesures et de leurs relations géographiques.
Voici un résumé des principales entités et de leurs relations :

1. **[Thing](https://geosas.fr/sofair-book/page/chap-sensorthings/things.html)** : représente un objet physique, une machine ou un équipement qui regroupe des capteurs et génère des observations en un point donné. Un **_Thing_** peut avoir plusieurs **_Datastreams_** ou chronique associée. Un **_Thing_** est généralement géolocalisé par sa **_Location_**.
2. **[FeatureOfInterest](https://geosas.fr/sofair-book/page/chap-sensorthings/featureofinterest.html)** : définit ou décrit l'objet observé (ex: un bassin versant).
3. **[Sensor](https://geosas.fr/sofair-book/page/chap-sensorthings/sensors.html)** : représente un capteur ou un dispositif de mesure. Chaque capteur mesure un ou plusieurs types d'observation (_ObservedProperties_). Un **_Sensor_** est associé à un ou plusieurs **_Datastream_**.
4. **[ObservedProperty](https://geosas.fr/sofair-book/page/chap-sensorthings/observedproperties.html)** : définit le phénomène ou la caractéristique mesurée par un capteur, comme par exemple, la température ou l'humidité. Une **_ObservedProperty_** est associée à un ou plusieurs **_Datastreams_**.
5. **[Location](https://geosas.fr/sofair-book/page/chap-sensorthings/location.html)** : représente la géolocalisation d’un _Thing_. Les coordonnées géographiques sont stockées sous forme de géométries, généralement représentées par des points et plus rarement par des polygones. Une **_Location_** est associée à un **_Thing_**.
6. **[Datastream](https://geosas.fr/sofair-book/page/chap-sensorthings/datastream.html)** : représente une série de mesures représentée par une chronique provenant d’un capteur spécifique, associée à un type d'observation, comme par exemple, la chronique de l'évolution de la témpérature quotidienne de la station météo Brest-Guipavas du 1er janvier 2020 au 31 décembre 2024. Un **_Datastream_** est nécessairement associé à un **_Thing_**, un **_Sensor_** et une **_ObservedProperty_**.
7. **[Observation](https://geosas.fr/sofair-book/page/chap-sensorthings/observation.html)** : représente une mesure spécifique à un instant donné. Une **_Observation_** est nécessairement reliée à un **_Datastream_**.

Le plus souvent, les services de diffusion de données d'observation reposant sur le standard [OGC SensorThings API](https://www.ogc.org/fr/standards/sensorthings/) n'utilisent pas les entités **HistoricalLocation** et **Multidatastreams**.
```{figure} img/STA_entities.png
:alt: Les différentes entités du SensorThings et leurs relations.
:width: 800px
:align: center
Les différentes entités du SensorThings et leurs relations.
```

Le paragraphe [Sensing entities](https://docs.ogc.org/is/18-088/18-088.html#sensing-entities2) du document de référénce de l'API SensorThings indique les définitions officielles des entités SensorThings. Les pages suivantes fournissent des définitions simplifiées et adaptaptées à des observatoires, ainsi que les paramètres nécessaires à renseigner pour chacune de ces entités.

```{Note}
| SensorThings        | concrètement                                                                                  |
| :----------------- | :-------------------------------------------------------------------------------------------- |
| Thing              | Qu'est-ce qui nous intéresse ? Un objet physique ou virtuel qu'on l'on souhaite étudier.      |
| ObservedProperty   | Qu'est-ce qu'on souhaite observer ? Le phénomène observé.                                     |
| Sensor             | Comment, avec quel instrument ?                                                               |
| DataStream         | Qu'est-ce qu'on obtient avec le "sensor" ? Une collection d'observations via un même capteur repésentée par une chronique |
| Observation        | L'action de mesurer le phénomène observé.                                                      |
| FeatureOfInterest  | Informations apportant du contexte à la mesure réalisée.                                      |
| Location           | Géolocalisation de l'instrument, du capteur.                                                          |
| HistoricalLocation | Historique de localisation de l'instrument. Pertinent pour les capteurs mobiles, généralement sans objet dans le cas des observatoires de recherche. |
```
