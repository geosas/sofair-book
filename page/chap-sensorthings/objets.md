## Les entités SensorThings

Le modèle de données SensorThings API repose sur plusieurs entités clés permettant de structurer et d'interroger les informations et données diffusées par les services conformes à ce standard. Ces différentes entités sont interconnectées, facilitant ainsi l'organisation des objets physiques, des types d'observations, des mesures et de leurs relations géographiques. 
Voici un résumé des principales entités et de leurs relations :

1. **Thing** : Représente un objet physique, une machine ou un équipement qui regroupe des capteurs et génère des observations en un point donné.
2. **Sensor** : Représente un capteur ou un dispositif de mesure. Chaque capteur mesure un ou plusieurs types d'observation (ObservedProperties).
3. **ObservedProperty** : définit le phénomène ou la caractéristique mesurée par un capteur, comme par exemple, la température ou l'humidité.
4. **Location** : Représente la géolocalisation d’un Thing. Les coordonnées géographiques sont stockées sous forme de géométries, généralement représentées par des points et plus rarement par des polygones.
5. **Datastream** : Représente une série de mesures représentée par une chronique provenant d’un capteur spécifique, associée à un type d'observation, comme par exemple, la chronique de l'évolution de la témpérature quotidienne de la station météo Brest-Guipavas du 1er janvier 2020 au 31 décembre 2024.
6. **Observation** : Représente une mesure spécifique dans un Datastream à un instant donné. Chaque observation contient la valeur mesurée et le moment de la mesure 

Le plus souvent, les services de diffusion de données d'observation reposant sur le standard OGC SensorThings API n'utilisent pas les entités **HistoricalLocation**, **Multidatastreams** et **FeatureOFInterest**.


```{figure} img/STA_entities.png
:alt: Les différentes entités du SensorThings et leurs relations.
:width: 800px
:align: center
Les différentes entités du SensorThings et leurs relations.
```
Le paragraphe [Sensing entities](https://docs.ogc.org/is/18-088/18-088.html#sensing-entities2) du document de référénce de l'API SensorThings indique les définitions officielles des entités SensorThings. Les pages suivantes fournissent des définitions simplifiées et adaptaptées à des observatoires, ainsi que les paramètres nécessaires à renseigner pour chacune de ces entités.
