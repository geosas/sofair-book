## Pourquoi le SensorThings ?

### Histoire et fondements de l'ouverture des données
Le mouvement actuel autour de l'ouverture des données produites par la recherche scientifique s'inscrit dans un long processus de prêt d'un demi siècle. 
Dès 1978, La **loi CADA** {cite}`cada-1978` veillait à la liberté d’accès aux documents administratifs, aux archives publiques et plus largement à la réutilisation des informations publiques. En 1998, la **convention d'Aarhus** {cite}`aarhus-1998` posait les bases de la démocratie environnementale. cet accord international signé par 49 états visait à améliorer l'information fournie par les autorités publiques, concernant les principales données environnementales. Cet accord fut ensuite renforcé en 2007 par une directive européenne, dite « **Directive Inspire** » {cite}`inspire-2007` afin de créer une infrastructure d’information géographique visant spécifiquement à favoriser la protection de l'environnement en Europe en ouvrant systématiquement au public les données géographiques dès lors qu'elles étaient produites via des fonds publics et disponibles sous forme numérique. Cette directive posait les bases des principes de la mise à disposition des données géographiques qui devait nécessairement respecter les normes et les standards de l'**Open Geospatial Consortium** (OGC). Bien qu'elles entraient dans le champ de la directive INSPIRE, les données produites par la recherche publique et France et plus largement en europe, étaient assez rarement publiées et partagées. Les choses évoluèrement rapidement en 2016 lors de la parution dans la revue Nature de l'article de Wilkinson {cite}`wilkinson:nature-2016` qui posait les bases d’un ensemble minimal de principes et de pratiques pour que les données de la recherche soient Trouvables (**F**indable), **A**ccessible(s), **I**nteroperable(s) et Réutilisables (**R**eusable). Naissait ainsi le **FAIR** data.

### Données géographiques VS données temporelles
L'un des défis rencontrés dans la spécification des exigences de la directive INSPIRE a été l'intégration des données de mesure avec les données spatiales qui composent habituellement une Infrastructure de Données Géographiques {cite}`kotsev-2018`. Les spécifications et l'adoption par les différentes communautés des standards OGC relatifs aux données géographiques d'une part, et aux données d'observations d'autre part, n'ont pas connu la même histoire et n'ont pas suivi le même chemin.
Précédant de plusieurs années la directive INSPIRE, les standards dédiés aux données géographiques furent edictés très tôt par l'OGC et répondaient aux besoins de visualisation et de téléchargement adaptés aux différents formats: i) le Web Mappging Service (**WMS**) en 2000 pour la visualisation et l'interrogation, ii) le Web Feature Service (**WFS**) en 2002 pour le téléchargement des données vectorielles et iii) le Web Coverage Service (**WCS**) en 2003 pour le téléchargement des données matricielles autrement appelées raster. 

Du fait de sa complexité, la définition des standards OGC dédiés aux données d'observation et de mesure s'est faites en plusieurs étapes. En premier lieu, 
après la création de prototypes initiaux utilisant des services de données spatiales normalisés tels que le Web Feature Service (WFS), il a été conclu que ces technologies n'étaient pas adaptées à la fourniture de données de mesure. en 2006, l'OGC a alors construit un cadre général pour l'exploitation des capteurs et systèmes de capteurs connectés au web via le standard Sensor Web Enablement (**SWE**) {cite}`ogc-06-021r1`, qui a permis la définition de nouveaux standards {cite}`botts-2008` :
- Observations & Measurements Schema (**O&M**) - Modèles et schéma XML pour le codage des observations et des mesures d'un capteur,
- Sensor Model Language (**SensorML**) - Modèles et schéma XML pour décrire les informations nécessaires à la découverte des capteurs, à la localisation des observations, au traitement des observations et des mesures des capteurs et l'énumération des propriétés mesurées,
- Sensor Observations Service (**SOS**) - Interface de service web standard pour la recherche, le filtrage et le traitement d'observations de capteurs.

A la fin de la décénie 2000-2010, bien que les données géographiques et les données temporelles bénéficiaient, toutes deux, de différents standards OGC permettant leur diffusion dans le cadre défini par la directive INSPIRE (Trouver, Voir, Télécharger), on pouvait faire le constat d'une **assymétrie** dans les facultés de ces standards à répondre aux besoins des utilisateurs.
Pour les données géographiques, l'attelage WMS pour la visualisation et WFS/WCS pour le téléchargement était fonctionnel et adapté au besoins des utilisateurs y conpris pour les données très volumineuses. Pour les données temporelles, l'équivalement du WMS n'existant pas, aucun stadard ne proposait de visualisation et concenrnant le téléchargement, les utlisateurs des services SOS constataient des problèmes de lenteur principalement dûs au format XML proposé par le standard SensorML.


### L'avènement du standard OGC SensorThings API
- bien qu'il soit adopté et déployé par la communauté
- pb de volumétrie du SOS et du SensorML
- A standard for exchanging sensor data and metadata
- Historic data & current data
- JSON Encoded
- RESTful
- Adapting OASIS OData URL patterns and query options
- Supporting ISO MQTT messaging
- Discoverable with only a web browser









En 2016, un nouveau standard OGC a émergé, dédié à la FAIRisation des données d'observation ainsi qu'aux IOT sur la base de choix pertinents (JSON, OData, ...) : SensorThings. 
