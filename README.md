Projet 8 - Purbeurre

# Présentation

Ce projet est un exercice de formation Python.

Le but de ce projet est de développer un site web permettant a quiconque de trouver un substitut plus sain à un aliment de sa consommation habituelle. Le site est déployé à l'adresse suivante : https://healthy-food-project.herokuapp.com/

Le site utilise des produits de l'API Openfoodfacts (https://fr.openfoodfacts.org/) et certaines informations peuvent être manquantes.

# Fonctionnement
La base de données (postgresql) étant limitée à 10.000 lignes sur l'hébergement sur heroku, le site ne permet pas d'intéragir avec la totalité des produits de l'API Openfoodfacts.
Les produits inclus dans le projets sont donc récupérés dans les catégories suivantes : 
-pates a tartiner au chocolat
-chocolats noirs aux feves de cacao
-pizzas a la bolognaise
-liegeois
-yaourts aromatises
-steaks de boeuf
-cereales au chocolat
-legumineuses-en-conserve
-speculoos
-chips-de-pommes-de-terre

Lorsque vous effectuez une recherche de produit, le serveur va chercher dans quelle(s) catégorie(s) se trouve(nt) l'aliment recherché, puis vous affiche, sur la page de résultats, les six produits les plus sains en terme de nutriscore pour chaque catégorie correspondante trouvée.
Vous pouvez cliquer sur le nom d'un produit pour accéder à une page qui affiche les repères nutritionnels pour 100g, le nutriscore et le lien de la page produit sur le site d'Openfoodfacts pour encore plus d'informations.

Sur la page de résultats, en dessous de chaque produit, vous avez la possibilité de sauvegardé des aliments dans vos favoris, que vous pouvez retrouver dans l'onget avec l'icone de carrotte, si vous êtes connecté.

# Utilisation

Pour effectuer une recherche, entrez le nom d'un aliment dans le formulaire central si vous êtes sur la page d'accueil, ou celui dans la navbar si vous êtes ailleurs, cela vous mènera à la page de résultats.

La seule condition d'utilisation concerne la fonctionnalité d'enregistrement de produits en favoris, qui requiert d'être authentifié, et donc la création d'un compte.

# Installation

Si vous êtes simple utilisateur, vous pouvez vous rendre sur le site du projet à l'adresse suivante : https://healthy-food-project.herokuapp.com/

Si vous êtes curieux et que vous voulez essayer le projet chez vous, suivez ces instructions : 
