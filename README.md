Projet 8 - Purbeurre

# Présentation

Ce projet est un exercice de formation Python.

Le but de ce projet est de développer un site web permettant a quiconque de trouver un substitut plus sain à un aliment de sa consommation habituelle. Le site est déployé à l'adresse suivante : https://healthy-food-project.herokuapp.com/

Le site utilise des produits de l'API Openfoodfacts (https://fr.openfoodfacts.org/) et certaines informations peuvent être manquantes.

# Fonctionnement
La base de données (postgresql) étant limitée à 10.000 lignes sur l'hébergement sur heroku, le site ne permet pas d'intéragir avec la totalité des produits de l'API Openfoodfacts.
Les produits inclus dans le projets sont donc récupérés dans les catégories suivantes :

-pates a tartiner aux noisettes et au cacao

-pizzas au chorizo

-liegeois

-yaourts nature

-steaks de boeuf

-escalopes de poulet

-corn flakes

-haricot verts

-biscuits sablés

-chips a l'ancienne

-prefous

Lorsque vous effectuez une recherche de produit, le serveur va chercher dans quelles catégories se trouvent l'aliment recherché, votre recherche peut concerner plusieurs catégories ,puis vous affiche sur la page de résultats les six produits les plus sains en terme de nutriscore pour chaque catégorie correspondante trouvée.

Vous pouvez cliquer sur un produit pour accéder à sa page, qui affiche les repères nutritionnels pour 100g, le nutriscore et le lien de la page produit sur le site d'Openfoodfacts pour encore plus d'informations.

Sur la page de résultats, en dessous de chaque produit, vous avez la possibilité de sauvegarder des aliments dans vos favoris, que vous pouvez retrouver dans l'onget avec l'icone de carrotte, si vous êtes connecté.

# Utilisation

Pour effectuer une recherche, entrez le nom d'un aliment dans le formulaire central si vous êtes sur la page d'accueil, ou celui dans la navbar si vous êtes ailleurs, cela vous mènera à la page de résultats.

La seule condition d'utilisation concerne la fonctionnalité d'enregistrement de produits en favoris, qui requiert d'être authentifié.

# Installation

Si vous êtes simple utilisateur, vous pouvez vous rendre sur le site du projet à l'adresse suivante : https://healthy-food-project.herokuapp.com/

Si vous voulez installer le projet chez vous, il vous faut python (version 3.6.5):

https://www.python.org/downloads/

Une fois installé, forkez ce repo dans votre espace github (bouton fork en haut à droite), puis clonez le sur votre machine à l'aide du bouton vert "Clone".

Maintenant, le projet est sur votre ordinateur, vous devez installer les dépendances pour le faire fonctionner.
Pour cela, il vous faut un gestionnaire de paquets, tel que pip : https://pip.pypa.io/en/stable/installing/

Ouvrez un terminal si ce n'est pas déjà fait et rendez-vous dans votre dossier d'installation, à l'endroit où se trouve le fichier "requirements.txt".
Une fois au bon endroit, lancez la commande :
```pip install -r requirements.txt```
Cela installe les dépendances dont le projet a besoin pour fonctionner.

Vous devez également créer votre base de données postgresql ou en utiliser une existante.

Pour faire connecter le projet avec votre base, vous devez créer un fichier nommé .env à la racine du projet, et y inclure les variables suivantes :
```
SECRET_KEY = '<votre SECRET KEY>'
ENV = 'development'
DB_USER = '<utilisateur de votre base de données>'
DB_PASSWORD = '<mot de passe utilisateur>'
DB_HOST = '<Adresse de l'hôte>'
DB_PORT= '<Port de votre base de données>'
```
Ainsi, les settings remplaceront les valeurs aux bons endroits.

Maintenant, vous devez créer les tables de la base de données avant de la remplir :
Lancez les commandes :

```python manage.py makemigrations```

```python manage.py migrate```

Il ne vous reste maintenant plus qu'à remplir la base de données, et lancer le serveur pour utiliser le projet en local.
Pour remplir la base de données, assurez-vous d'être à l'endroit où se trouve le fichier manage.py (normalement au même endroit que requirements.txt) et lancez la commande :

```python manage.py initdb off_urls.txt```

Cela va donc remplir la base de données avec les catégories que contient le fichier off_urls.txt. Vous pouvez évidemment le modifier à volonté. Avec les catégories actuelles, il y a en tout autour de 5000 produits, et le remplissage prend environ 1.30min.

Une fois terminé,vous n'avez plus qu'à lancer le serveur django :
```python manage.py runserver```

Vous pouvez désormais utiliser le projet en local, généralement à l'adresse ```127.0.0.1:8000```

Une dernière chose, le projet contient des tests, pour les lancer, utilisez la commande ```python manage.py test```

Sachez par contre qu'il y a un test selenium, qui est effectué sur chrome, donc vous devez installer le chrome driver de votre version de chrome pour que ce test soit fonctionnel. Vous pouvez télécharger le ChromeDriver via ce lien : https://chromedriver.chromium.org/downloads,
et placer l'executable dans ```purbeurre\tests\functionnal```
