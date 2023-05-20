START TRANSACTION;


/***********************
*       INSERT         *
***********************/

INSERT INTO ABONNEMENT (Type, Prix) VALUES ('Basique', 0);
INSERT INTO ABONNEMENT (Type, Prix) VALUES ('Premium', 4.99);
INSERT INTO ABONNEMENT (Type, Prix) VALUES ('Ultimate', 6.99);

INSERT INTO CATEGORIE (Nom, Description) VALUES ('Action', 'Jeux avec des éléments d''action et de combat');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('Aventure', 'Jeux d''aventure avec des énigmes et des quêtes');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('Stratégie', 'Jeux de stratégie et de gestion de ressources');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('Sport', 'Jeux de sport comme le football, le basket-ball, etc.');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('Course', 'Jeux de course de voitures, de motos, etc.');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('RPG', 'Jeux de rôle avec des personnages et des quêtes');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('MMORPG', 'Jeux de rôle en ligne avec des personnages et des quêtes');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('Survie', 'Jeux de survie, construire, trouver des vivres');
INSERT INTO CATEGORIE (Nom, Description) VALUES ('Combat', 'Jeux de combat, battez vous contre vos amis ou une IA');

INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (987654312, 'Volve', 'Volve est une entreprise de jeu vidéo, connue pour Half-Death', 'https://www.volve.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (123456789, 'UbiRoft', 'Entreprise responsable des succès tel que Assassins Cream', 'https://www.ubiroft.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (987654321, 'EpicJeux', 'On a créé FortKnife', 'https://www.epicjeux.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (456789123, 'Activisum', 'Donnez votre argent, payez nos DLC, nos BattlePass', 'https://www.activisum.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (496789124, 'Ae', 'Its in our game', 'https://www.ae.com');

INSERT INTO SOLDE(TauxSolde, DateDebutSolde, DateFinSolde) VALUES (50, "2023/05/19", "2023/06/30");
INSERT INTO SOLDE(TauxSolde, DateDebutSolde, DateFinSolde) VALUES (1, "2023/05/19", "2023/06/30");

INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Grand Theft Auto: Petty Theft Automatic', 'Un jeu daction épique rempli de rebondissements et de défis passionnants.', '2021-09-17', 49.99, FALSE, '123456789', '123456789', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Call of Booty: Skirmish in Skivvies', 'Une expérience de tir intense avec des combats en sous-vêtements et des batailles palpitantes.', '2022-07-08', 59.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('World of Warcrap: Universe of War Crap', 'Plongez dans un univers fantastique rempli de guerres absurdes et de personnages décalés.', '2020-03-22', 39.99, FALSE, '496789124', '496789124', 1, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Super Smash Brossard: Brawl of Veggies', 'Affrontez vos amis avec des personnages végétariens dans des combats délirants et explosifs.', '2019-11-12', 44.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('The Legend of Zoldo: The Legend of the Doofus', 'Partez à laventure avec un héros maladroit et découvrez un monde rempli de mystères et de quêtes épiques.', '2018-06-30', 29.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Minecrash: Build, Survive, and Avoid Bugs', 'Un jeu de construction et de survie où vous devez éviter les bugs qui menacent votre monde.', '2023-01-05', 39.99, FALSE, '987654321', '987654321', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Assassins Cream: Cream of the Assassin', 'Incarnez un assassin culinaire et préparez les desserts les plus mortels dans ce jeu daction gourmand.', '2017-08-21', 19.99, FALSE, '123456789', '123456789', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Street Fighter II Turbo: Sidewalk Boxer III Super', 'Affrontez les meilleurs combattants de rue dans des duels explosifs et des séquences de combat intenses.', '2016-04-02', 24.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Fallout 76 Dollars: Atomic Failure', 'Explorez un monde post-apocalyptique rempli de bugs et de déceptions dans cette expérience de jeu désastreuse.', '2018-11-14', 59.99, FALSE, '987654312', '987654312', 2, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Pokémon Go: Gollum Snatch!', 'Partez à la chasse aux Pokémon dans le monde réel et capturez-les pour devenir le meilleur dresseur.', '2016-07-06', 0, TRUE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Call of Booty: Battle Pass Season 19', 'Des Skins, des Cosmétiques pour être le guerrier le plus choupi sur le champ de bataille !', '2022-08-08', 19.99, FALSE, '456789123', '456789123', NULL, TRUE, 2);


INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/GTA7.jpg', 'GTA : Petty Theft Automatic Gameplay Screenshot',1);
INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/COD.jpg', 'COD Battle Pass Season 19 Image',2);
INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/WOW.jpg', 'Nouvelle Extension WOW: Flush The Toilet',3);
INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/SMB.jpg', 'Nouveau Personnage : Brussel Sprout',4);

INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Français', 'FR');
INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Anglais', 'EN');
INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Espagnol', 'ES');
INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Allemand', 'DE');


INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (1, 'Action');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (1, 'Course');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (2, 'Action');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (2, 'Stratégie');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (3, 'MMORPG');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (3, 'Aventure');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (4, 'Action');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (4, 'Sport');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (5, 'Aventure');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (5, 'RPG');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (6, 'Survie');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (6, 'Aventure');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (7, 'Action');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (7, 'Aventure');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (8, 'Combat');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (9, 'MMORPG');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (9, 'Aventure');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (9, 'Action');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (10, 'Aventure');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (10, 'RPG');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (11, 'Action');
INSERT INTO CATEGORIE_JEU(Jeu, Categorie) VALUES (11, 'Stratégie');

INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 1);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 2);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Français', 2);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Allemand', 2);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Espagnol', 2);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 3);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Français', 3);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 4);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 5);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Français', 6);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 7);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Français', 7);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Espagnol', 7);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 8);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 9);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Français', 9);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 10);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Anglais' , 11);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Français', 11);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Allemand', 11);
INSERT INTO JEU_LANGUE_AUDIO(Langue, Jeu) VALUES ('Espagnol', 11);

INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,1);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',1);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',1);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',1);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,2);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',2);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',2);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',2);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,3);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',3);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',3);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',3);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,4);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',4);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',4);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',4);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,5);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',5);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',5);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',5);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,6);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',6);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',6);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',6);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,7);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',7);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',7);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',7);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,8);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',8);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',8);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',8);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,9);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',9);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',9);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',9);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,10);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',10);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',10);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',10);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Anglais' ,11);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Français',11);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Espagnol',11);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ('Allemand',11);



INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Couteau en or massif 50K', 'Un beau couteau virtuel qui coute énormement d"argent bien réel',2);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('T-Shirt "My Homies Hate SQL3"', 'On déteste tous ça',1);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Graffiti "69, Nice"', 'Le fameux funny number',1);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Le burn-out de Maxime', 'Il en a marre',4);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Les examens de juin', 'Le pouvoir le plus redoutable pour vaincre les étudiants',3);

INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("12", "Rue de la babouche", "Andenne", 5300, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("69", "Rue du Funny Number", "Marrant", 6969, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("3", "Rue du Cheval de Troie", "Blagounette", 3300, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("42", "Avenue de la Sagesse", "Sérénité", 1234, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("7", "Chemin des Étoiles", "Constellation", 5678, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("13", "Place du Rire", "Bonheur", 9876, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("18", "Boulevard de la Fantaisie", "Joyeux", 2468, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("9", "Allée des Farces", "Rigolade", 1357, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("23", "Rue de la Plaisanterie", "Amusant", 8642, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("77", "Avenue de la Comédie", "Drôle", 3141, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("55", "Chemin du Sourire", "Enjoué", 2718, "Belgique");
INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES ("21", "Place des Jeux de Mots", "Amusement", 5050, "Belgique");


INSERT INTO PANIER (PanierId, Montant) VALUES (1, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (2, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (3, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (4, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (5, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (6, 0);

INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("InkMonster", "Lucas", "Pastori", "test@test.com", "b98f9643a856719a5944672f84cf13da694a1576c11fb9f3d57b7b71c9588981", "2022-03-01", "2000-06-06", 1); -- mdp: wéwéwé
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier, Portefeuille) VALUES ("test", "test", "test", "test@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "2000-04-02", 2, 100); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("max", "max", "max", "max@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "2000-04-02", 3); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("BenAOrdure", "Benjamin", "Pans", "ben@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "2000-11-29", 4); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("PtitLouis", "Louis", "Cavrenne", "louis@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "1999-07-28", 5); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("MomoRiche", "Mohamed", "Ait Hassou", "momo@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "1987-09-11", 6); -- mdp: test

-- special users
INSERT INTO PANIER (PanierId, Montant) VALUES (7, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (8, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (9, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (10, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (11, 0);
INSERT INTO PANIER (PanierId, Montant) VALUES (12, 0);
INSERT INTO UTILISATEUR (Panier, Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Role) VALUES (7, "op01", "Op01", "STIME", "op01@stime.com", "8d977c9751464efc6c731130f8b5a52918e249fbe004a1f54dbe06fc4d98656e", "2022-03-01", "2000-06-06", 5); -- mdp: pa55w0rd
INSERT INTO UTILISATEUR (Panier, Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Role) VALUES (8, "admin01", "Admin01", "STIME", "admin01@stime.com", "8d977c9751464efc6c731130f8b5a52918e249fbe004a1f54dbe06fc4d98656e", "2022-03-01", "2000-06-06", 4); -- mdp: pa55w0rd
INSERT INTO UTILISATEUR (Panier, Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Role) VALUES (9, "entreprise01", "Stime", "STIME", "stime@stime.com", "8d977c9751464efc6c731130f8b5a52918e249fbe004a1f54dbe06fc4d98656e", "2022-03-01", "2000-06-06", 3); -- mdp: pa55w0rd
INSERT INTO UTILISATEUR (Panier, Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Role) VALUES (10, "entreprise02", "EpicJeu", "STIME", "stime@epicjeu.com", "8d977c9751464efc6c731130f8b5a52918e249fbe004a1f54dbe06fc4d98656e", "2022-03-01", "2000-06-06", 3); -- mdp: pa55w0rd
INSERT INTO UTILISATEUR (Panier, Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Role) VALUES (11, "entreprise03", "Ae", "STIME", "stime@ae.com", "8d977c9751464efc6c731130f8b5a52918e249fbe004a1f54dbe06fc4d98656e", "2022-03-01", "2000-06-06", 3); -- mdp: pa55w0rd
INSERT INTO UTILISATEUR (Panier, Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Role) VALUES (12, "compta01", "Compta01", "STIME", "compta01@stime.com", "8d977c9751464efc6c731130f8b5a52918e249fbe004a1f54dbe06fc4d98656e", "2022-03-01", "2000-06-06", 2); -- mdp: pa55w0rd


INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (1,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (2,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (3,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (4,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (5,'Premium', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (6,'Ultimate', "2022-03-01", 30);

INSERT INTO OBJET_INSTANCE (DateObtention, Possesseur, Objet) VALUES ('2022-06-06', 1 , 1);
INSERT INTO OBJET_INSTANCE (DateObtention, Possesseur, Objet) VALUES ('2022-06-06', 1 , 2);
INSERT INTO OBJET_INSTANCE (DateObtention, Possesseur, Objet) VALUES ('2022-06-06', 1 , 3);
INSERT INTO OBJET_INSTANCE (DateObtention, Possesseur, Objet) VALUES ('2022-06-06', 2 , 3);
INSERT INTO OBJET_INSTANCE (DateObtention, Possesseur, Objet) VALUES ('2022-06-06', 2 , 4);


INSERT INTO TRANSACTION (DateMiseEnVente, PrixVente, Revendeur, Objet) VALUES ("2022-05-06", 10, 1, 1);
INSERT INTO TRANSACTION (DateMiseEnVente, PrixVente, Revendeur, Objet) VALUES ("2022-05-06", 20, 1, 2);
INSERT INTO TRANSACTION (DateMiseEnVente, PrixVente, Revendeur, Objet) VALUES ("2022-05-06", 30, 1, 3);


INSERT INTO UTILISATEUR_JEU (Utilisateur, Jeu, GamePass) VALUES (2,1, FALSE);
INSERT INTO UTILISATEUR_JEU (Utilisateur, Jeu, GamePass) VALUES (2,2, FALSE);
INSERT INTO UTILISATEUR_JEU (Utilisateur, Jeu, GamePass) VALUES (2,3, FALSE);


INSERT INTO MOYEN_PAIEMENT(Nom,TaxeDuMoyen) VALUES ("Wallet", 0);
INSERT INTO MOYEN_PAIEMENT(Nom,TaxeDuMoyen) VALUES ("Paypal", 5);
INSERT INTO MOYEN_PAIEMENT(Nom,TaxeDuMoyen) VALUES ("Bank", 10);


INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (99, "2023/11/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (84, "2023/09/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (54, "2022/09/12", 2, 1, 2);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (102, "2022/07/12", 1, 1, 1);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (99, "2016/01/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (84, "2016/02/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (54, "2017/03/12", 2, 1, 2);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (102, "2017/04/12", 1, 1, 1);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (99, "2018/05/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (84, "2018/06/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (54, "2019/07/12", 2, 1, 2);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (102, "2019/08/12", 1, 1, 1);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (99, "2020/09/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (84, "2020/10/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (54, "2021/11/12", 2, 1, 2);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (102, "2021/12/12", 1, 1, 1);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (99, "2022/01/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (84, "2022/02/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (54, "2023/03/12", 2, 1, 2);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (102, "2023/04/12", 1, 1, 1);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (99, "2023/05/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (84, "2023/06/12", 4, 1, 4);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (54, "2023/07/12", 2, 1, 2);
INSERT INTO ACHAT(MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (102, "2023/08/12", 1, 1, 1);

INSERT INTO AVIS(Jeu, Auteur, Date, Note, Commentaire) VALUES (1, 4, "2023/05/20", 9, "J'ai bien aimé le moment ou");
INSERT INTO AVIS(Jeu, Auteur, Date, Note, Commentaire) VALUES (2, 5, "2023/05/20", 2, "J'ai payé tout les battle pass mais je suis pas plus fort que les autres...");
INSERT INTO AVIS(Jeu, Auteur, Date, Note, Commentaire) VALUES (3, 1, "2023/05/20", 10, "Alors pour avoir passé 148 heures a farm le dernier boss, j'ai trop kiffé! Je fais du 143 DPS avec le sort 'Fart'.");

INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (6, 3, 1);
INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (5, 1, 0);
INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (1, 2, 0);
INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (2, 2, 0);
INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (3, 2, 0);
INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (4, 2, 0);
INSERT INTO EVALUATION(Utilisateur, Avis, Approuve) VALUES (6, 2, 0);
