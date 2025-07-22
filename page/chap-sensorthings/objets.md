## Les entités SensorThings

Le modèle de données SensorThings API repose sur plusieurs entités clés permettant de structurer et d'interroger les informations et données diffusées par les services conformes à ce standard. Ces différentes entités sont interconnectées, facilitant ainsi l'organisation des objets physiques, des types d'observation, des mesures et de leurs relations géographiques. 
Voici un résumé des principales entités et de leurs relations :

1. **[Thing](https://geosas.fr/sofair-book/page/chap-sensorthings/things.html)** : Représente un objet physique, une machine ou un équipement qui regroupe des capteurs et génère des observations en un point donné. Un ***Thing*** peut avoir plusieurs ***Datastreams*** ou chronique associée. Un ***Thing*** est généralement géolocalisé par sa ***Location***.
3. **[Sensor](https://geosas.fr/sofair-book/page/chap-sensorthings/sensors.html)** : Représente un capteur ou un dispositif de mesure. Chaque capteur mesure un ou plusieurs types d'observation (ObservedProperties). Un ***Sensor*** est associé à un ou plusieurs ***Datastream***.
4. **[ObservedProperty](https://geosas.fr/sofair-book/page/chap-sensorthings/observedproperties.html)** : définit le phénomène ou la caractéristique mesurée par un capteur, comme par exemple, la température ou l'humidité. Une ***ObservedProperty*** est associée à un ou plusieurs ***Datastreams***.
5. **[Location](https://geosas.fr/sofair-book/page/chap-sensorthings/location.html)** : Représente la géolocalisation d’un Thing. Les coordonnées géographiques sont stockées sous forme de géométries, généralement représentées par des points et plus rarement par des polygones. Une ***Location*** est associée à un ***Thing***.
6. **[Datastream](https://geosas.fr/sofair-book/page/chap-sensorthings/datastream.html)** : Représente une série de mesures représentée par une chronique provenant d’un capteur spécifique, associée à un type d'observation, comme par exemple, la chronique de l'évolution de la témpérature quotidienne de la station météo Brest-Guipavas du 1er janvier 2020 au 31 décembre 2024. Un ***Datastream*** est nécessairement associé à un ***Thing***, un ***Sensor*** et une ***ObservedProperty***. 
7. **[Observation](https://geosas.fr/sofair-book/page/chap-sensorthings/observation.html)** : Représente une mesure spécifique à un instant donné. Une ***Observation*** est nécessairement reliée à un ***Datastream***.

Le plus souvent, les services de diffusion de données d'observation reposant sur le standard [OGC SensorThings API](https://www.ogc.org/fr/standards/sensorthings/) n'utilisent pas les entités **HistoricalLocation**, **Multidatastreams** et **FeatureOFInterest**.


```{figure} img/STA_entities.png
:alt: Les différentes entités du SensorThings et leurs relations.
:width: 800px
:align: center
Les différentes entités du SensorThings et leurs relations.
```

Le paragraphe [Sensing entities](https://docs.ogc.org/is/18-088/18-088.html#sensing-entities2) du document de référénce de l'API SensorThings indique les définitions officielles des entités SensorThings. Les pages suivantes fournissent des définitions simplifiées et adaptaptées à des observatoires, ainsi que les paramètres nécessaires à renseigner pour chacune de ces entités.  

  ## Synthèse  
  

| Sensorthing        | concrètement                                                                                  |
| :------------------|:----------------------------------------------------------------------------------------------|
| Thing              | Qu'est-ce qui nous interesse ? un objet physique ou virtuel qu'on l'on souhaite étudier       |
| ObservedProperty   | Qu'est-ce qu'on souhaite observer ?  Le phénomène observé                                     |
| Sensor             | Comment, avec quel instrument ?                                                               |
| DataStream         | Qu'est-ce qu'on obtient avec le "sensor" ?  Une collection d'observations via un même capteur |
| Observation        | L'action de mesurer le phénomène observé                                                      |
| FeatureOfInterest  | Informations apportant du contexte à la mesure réalisée                                       |
| Location           | localisation de l'instrument                                                                  |
| HistoricalLocation | Historique de localisation de l'instrument                                                    |
