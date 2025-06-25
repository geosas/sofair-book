## Les entités SensorThings

Le modèle de données SensorThings API repose sur plusieurs entités clés permettant de structurer et d'interroger les informations et données diffusées par les services conformes à ce standard OGC. Ces différentes entités sont interconnectées, facilitant ainsi l'organisation des objets physiques, des types d'observations, des mesures et de leurs relations géographiques. 
Voici un résumé des principales entités et de leurs relations :

1. **Thing** : Représente un objet physique, une machine ou un équipement qui regroupe des capteurs et génère des observations en un point donné.
2. **Sensor** : Représente un capteur ou un dispositif de mesure. Chaque capteur mesure un ou plusieurs types d'observations (ObservedProperties).
3. **ObservedProperty** : définit le phénomène ou la caractéristique mesurée par un capteur, comme par exemple, la température ou l'humidité.
4. **Location** : Représente la géolocalisation d’un Thing. Les coordonnées géographiques sont stockées sous forme de géométries, généralement représentées par des point et parfois par des polygones.
5. **Datastream** : Représente une série de mesures représentée par une chronique provenant d’un capteur spécifique, associée à un type d'observation (par exemple, la température ou l’humidité).
6. **Observation** : Représente une mesure spécifique dans un Datastream à un instant donné. Chaque observation contient la valeur mesurée et le moment de la mesure 

  
Vous trouverez les définitions officielles des objets Sensorthings, appelés égalment entités, sur le site de [Open Geospatial Consortium](https://docs.ogc.org/is/18-088/18-088.html#sensing-entities2).  
Les pages suivantes fournissent des définitions simplifiées et adaptaptées à des observatoies, ainsi que les parammatres nécessaires à renseigner.

```{figure} img/STA_entities.png
:alt: Les différents objets du SensorThings et leurs relations.
:width: 800px
:align: center
Les différents objets du SensorThings et leurs relations.
```
