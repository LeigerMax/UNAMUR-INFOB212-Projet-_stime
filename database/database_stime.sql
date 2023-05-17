CREATE DATABASE IF NOT EXISTS dbstime;
use dbstime;

/***********************
*       CREATE         *
***********************/

create table ABONNEMENT (
     Type varchar(255) not null,
     Prix int not null,
     constraint ID_ABONNEMENT primary key (Type)
);

create table PANIER (
     PanierId int not null AUTO_INCREMENT ,
     Montant float not null,
     constraint ID_PANIER primary key (PanierId)
);


create table CATEGORIE (
     Nom varchar(255) not null,
     Description varchar(255) not null,
     constraint ID_CATEGORIE primary key (Nom)
);

create table LANGUE (
     Langue varchar(255) not null,
     Raccourci varchar(255) not null,
     constraint ID_LANGUE primary key (Langue)
);


create table MOYEN_PAIEMENT (
     MoyenPaiementId int not null AUTO_INCREMENT,
     Nom varchar(255) not null,
     TaxeDuMoyen int not null,
     constraint ID_MOYEN_PAIEMENT primary key (MoyenPaiementId)
);

create table SOLDE (
     SoldeId int not null AUTO_INCREMENT,
     TauxSolde int not null,
     DateDebutSolde date not null,
     DateFinSolde date not null,
     constraint ID_SOLDE primary key (SoldeId)
);


create table ADRESSE (
     AdresseId int not null AUTO_INCREMENT,
     Numero varchar(10) not null,
     Rue varchar(255) not null,
     Ville varchar(255) not null,
     CodePostal int not null,
     Pays varchar(255) not null,
     constraint ID_ADRESSE primary key (AdresseId)
);

create table UTILISATEUR (
     UserId int not null AUTO_INCREMENT,
     Username varchar(255) not null,
     Prenom varchar(255) not null,
     Nom varchar(255) not null,
     Email varchar(255) not null,
     MDP varchar(255) not null,
     DateInscription date not null,
     DateNaissance date not null,
     Portefeuille float default 00.00 not null,
     AdresseLivraison int,
     AdresseFacturation int,
     Panier int not null,
     constraint ID_UTILISATEUR primary key (UserId),
     constraint FK_ADRESSE_LIVRAISON foreign key (AdresseLivraison) references ADRESSE (AdresseId),
     constraint FK_ADRESSE_FACTURATION foreign key (AdresseFacturation) references ADRESSE (AdresseId),
     constraint FK_PANIER foreign key (Panier) references PANIER (PanierId)
);


create table ENTREPRISE (
     NumSiret varchar(255) not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     AdresseWeb char(255) not null,
     EstBoiteDev BOOLEAN DEFAULT false not null,
     EstEditeur BOOLEAN DEFAULT false not null,
     constraint IDENTREPRISE primary key (NumSiret)
);

create table ENTREPRISE_ADRESSE (
     Entreprise varchar(255) not null,
     Adresse int not null,
     constraint ID_ENTREPRISE_ADRESSE primary key (Entreprise, Adresse),
     constraint FK_ENTREPRISE foreign key (Entreprise) references ENTREPRISE (NumSiret),
     constraint FK_ADRESSE foreign key (Adresse) references ADRESSE (AdresseId)
);


create table JEU (
     GameId int not null AUTO_INCREMENT,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     DateDeSortie date not null,
     Prix float not null,
     GamePass BOOLEAN DEFAULT false not null,
     Developpeur varchar(255) not null,
     Editeur varchar(255) not null,
     Solde int,
     EstDLC BOOLEAN DEFAULT FALSE not null,
     DLC int,
     constraint ID_JEU primary key (GameId),
     constraint FK_DEVELOPPEUR foreign key (Developpeur) references ENTREPRISE (NumSiret),
     constraint FK_EDITEUR foreign key (Editeur) references ENTREPRISE (NumSiret),
     constraint FK_SOLDE foreign key (Solde) references SOLDE (SoldeId),
     constraint FK_DLC foreign key (DLC) references JEU (GameId)
);

create table OBJET (
     ObjetId int not null AUTO_INCREMENT,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     Jeu int not null,
     constraint ID_OBJET primary key (ObjetId),
     constraint FK_JEU_OBJET foreign key (Jeu) references JEU (GameId)
);

create table OBJET_INSTANCE (
     Id int not null AUTO_INCREMENT,
     DateObtention date not null,
     Possesseur int not null,
     Objet int not null,
     Panier int not null,
     constraint ID_OBJET_INSTANCE primary key (ID),
     constraint FK_POSSESSEUR foreign key (Possesseur) references UTILISATEUR (UserId),
     constraint FK_PANIER_OBJETI foreign key (Panier) references PANIER (PanierId),
     constraint FK_OBJET foreign key (Objet) references OBJET (ObjetId)
);



create table TRANSACTION (
     TransactionId int not null AUTO_INCREMENT,
     DateMiseEnVente date not null,
     DateVente date,
     PrixVente float not null,
     Revendeur int not null,
     Acheteur int,
     Objet int not null,
     constraint ID_TRANSACTION primary key (TransactionId),
     constraint FK_REVENDEUR foreign key (Revendeur) references UTILISATEUR (UserId),
     constraint FK_ACHETEUR foreign key (Acheteur) references UTILISATEUR (UserId),
     constraint FK_OBJET_INSTANCE foreign key (Objet) references OBJET_INSTANCE (Id)
);

create table ACHAT (
     AchatId int not null AUTO_INCREMENT,
     MontantTotal float not null,
     DateAchat date not null,
     Utilisateur int not null,
     MoyenPaiement int not null,
     Panier int not null,
     constraint ID_ACHAT primary key (AchatId),
     constraint FK_UTILISATEUR_ACHAT foreign key (Utilisateur) references UTILISATEUR (UserId),
     constraint FK_MOYEN_PAIEMENT foreign key (MoyenPaiement) references MOYEN_PAIEMENT (MoyenPaiementId),
     constraint FK_PANIER_ACHAT foreign key (Panier) references PANIER (PanierId)
);

create TABLE UTILISATEUR_ABONNEMENT (
    Utilisateur int not null,
    Abonnement varchar(255) not null,
    DateDebut date not null,
    Duree int not null,
    constraint ID_UTILISATEUR_ABONNEMENT primary key (Utilisateur, Abonnement, DateDebut),
    constraint FK_UTILISATEUR_UTIL_ABO foreign key (Utilisateur) references UTILISATEUR (UserId),
    constraint FK_ABONNEMENT foreign key (Abonnement) references ABONNEMENT (Type)
);

create table UTILISATEUR_JEU (
     Utilisateur int not null,
     Jeu int not null,
     GamePass BOOLEAN not null,
     constraint ID_UTILISATEUR_JEU primary key (Utilisateur, Jeu),
     constraint FK_UTILISATEUR_UTIL_JEU foreign key (Utilisateur) references UTILISATEUR (UserId),
     constraint FK_JEU_UTILISATEUR_JEU foreign key (Jeu) references JEU (GameId)
);


create table PANIER_JEU (
     Panier int not null,
     Jeu int not null,
     constraint ID_PANIER_JEU primary key (Panier, Jeu),
     constraint FK_PANIER_PJEU foreign key (Panier) references PANIER (PanierId),
     constraint FK_JEU_PANIER_JEU foreign key (Jeu) references JEU (GameId)
);

create table JEU_LANGUE_TEXTE (
     Langue varchar(255) not null,
     Jeu int not null,
     constraint ID_JEU_LANGUE_TEXTE primary key (Langue, Jeu),
     constraint FK_LANGUE_TEXTE foreign key (Langue) references LANGUE (Langue),
     constraint FK_JEU_LANGUE_TEXTE foreign key (Jeu) references JEU (GameId)
);

create table JEU_LANGUE_AUDIO (
     Langue varchar(255) not null,
     Jeu int not null,
     constraint ID_JEU_LANGUE_TEXTE primary key (Langue, Jeu),
     constraint FK_LANGUE_AUDIO foreign key (Langue) references LANGUE (Langue),
     constraint FK_JEU_LANGUE_AUDIO foreign key (Jeu) references JEU (GameId)
);

create table IMAGE_JEU (
     URL_image varchar(255) not null,
     Alt varchar(255) not null,
     Jeu int not null,
     constraint ID_IMAGE_JEU primary key (URL_image),
     constraint FK_JEU_IMAGE foreign key (Jeu) references JEU (GameId)
);

create table CATEGORIE_JEU (
     Jeu int not null,
     Categorie varchar(255) not null,
     constraint ID_CATEGORIE_JEU primary key (Jeu, Categorie),
     constraint FK_JEU_CATEGORIE foreign key (Jeu) references JEU (GameId),
     constraint FK_CATEGORIE foreign key (Categorie) references CATEGORIE (Nom)
);

create table AVIS (
     AvisId int not null AUTO_INCREMENT,
     Jeu int not null,
     Auteur int not null,
     Date date not null,
     Note int not null,
     Commentaire varchar(255) not null,
     constraint ID_AVIS primary key (AvisId),
     constraint FK_JEU_AVIS foreign key (Jeu) references JEU (GameId),
     constraint FK_AUTEUR foreign key (Auteur) references UTILISATEUR (UserId)
);

create table EVALUATION (
     Utilisateur int not null,
     Avis int not null,
     Approuve BOOLEAN not null,
     constraint ID_EVALUATION primary key (Utilisateur,Avis),
     constraint FK_UTILISATEUR_EVALUATION foreign key (Utilisateur) references UTILISATEUR (UserId),
     constraint FK_AVIS foreign key (Avis) references AVIS (AvisId)
);

/***********************
*       TRIGGER        *
***********************/


/***********************
*        VIEW          *
***********************/
CREATE VIEW vue_entreprise_jeux
     AS SELECT E.Nom, E.Description, E.AdresseWeb, G.Nom as NomJeu
     FROM ENTREPRISE E
     JOIN JEU G ON G.Developpeur = E.NumSiret AND G.Editeur = E.NumSiret;

CREATE VIEW vue_jeux_langues 
AS SELECT J.GameId, J.Nom, J.Description, J.DateDeSortie, J.Prix, J.GamePass, J.Developpeur, J.Editeur, L.Langue
FROM JEU J
JOIN JEU_LANGUE_TEXTE JLT ON J.GameId = JLT.Jeu
JOIN LANGUE L ON JLT.Langue = L.Langue;

CREATE VIEW vue_jeux_categories AS
SELECT J.GameId, J.Nom, J.Description, J.DateDeSortie, J.Prix, J.GamePass, J.Developpeur, J.Editeur, C.Nom AS Categorie
FROM JEU J
JOIN CATEGORIE_JEU CJ ON J.GameId = CJ.Jeu
JOIN CATEGORIE C ON CJ.Categorie = C.Nom;
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

INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (987654312, 'Stime', 'Stime est une plateforme de distribution de contenu vidéo ludique en ligne', 'https://www.stime.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (123456789, 'UbiRoft', 'Description de l''entreprise UbiRoft', 'https://www.ubiroft.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (987654321, 'EpicJeux', 'Description de l''entreprise EpicJeux', 'https://www.epicjeux.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (456789123, 'Activisum', 'Description de l''entreprise Activisum', 'https://www.activisum.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (496789124, 'Ae', 'Description de l''entreprise Ae', 'https://www.ae.com');

INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Jeu1', 'Description du jeu1', '2022-01-01', 59.99, FALSE,'987654312','987654312',null,FALSE, null );
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('DLCJeu1', 'Description du dlc du jeu2', '2022-02-01', 29.99, TRUE, '987654312','987654312',null,TRUE, 1);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Jeu3', 'Description du jeu3', '2022-03-01', 39.99, FALSE, '987654312','987654312',null,FALSE, null);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Jeu4', 'Description du jeu4', '2022-03-01', 59.99, FALSE, '987654312','987654312',null,FALSE, null);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Super Aventure', 'Un jeu d action épique rempli de rebondissements et de défis passionnants.', '2022-04-15', 49.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Course Folle', 'Plongez dans l univers de la vitesse avec ce jeu de course palpitant.', '2022-05-20', 29.99, FALSE, '987654321', '987654321', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('RPG Magique', 'Explorez un monde fantastique et devenez le héros dans ce jeu de rôle captivant.', '2022-06-10', 39.99, FALSE, '987654321', '987654321', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Stratégie Totale', 'Testez vos compétences tactiques dans ce jeu de stratégie complexe et engageant.', '2022-07-05', 59.99, FALSE, '496789124', '496789124', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Grand Theft Auto: Petty Theft Automatic', 'Un jeu daction épique rempli de rebondissements et de défis passionnants.', '2021-09-17', 49.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Call of Booty: Skirmish in Skivvies', 'Une expérience de tir intense avec des combats en sous-vêtements et des batailles palpitantes.', '2022-07-08', 59.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('World of Warcrap: Universe of War Crap', 'Plongez dans un univers fantastique rempli de guerres absurdes et de personnages décalés.', '2020-03-22', 39.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Super Smash Brossard: Brawl of Veggies', 'Affrontez vos amis avec des personnages végétariens dans des combats délirants et explosifs.', '2019-11-12', 44.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('The Legend of Zoldo: The Legend of the Doofus', 'Partez à laventure avec un héros maladroit et découvrez un monde rempli de mystères et de quêtes épiques.', '2018-06-30', 29.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Minecrash: Build, Survive, and Avoid Bugs', 'Un jeu de construction et de survie où vous devez éviter les bugs qui menacent votre monde.', '2023-01-05', 39.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Assassins Cream: Cream of the Assassin', 'Incarnez un assassin culinaire et préparez les desserts les plus mortels dans ce jeu daction gourmand.', '2017-08-21', 19.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Street Fighter II Turbo: Sidewalk Boxer III Super', 'Affrontez les meilleurs combattants de rue dans des duels explosifs et des séquences de combat intenses.', '2016-04-02', 24.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Fallout 76 Dollars: Atomic Failure', 'Explorez un monde post-apocalyptique rempli de bugs et de déceptions dans cette expérience de jeu désastreuse.', '2018-11-14', 59.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Mario Kart: Tractor Leap', 'Prenez le volant de tracteurs personnalisables et défiez vos amis dans des courses déjantées et pleines de rebondissements.', '2020-08-27', 49.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('The Witcher 3: Witch Hunter 3 - The Great Cleanup', 'Incarnez un chasseur de sorcières dans une quête épique pour nettoyer le monde des forces maléfiques.', '2015-05-19', 39.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Final Fantasy: The Ultimate Delusion', 'Plongez dans un univers fantastique rempli de personnages excentriques et dhistoires captivantes dans ce jeu de rôle épique.', '2019-07-09', 59.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Metal Gear Salad: Stealthy Salad', 'Incarnez un chef cuisinier ninja et préparez des salades secrètes dans ce jeu dinfiltration culinaire.', '2017-02-28', 29.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('The Sims: The Fools', 'Créez votre monde virtuel et faites jouer des tours à vos Sims dans cette simulation de vie délirante.', '2022-10-11', 39.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Dark Souls: Black Souls', 'Affrontez des ennemis redoutables et relevez des défis sombres et impitoyables dans ce jeu de rôle hardcore.', '2011-09-22', 29.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('BioShock: Algae Shock', 'Explorez une ville sous-marine infestée dalgues mutantes et découvrez les mystères qui sy cachent.', '2007-08-21', 19.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Halo: Cosmic Hoop', 'Entraînez-vous pour devenir un guerrier intergalactique et participez à des combats intenses dans cet univers futuriste.', '2020-12-08', 59.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Pokémon Go: Gollum Snatch!', 'Partez à la chasse aux Pokémon dans le monde réel et capturez-les pour devenir le meilleur dresseur.', '2016-07-06', 0, TRUE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('Red Dead Redemption: Dead Cow Reward', 'Explorez lOuest sauvage et affrontez les hors-la-loi pour obtenir des récompenses alléchantes dans ce jeu daction captivant.', '2018-10-26', 59.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);
INSERT INTO JEU (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES ('The Elder Scrolls: The Ancient Scrolls', 'Plongez dans un monde fantastique rempli de magie et de quêtes épiques dans cette aventure légendaire.', '2021-03-23', 49.99, FALSE, '456789123', '456789123', NULL, FALSE, NULL);

INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/image1.jpg', 'Image du jeu 1',1);
INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/image2.jpg', 'Image du jeu 2',2);
INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/image3.jpg', 'Image du jeu 3',3);
INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES ('https://example.com/image4.jpg', 'Image du jeu 4',4);

INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Français', 'FR');
INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Anglais', 'EN');
INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Espagnol', 'ES');
INSERT INTO LANGUE (Langue, Raccourci) VALUES ('Allemand', 'DE');

INSERT INTO JEU_LANGUE_AUDIO (Langue, Jeu) VALUES ('Français', 1);
INSERT INTO JEU_LANGUE_AUDIO (Langue, Jeu) VALUES ('Anglais', 1); 


INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ("Français", 1);
INSERT INTO JEU_LANGUE_TEXTE(Langue, Jeu) VALUES ("Anglais", 1);


INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Objet1', 'Description de l''objet1',1);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Objet2', 'Description de l''objet2',1);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Objet3', 'Description de l''objet3',1);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Objet4', 'Description de l''objet4',1);
INSERT INTO OBJET (Nom, Description, Jeu) VALUES ('Objet5', 'Description de l''objet5',1);

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


INSERT INTO PANIER (Montant) VALUES (0);
INSERT INTO PANIER (Montant) VALUES (0);
INSERT INTO PANIER (Montant) VALUES (0);
INSERT INTO PANIER (Montant) VALUES (0);
INSERT INTO PANIER (Montant) VALUES (0);
INSERT INTO PANIER (Montant) VALUES (0);

INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("InkMonster", "Lucas", "Pastori", "test@test.com", "b98f9643a856719a5944672f84cf13da694a1576c11fb9f3d57b7b71c9588981", "2022-03-01", "2000-06-06",1); -- mdp: wéwéwé
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("test", "test", "test", "test@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "2000-04-02",2); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("max", "max", "max", "max@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "2000-04-02",3); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("BenAOrdure", "Benjamin", "Pans", "ben@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "2000-11-29",4); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("PtitLouis", "Louis", "Cavrenne", "louis@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "1999-07-28",5); -- mdp: test
INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Panier) VALUES ("MomoRiche", "Mohamed", "Ait Hassou", "momo@test.be", "1ab261b6ccd26fffd2781bd0d9dfdc5a95443bea35d7e2889a41fdf2b6cfe53b", "2022-03-01", "1987-09-11",6); -- mdp: test

INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (1,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (2,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (3,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (4,'Basique', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (5,'Premium', "2022-03-01", 30);
INSERT INTO UTILISATEUR_ABONNEMENT (Utilisateur, Abonnement, DateDebut, Duree) VALUES (6,'Ultimate', "2022-03-01", 30);

INSERT INTO UTILISATEUR_JEU (Utilisateur, Jeu, GamePass) VALUES (2,1, FALSE);
INSERT INTO UTILISATEUR_JEU (Utilisateur, Jeu, GamePass) VALUES (2,2, FALSE);
INSERT INTO UTILISATEUR_JEU (Utilisateur, Jeu, GamePass) VALUES (2,3, FALSE);


INSERT INTO MOYEN_PAIEMENT(Nom,TaxeDuMoyen) VALUES ("Wallet", 0);
INSERT INTO MOYEN_PAIEMENT(Nom,TaxeDuMoyen) VALUES ("Paypal", 5);
INSERT INTO MOYEN_PAIEMENT(Nom,TaxeDuMoyen) VALUES ("Bank", 10);

