## Pourquoi le SensorThings ?

### Histoire et fondements de l'ouverture des données
Le mouvement actuel autour de l'ouverture des données produites par la recherche scientifique s'inscrit dans un long processus de prêt d'un demi siècle. 
Dès 1978, La **loi CADA** {cite}`cada-1978` veillait à la liberté d’accès aux documents administratifs, aux archives publiques et plus largement à la réutilisation des informations publiques. En 1998, la **convention d'Aarhus** {cite}`aarhus-1998` posait les bases de la démocratie environnementale. cet accord international signé par 49 états visait à améliorer l'information fournie par les autorités publiques, concernant les principales données environnementales. Cet accord fut ensuite renforcé en 2007 par une directive européenne, dite « **Directive Inspire** » {cite}`inspire-2007` afin de créer une infrastructure d’information géographique visant spécifiquement à favoriser la protection de l'environnement en Europe en ouvrant systématiquement au public les données géographiques dès lors qu'elles étaient produites via des fonds publics et disponibles sous forme numérique. Cette directive posait les bases des principes de la mise à disposition des données géographiques qui devait nécessairement respecter les normes et les standards de l'**Open Geospatial Consortium** (OGC). Bien qu'elles entraient dans le champ de la directive INSPIRE, les données produites par la recherche publique et France et plus largement en europe, étaient assez rarement publiées et partagées. Les choses évoluèrement rapidement en 2016 lors de la parution dans la revue Nature de l'article de Wilkinson {cite}`wilkinson:nature-2016` qui posait les bases d’un ensemble minimal de principes et de pratiques pour que les données de la recherche soient Trouvables (**F**indable), **A**ccessible(s), **I**nteroperable(s) et Réutilisables (**R**eusable). Naissait ainsi le **FAIR** data.

### Open data et données géographiques VS données temporelles
L'un des défis rencontrés dans la spécification des exigences de la driective INSPIRE a été l'intégration des données de mesure avec les données spatiales qui composent habituellement une Infrastructure de Données Géographiques {cite}`JRC112221`. Les spécifications et l'adoption par les différentes communautés des standards OGC relatifs aux données géographiques d'une part, et aux données d'observations d'autre part, n'ont pas connu la même histoire et n'ont pas suivi le même chemin.
Précédant de plusieurs années la directive INPIRE, les standards dédiés auxs données géographiques furent edictés très tôt par l'OGC et répondaient aux besoins de visualisation et de téléchargement adaptés aux différents formats: i) le Web Mappging Service (WMS) en 2000 pour la visualisation et l'interrogation, ii) le Web Feature Service (WFS) en 2002 pour le téléchargement des données vectorielles et iii) le Web Coverage Service (WCS) en 2003 pour le téléchargement des données matricielles autrement appelées raster. 

 



La directive Inspire a donc initié 
Distinction géo / tempo
OGC et Données géo -> maturité depuis plus
WMS (2000), WFS (2002), WCS (2003)
01MDonnées d'observation  


### L'ouverture des donnéees d'observation, un long chemin de croix

### L'avènement du standard OGC SensorThings API


Depuis 

Depuis plus de vingt ans, les données produites par    
Le choix du standard OGC **SensorThings** ...

 + FAIR {cite}`wilkinson:nature-2016` --> OGC




Dans le domaine de la FAIRisation des données géographiques, des standards ouverts ont été initiés il y a plus de 20 ans par l'Open Geospatial Consortium (WMS, WFS, WCS, etc.). Aujourd'hui, les outils de diffusion, de partage et de réutilisation de ce type de données ont atteint une certaine maturité, symbolisée par l'avènement des Infrastructures de Données Spatiales (IDS). 

La FAIRisation des données temporelles, telles que celles produites par les observatoires de recherche, n'en est pas au même stade. Différentes tentatives ont émergé au cours de la décennie 2010-2020 autour du standard OGC SOS (Sensor Observation Service) pour publier les journaux d'observation des observatoires et des dispositifs expérimentaux de recherche sur l'environnement (ORE, SOERE, SNO, ZA...). Ce standard a été abandonné principalement pour des raisons de volume dans les échanges client/serveur liées au format XML utilisé.

En 2016, un nouveau standard OGC a émergé, dédié à la FAIRisation des données d'observation ainsi qu'aux IOT sur la base de choix pertinents (JSON, OData, ...) : SensorThings. 
