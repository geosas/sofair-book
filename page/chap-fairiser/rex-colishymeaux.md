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

### Echantillons de correspondance
#### *Avec l'Autorité Routière Départementale 14*
![ARD 14-1](/img/colishymeaux-ARD1.png)
![ARD 14-2](/img/colishymeaux-ARD2.png)
![ARD 14-3](/img/colishymeaux-ARD3.png)

#### *Avec l'animateur du site Natura 2000*
![anim_natura2000](/img//colishymeaux-anim_natura2000.png)

#### *Avec une société qui fournit des sondes spectro UV immergeables*
![spectro1]([spectro1](/img/colishymeaux-spectro1.png))
![spectro2]([spectro1](/img/colishymeaux-spectro2.png))

### Outils de FAIRisation
Le service https://frost.geosas.fr/colishymeaux/v1.1/ a été créé par Hervé Squividant. Ensuite, j'ai intégralement peuplé le service par des requêtes sous R. J'avais un peu de pratique des API, sous R en particulier (réanalyse ERA5 de l'ECMWF, Météo France, HubEau, etc.) donc ça a été assez simple, le design RESTful est même encore plus simple puisqu'il n'y a pas besoin de charger un package dédié (genre https://cran.r-project.org/package=ecmwfr ou https://cran.r-project.org/package=hubeau). 
Tout se fait par des requêtes HTTP et des fichiers JSON, on a juste besoin de :
```
# Chargement des packages requis
library(httr)
library(jsonlite)
library(rstudioapi) # optionnel
```
La connection au service est simple :
```
# Fonction pour récupérer un jeton
get_token <- function(url_logging, user, pswd) {
  response <- POST(url_logging, body = toJSON(list(user = user, pswd = pswd)), encode = "json")
  
  if (status_code(response) == 201) {
    print("connexion OK")
    content <- content(response, as = "parsed", type = "application/json")
    token <- content$token
    return(token)
  } else {
    print(content(response))
  }
}

# L'URL du service
url <- 'https://frost.geosas.fr/colishymeaux/v1.1/'

# Pour éviter de mettre les identifiants en dur dans le script :
user <- rstudioapi::askForPassword("username :")
pswd <- rstudioapi::askForPassword("password :")
url_logging = 'https://frost.geosas.fr/proxy_login'

# Connection
token=get_token(url_logging,user,pswd)
```
Pour créer des things, des sensors, des observed_properties ou des datastreams, c'est simple, on peut même faire des boucles si on a des des catégories de things comme des piézos. Là le couplage avec les packages geospatiaux de R (sf, sp, terra, etc.) est vraiment hyper-pratique, rien à rentrer en dur si on a par exemple les emplacements dans des fichiers shapefile ou geopackage :
```
library(sf)

piezos <- read_sf(dsn="/home/lemoinen/IARA/Recherche/CoLiSHyMEaux/draft/",
                  layer="implantation_piezos_v5")
piezos <- st_transform(piezos[order(piezos$Nom),],4326)
piezos$LON <- st_coordinates(piezos)[,1]
piezos$LAT <- st_coordinates(piezos)[,2]

for(i in seq_len(nrow(piezos)))
{
  thing <- piezos[i,]
  thing_info <- list(
    name = thing$Nom,
    description = sprintf("Piézomètre %s, profondeur %d m. Horizon capté : %s",
                          thingProfondeur,thing$Strati),
    Locations = list(list(
      name = thing$Nom,
      description = sprintf("Piézomètre %s, profondeur %d m. Horizon capté : %s",
                            thingProfondeur,thing$Strati),
      encodingType = "application/geo+json",
      location = list(
        name = thing$Nom,
        type = "Feature",
        geometry = list(
          type = "Point",
          coordinates = c(thingLAT)
        )
      )
    ))
  )
  
  # Attention si on veut positionner les things avec une précision suffisante,
  # il faut écrire 6 décimales au moins aux coordonnées géographiques
  json_body <- jsonlite::toJSON(thing_info, auto_unbox = TRUE, digits = 6)
  resp_things <- POST(paste0(url,"Things"), body = json_body, encode = "raw",add_headers(`X-Auth` = token))
}
```
Je conserve l'historique daté de l'ensemble des requêtes que j'ai envoyées au service (POST, PATCH ou DELETE), comme cela je peux tracer l'ensemble des modifications successives (déplacement de la position d'un futur capteur après une discussion avec quelqu'un, etc.). Le gros plus est aussi la possibilité d'enrichir la description des things par ajout de photos :
```
hing_info <- list(
  properties = list(
    Height = 60,
    image = list("https://geosas.fr/metadata/colishymeaux/img/Roulecrotte_RD514_1.JPG",
                 "https://geosas.fr/metadata/colishymeaux/img/Roulecrotte_RD514_2.JPG",
                 "https://geosas.fr/metadata/colishymeaux/img/entree_buse_RD514.JPG")
  )
)
json_body <- jsonlite::toJSON(thing_info, auto_unbox = TRUE)
PATCH(paste0(url,"Things(2)"), body = json_body, encode = "raw",add_headers(`X-Auth` = token))
```
