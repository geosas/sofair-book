## Introduction

Dans le domaine de la FAIRisation des données géographiques, des standards ouverts ont été initiés il y a plus de 20 ans par l'Open Geospatial Consortium (WMS, WFS, WCS, etc.). Aujourd'hui, les outils de diffusion, de partage et de réutilisation de ce type de données ont atteint une certaine maturité, symbolisée par l'avènement des Infrastructures de Données Spatiales (IDS). 

Initié en France en 2010 au sein des UMR SAS et LISAH, puis en 2014 au sein du CATI SIOEA (aujourd'hui GEODEOP), le déploiement de l'IDS geOrchestra a placé l'INRAE parmi les précurseurs de l'Open Data scientifique français pour les données dites " environnementales ".

La FAIRisation des données temporelles, telles que celles produites par les observatoires de recherche, n'en est pas au même stade. Différentes tentatives ont émergé au cours de la décennie 2010-2020 autour du standard OGC SOS (Sensor Observation Service) pour publier les journaux d'observation des observatoires et des dispositifs expérimentaux de recherche sur l'environnement (ORE, SOERE, SNO, ZA...). Ce standard a été abandonné principalement pour des raisons de volume dans les échanges client/serveur liées au format XML utilisé.

En 2016, un nouveau standard OGC a émergé, dédié à la FAIRisation des données d'observation ainsi qu'aux IOT sur la base de choix pertinents (JSON, OData, ...) : SensorThings. 
Nous proposons ici de présenter le projet SOFAIR (Sensor Observations to FAIR data) [squividant:hal-04236491], un middleware pour simplifier, automatiser et guider la FAIRisation des données temporelles. 

Ce projet propose 
1. la création d'une nouvelle instance de SensorThings,
2. des méthodes de configuration de cette instance,
3. différents chemins de données du capteur vers le service,
4. la connexion de ce service aux infrastructures de données géographiques en termes de métadonnées et de couches géographiques,
5. la génération de visualisateurs de ce service dans des portails cartographiques ou temporels.

Cet outil nous semble être le chaînon manquant dans le concept d'**Infrastructure de Données Spatiales et Temporelles** : STDS.
