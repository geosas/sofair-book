## REX CoLiSHyM'Eaux

### Qui parle ?
                    
![Nicolas Le Moine](/img/nicolas.png) Nicolas Le Moine, maître de conférence en géomatique à l'Institut Agro, hydrologue.

### CoLiKézaco ? Eléments de contexte

CoLiSHyM'Eaux, c'est un projet financé par l'Agence de l'Eau Seine Normandie, dont l'objectif est de comprendre le fonctionnement hydrodynamique et biogéochimique d'une zone humide rétro-littorale située sur la côte du Bessin, dans le Calvados, notamment en réponse à l'élévation du niveau de la mer. Cet acronyme infernal à écrire signifie : Connectivité Littorale entre Sols, Hydrosystèmes superficiels, Mer et Eaux souterraines. Le projet a démarré en avril 2025, on est au tout début, il y a un gros travail d'instrumentation à mener d'ici -- et pendant -- le démarrage d'une thèse à la rentrée 2026.


### Une idée qui émerge petit-à-petit : tester le FAIR by design

Comme dans tout projet de métrologie en environnement, on a bien sûr des aspects purement techniques à gérer (choix des capteurs, "ancrage" sur site, alimentation, etc.), mais aussi des aspects juridiques et réglementaires puisqu'il faut s'assurer de l'accord du/des propriétaire(s) des parcelles instrumentées, le formaliser par des conventions, etc. Dans le cas de CoLiSHyM'Eaux, le contexte du marais maritime multiplie les interlocuteurs :

- la SCI des Dunes, propriétaire de la quasi-totalité des terrains dans la moitié ouest du marais,
- le Conservatoire du Littoral, propriétaire d'un bon nombre de parcelles dans la moitié est,
- le Syndicat Mixte Littoral Normand, qui porte le contrat Natura 2000 de ce périmètre classé,
- la DDTM du Calvados, qui instruit les demandes d'autorisation de travaux sur ce périmètre,
- l'Autorité Routière Départementale (ARD 14) pour les travaux dans l'emprise de la départementale délimitant le site au sud,
- les mairies de Ver-sur-Mer et Meuvaines pour les travaux dans l'emprise des voies communales
- ...

Pour complexifier encore les choses, ces acteurs ont des visions assez antagonistes de l'avenir de cet espace, avec deux modes de gestion diamétralement opposés : dans la partie est du marais, le Conservatoire du Littoral part du principe que ces espaces sont perdus à moyen terme, et qu'il ne sert à rien d'entretenir à grands frais une protection frontale (enrochements, épis, etc.) contre les épisodes de submersions marines amenés à croître en fréquence et en intensité. De fait, dans ce secteur est on voit clairement, à chaque tempête ou marée de fort coefficient, le cordon dunaire se démanteler ou migrer vers la paléo-falaise au pied de laquelle le marais s'étend. Inversement, dans le secteur ouest, où la chasse au gabion est l'activité principale, le maintien du caractère "marais d'eau douce" est priorisé et la protection frontale entretenue. L'un des enjeux du projet, avant même son démarrage, a donc été de faire accepter la démarche d'instrumentation en restant "neutre" sur la vision du territoire, en expliquant simplement aux acteurs que l'objectif était de produire d'abord de la connaissance, et non pas des recommandations de gestion.

Pour cela, il a donc fallu imaginer des outils pour "faire voir" ce à quoi ressemblerait l'observatoire : points de mesure, emprise des instruments, paramètres mesurés, partage des données produites, etc. Les cartes statiques sont intéressantes, mais c'est en regardant ce qui avait été fait par Tom Lorée sur l'observatoire urbain du projet City Orchestra à Beauregard que la solution SensorThings s'est imposée non seulement comme un standard de diffusion intéressant (quand les capteurs commenceront à produire de la données), mais aussi comme un outil de conception, de maquettage de l'observatoire avant même l'achat du premier capteur. La vision synthétique du STAV et les différentes entrées (géographique / data streams / capteurs) permet de naviguer facilement entre ces différentes facettes et communiquer aussi bien avec les acteurs du territoire qu'avec les fournisseurs de matériel pour expliquer les objectifs et les contraintes. Au niveau pratique, ça évite de multiplier les plans par exemple (carte générale au 1/25000, puis plans cadastraux locaux, etc.). On peut directement décrire et documenter les Things avec une vision très proche du terrain, de la facilité / difficulté à accéder au capteur, etc.

Ca force même à réfléchir, au cas-par-cas, ce que désigne exactement chaque Thing. Par exemple on peut partir avec l'idée initiale qu'un station hydrométrique au niveau d'un pont c'est une Thing globale, mais à la réflexion si on mesure quelque chose côté amont, et autre chose côté aval, est-ce que c'est la même Thing ? Si à l'aval il y a par exemple une buse avec un jet dénoyé, il faut peut-être conceptualiser deux Things distinctes, etc. En plus il faut traverser la route pour passer d'un côté à l'autre, on ne peut peut-être pas passer un câble d'alimentation dans la buse... Bref, on peut avoir différentes choses (things) presque au même endroit (location), idem pour un doublet de forages par exemple. Ainsi à plusieurs reprises j'ai finalement "scindé" des Things que j'avais en première intention considérées de façon trop globale et ça, au niveau de la conception, ça aide.


...
