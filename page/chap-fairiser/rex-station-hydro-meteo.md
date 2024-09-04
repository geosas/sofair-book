# REX Station Hydro-Météo

## Qui parle ?
                    
![Paloma](/img/paloma.png) Paloma Cucchi, ingénieure d'étude contractuelle à l'Institut Agro, géomaticienne.


## Objectif

Création d'un service numérique "SensorThings" pour la diffusion des données météorologiques et hydrologiques de la station de mesure de l'Institut Agro Rennes-Angers.

## Différentes étapes

- Comprendre et prendre en main ce qu'est un SensorThings, comment ça s'articule par le biais de réunion et de temps d'information (quelques mois).
- Se renseigner de comment créer, configurer un service = présentation des différents volets d'un SensorThings, de ce qui existe déjà en la matière (Aghrys).
- Reprise du fichier de configuration d'AgrHyS pour concevoir le service.
- Aller voir sur place où est la station, savoir comment elle fonctionne, comment on récupère la donnée, à quelle fréquence et combien de capteurs mesurent quelles données. Une demi journée avec les techniciens d'une journée type où ils vont récupérer la donnée.
- Explication avec les techniciens de comment la centrale est programmée en fonction des capteurs qu'elle a, démonstration dans le logiciel, export d'un programme type pour voir le nom des variables en sortie.
- Comprendre que le logiciel qui programme les mesures sort un certain nombre de variables qui n'a pas le même nom que dans les fichiers présents sur les serveurs. Il a fallu prendre du temps aussi pour ça avec les techniciens afin que je comprenne la nomenclature précise des variables. Je me suis retrouvée avec 3 dénominations différentes pour la même variable mesurée, car le nom par défaut n'étant pas très explicite.
- Remplir le fichier de configuration était assez lourd compte tenu du caractère redondant de sa conception. Mais c'est ce qui m'a permis de bien différencier le "datastream", de l'"observed property" ainsi que du "sensor" et de la "thing". Rien ne vaut la répétition pour comprendre et de mettre les mains dedans.
- Une fois avoir défini les capteurs et renseigner leur documentation frabricant, fait la liste des variables avec leur définition scientifique liée au thesorus ; nous avons un fichier de configuration qui permet déjà d'y voir plus clair et de mieux apprécier l'écosystème d'un SensorThing. J'étais à ce moment plus capable, de l'expliquer et surtout de le restituer aux techniciens qui leur permette d'avoir photographie de l'organisation de la donnée.
- Après le jeu s'est fait entre le scientifique, les techniciens et moi (accompagnant) pour avoir une nomenclature finale de chaque variable qui soit parlante et le plus près de la mesure faite par le capteur.
- Test du fichier de configuration pour voir s'il n'y avait pas de problème.
