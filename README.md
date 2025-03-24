# python-project
ce projet sera à propos d'une application de gestion de contact en Python qui permettra d'ajouter des contacts avec nom,email et numéro de téléphone avec l'option de recherche et le filtrage de contact par catégorie. Ce projet sera réalisé par Othmane Chougrad et Aya Allaoui
# contexte et définition du problème
la gestion des contacts est essentielle pour une bonne organisation personnelle et professionnelle. Cependant,les utilisateurs perdent leurs contacts en raison d’un mal stockage de donnée non sécurisé ou d’un manque de fonctionnalités de recherche et de filtrage, d'où ce projet donnera solution à ces problèmes. Il y a possibilité de :

-l’ajout, la modification et la suppression de contacts (nom, email, numéro de téléphone).
-une authentification par numéro de téléphone et mot de passe.
-la recherche d’un contact par son numéro.
-le filtrage des contacts par catégorie (domicile, professionnel, mobile).
-un stockage sécurisé dans une base de données pour éviter les pertes de données.

# objectif 

-gestion optimale des données
-présenter un nouveau prototype logiciel efficace
-répondre au besoin clients
# scope 

-target : particulier / professionnel
-plateforme : application web  

# stakeholders
- client ( utilisateur final ) : utilisation de l'application
- développeurs : gestion du développement
- administrateur : gestion de BDD
# besoins fonctionnels 

*Authentification* 

Objectif : Permettre à l’utilisateur de se connecter de manière sécurisée.
Description : L’utilisateur doit pouvoir s’authentifier avec son numéro de téléphone et un mot de passe.
Contraintes : Validation du format du numéro de téléphone et mdp.
Priorité : Haute.

*Ajout d’un nouveau contact*

Objectif : Permettre à l’utilisateur d’enregistrer un nouveau contact.
Description : L’utilisateur doit pouvoir ajouter un contact avec un nom, un email, un numéro de téléphone et une catégorie (domicile, professionnel, mobile).
Contraintes : Vérification du format de l’email et du numéro de téléphone.
Priorité : Haute.

*Modification d’un contact*

Objectif : Permettre à l’utilisateur de mettre à jour les informations d’un contact.
Description : L’utilisateur doit pouvoir modifier le nom, l’email, le numéro ou la catégorie d’un contact déjà enregistré.
Contraintes : Vérification des nouvelles données avant enregistrement.
Priorité : Moyenne.

*Suppression d’un contact*

Objectif : Permettre à l’utilisateur de supprimer un contact.
Description : L’utilisateur doit pouvoir supprimer un contact, avec une confirmation avant l’action pour éviter les erreurs.
Contraintes : Demande de confirmation avant suppression.
Priorité : Moyenne.

*Recherche d’un contact par numéro*

Objectif : Permettre à l’utilisateur de retrouver rapidement un contact.
Description : L’utilisateur doit pouvoir rechercher un contact en saisissant son numéro de téléphone.
Contraintes : Résultats affichés en moins de 2 secondes.
Priorité : Haute.

*Filtrage des contacts par catégorie*

Objectif : Permettre à l’utilisateur d’organiser ses contacts.
Description : L’utilisateur doit pouvoir filtrer les contacts selon leur catégorie (domicile, professionnel, mobile).
Contraintes : Interface clair pour la sélection des catégories.
Priorité : Moyenne

*Stockage des contacts*

Objectif : Éviter toute perte de données.
Description : Tous les contacts doivent être sauvegardés dans une base de données (sqlite3)
Contraintes : Sauvegarde sécurisée et robuste.
Priorité : Haute.

# besoins non fonctionnels

*Performance*
L’application doit répondre rapidement, avec un temps de chargement inférieur à 2 secondes pour les opérations de recherche et d’affichage

*Sécurité*
Protection contre les injections SQL en intégrant dans la BDD

*Fiabilité*
Aucune perte de donnée

*UI intuitive*
Interface graphique clair et amical

*Maintenable*
Code bien organisé
