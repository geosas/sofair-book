## Alimenter en observations
Les méthodes d'alimentation en données d'un modèle de données Sensorthings dépendent de plusieurs facteurs.  
* La solution technique d'API utilisée, Frost, STEAN, etc...
* Alimentation d'une mesure seule à intervale régulier ou non.
* Importation d'une série temporelle entière.
* Du nombre de points à injecter, 10,  100000, ou plus.
* Des possibilités techniques de l'API, importation en masse via des fichhiers.

### Quelques exemples  
Vous pouvez consulter les retours d'expériences pour plus de détails de mise en oeuvre.  

**Importation de données historiques ou par campagne annuelle de mise en ligne de données**  
Dans ce cas, prenons l'exemple d'importation de données via des fichiers textes au format CSV.

Les étapes:  
* Obtention des fichiers CSV dans un formalisme quelconque.
* Mise en forme des fichiers de données selon un formalisme acceptée par l'API.
* Importation des données selon la solution technique:  
    * Frost: par script Python, découpage du fichier de données, créer d'une trame au format Json à envoyer au service, rebouclage selon le nombre de découpage.
    * STEAN: par script Python, importation des fichiers CSV au bon formalisme un par un.

