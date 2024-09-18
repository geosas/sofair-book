# Retrour d'expérience de l'ORE Agrhys
- [1. Qui parle](#qui_parle)    
- [2. Introduction](#intro)
- [3. Configurer une instance STEAN](#conf)  
  - [3.1. Fichier de configuration](#fichier_conf)
  - [3.2. Comment ce fichier de configuration fonctionne-t-il?](#fonc_conf)

<a id="top"></a>
<a id="qui_parle"></a>
## 1. Qui parle ?
Christophe Geneste, ingénieur d'étude INRAE, administrateur de plateformes, d'applications web et de bases de données à l'UMR SAS.

<a id="intro"></a>
## 2. Introduction
Appliquer le modèle de données Sensorthings à un observatoire, tel que l'ORE Agrhys, n'est pas trivial au premier abord.  
Comment restrancrire la réalité de terrain vers Sensorthings?   
![du terrain au service SensorThings](img/terrain_vers_ST_v2.png)

Sachant que:  
*  Je ne suis pas spécialiste en base de données
*  L'utilisation de l'API SensorThings m'est difficile
*  La compréhension du modèle de données SensorThings n'est pas aisée  

```{important}
Pour lever ces verrous, ce travail nécessite 3 compétences. Vous les posséder, alors vous êtes autonomes!
```

![3 competences](img/trois_competences.png)

[Revenir en haut](#top) 
<a id="conf"></a>
## 3. Configurer une instance STEAN  
[STEAN](https://github.com/Mario-35/STEAN) est une implémentation de l'API SensorThings. [Pour en savoir plus](https://sensorthings.geosas.fr/)  

La première difficulté est de déterminer les [Things](https://geosas.fr/sofair-book/page/chap-sensorthings/things.html) et Features of Interest. Que doivent-ils représenter? Ici, le/la scientifique intervient majoritairement.
la seconde étape est la définition de Sensors et Observed Properties. La/le scientifique travaillent de concert avec le personnl de terrain essentiellemnt.

Dans le cas de l'ORE Agrhys:
* le point de mesure est attribué aux entités [Things](https://geosas.fr/sofair-book/page/chap-sensorthings/things.html)  
Exemple: le point de mesure E30 correspond à l'éxutoire du bassin versant du Puits dont les coordonnées géographiques sont [-4.1208244,47.9441891]
* Sensors = capteur ou analyseur
* Observed properties = grandeur physique mesurée ou analysée.

<a id="fichier_conf"></a>
### 3.1. Fichier de configuration
Maintenant que les [Things](https://geosas.fr/sofair-book/page/chap-sensorthings/things.html), les Features of Interest, les Sensors et les Observed Properties sont définis, comment configurer une instances STEAN? C'est ici que le Data Scientist commence à intervenir. Il doit fournir les outils et les formalismes pour accompganger le scientifique et le personnel de terrain dans l'intégration de leurs données vers le modèle de données SensorThings.  

Dans la cas d'un observatoires, nous avons produit un fichier tableur dit de configuration. Les informations collectées au travers de ce fichier sont traitées par un script Python permettant de configuer une instance STEAN. L'alimentation en données sera effectuée ultérieurement.

<a id="fonc_conf"></a>
### 3.2. Comment ce fichier de configuration fonctionne-t-il?  
Il est composé d'un onglet d'information et de 5 onglets correspondant aux entités du modèle de données Sensorthings. 
* Lisez-moi: guide l'utilisateur dans la saisie: Les données attendues 
* 1_observedProperty
* 2_sensor
* 3_thing
* 4_datastream
* 5_featureOfInterest

Les 5 onglets (en rouge) seront par la suite interprétés par un script Python pour configurer une instance STEAN.

ILe fichier de configuration contient une macro VBA effectuant des controles de saisies et produit automatiquement la liste des datastreams.

**Instruction génrales**  

1- Renseigner les onglets 1_observedProperty, 2_sensor, 3 _thing, 5_featureOfInterest, puis actualiser les données dans l'onglet 4_datastream.  
2- Adapter les noms des datastreams si nécessaire. Ils doivent être uniques. Attention: Une action sur le bouton Actualiser effacera vos modifications  

* Le séparateur décimal le point.  
* Ne modifier pas la structure des onglets en rouge. Si présence de doublons dans la colonne name , les cellules passent en rouge.  
* Ne pas utliser les caractères _ et -. Ces caractères seront automatiquement supprimés des colonnes name.  
* Vérifier les menus déroulants des onglets 2_sensor (colonnes observedPropertyn), 3_thing (colonnes sensorn ) et 4_datastream (colonne featureOfInterest ).  
* Eviter de laisser des lignes vides.  
* Le nom des colonnes en fond blanc sont standards et ne doivent pas être modifiés.  
* Les colonnes grisées correspondent aux propriétés de chaque entité. Elles sont personnalisables.  
* Données obligatoires repérées par une * et en rouge.

  

