CREATE DATABASE IF NOT EXISTS dbstime;
use dbstime;

/***********************
*       CREATE         *
***********************/

create table ABONNEMENT (
     Type varchar(255) not null,
     Prix int not null,
     constraint IDABONNEMENT primary key (Type));

create table PANIER (
     PanierId int not null,
     Montant float not null,
     constraint IDACHAT primary key (PanierId));

create table ADRESSE (
     AdresseId int not null,
     Numero varchar(255) not null,
     Rue varchar(255) not null,
     Ville varchar(255) not null,
     CodePostal int not null,
     Pays varchar(255) not null,
     constraint IDADRESSE primary key (AdresseId));

create table AVIS (
     Date date not null,
     Note int not null,
     Commentaire varchar(255) not null,
     constraint IDAVIS primary key (Date, Note, Commentaire)); 

create table CATEGORIE_JEU (
     Nom varchar(255) not null,
     Description varchar(255) not null,
     constraint IDCATEGORIE_JEU primary key (Nom));

create table achat (
     MontantTotal float not null,
     DateAchat date not null);

create table MOYEN_PAIEMENT (
     MoyenPaiementId int not null,
     Nom varchar(255) not null,
     taxeDuMoyen int not null,
     constraint IDMOYEN_PAIEMENT primary key (MoyenPaiementId));

create table ENTREPRISE (
     NumSiret int not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     AdresseWeb char(255) not null,
     constraint IDENTREPRISE primary key (NumSiret));

create table IMAGE_JEU (
     URL_image varchar(255) not null,
     Alt varchar(255) not null,
     constraint IDIMAGE_JEU primary key (URL_image));

create table JEU (
     GameId int not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     DateDeSortie date not null,
     Prix float not null,
     EstDLC BOOLEAN default FALSE not null,
     GamePass BOOLEAN not null,
     constraint IDJEUX primary key (GameId));

create table LANGUE_JEU (
     Langue varchar(255) not null,
     Raccourci varchar(255) not null,
     constraint IDLANGUE primary key (Langue));

create table OBJET (
     ObjetId int not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     constraint IDOBJET primary key (ObjetId));

create table OBJET_INSTANCE (
     ID int not null,
     DateObtention date not null,
     constraint IDOBJET_INSTANCE primary key (ID));

create table SOLDE (
     SoldeId char(255) not null,
     TauxSolde int not null,
     DateDebutSolde date not null,
     DateFinSolde date not null,
     constraint IDSOLDE primary key (SoldeId));

create table TRANSACTION (
     TransactionId int not null,
     DateMiseEnVente date not null,
     DateVente date not null,
     PrixVente int not null,
     constraint IDMARCHE primary key (TransactionId));

create table UTILISATEUR (
     UserId varchar(255) not null,
     Username varchar(255) not null,
     Prenom varchar(255) not null,
     Nom varchar(255) not null,
     Email varchar(255) not null,
     MDP varchar(255) not null,
     DateInscription date not null,
     DateNaissance date not null,
     Portefeuille float not null,
     constraint IDUTILISATEUR primary key (UserId));


/***********************
*       TRIGGER        *
***********************/


/***********************
*        VIEW          *
***********************/


/***********************
*       INSERT         *
***********************/

INSERT INTO ABONNEMENT (Type, Prix) VALUES ('Basique', 0);
INSERT INTO ABONNEMENT (Type, Prix) VALUES ('Premium', 4.99);
INSERT INTO ABONNEMENT (Type, Prix) VALUES ('Ultimate', 6.99);

INSERT INTO CATEGORIE_JEU (Nom, Description) VALUES ('Action', 'Jeux avec des éléments d''action et de combat');
INSERT INTO CATEGORIE_JEU (Nom, Description) VALUES ('Aventure', 'Jeux d''aventure avec des énigmes et des quêtes');
INSERT INTO CATEGORIE_JEU (Nom, Description) VALUES ('Stratégie', 'Jeux de stratégie et de gestion de ressources');
INSERT INTO CATEGORIE_JEU (Nom, Description) VALUES ('Sport', 'Jeux de sport comme le football, le basket-ball, etc.');
INSERT INTO CATEGORIE_JEU (Nom, Description) VALUES ('Course', 'Jeux de course de voitures, de motos, etc.');
INSERT INTO CATEGORIE_JEU (Nom, Description) VALUES ('RPG', 'Jeux de rôle avec des personnages et des quêtes');

INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (987654312, 'Stime', 'Stime est une plateforme de distribution de contenu vidéo ludique en ligne', 'https://www.stime.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (123456789, 'UbiRoft', 'Description de l''entreprise UbiRoft', 'https://www.ubiroft.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (987654321, 'EpicJeux', 'Description de l''entreprise EpicJeux', 'https://www.epicjeux.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (456789123, 'Activisum', 'Description de l''entreprise Activisum', 'https://www.activisum.com');
INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb) VALUES (496789124, 'Ae', 'Description de l''entreprise Ae', 'https://www.ae.com');

INSERT INTO IMAGE_JEU (URL_image, Alt) VALUES ('https://example.com/image1.jpg', 'Image du jeu 1');
INSERT INTO IMAGE_JEU (URL_image, Alt) VALUES ('https://example.com/image2.jpg', 'Image du jeu 2');
INSERT INTO IMAGE_JEU (URL_image, Alt) VALUES ('https://example.com/image3.jpg', 'Image du jeu 3');
INSERT INTO IMAGE_JEU (URL_image, Alt) VALUES ('https://example.com/image4.jpg', 'Image du jeu 4');
INSERT INTO IMAGE_JEU (URL_image, Alt) VALUES ('https://example.com/image5.jpg', 'Image du jeu 5');
INSERT INTO IMAGE_JEU (URL_image, Alt) VALUES ('https://example.com/image6.jpg', 'Image du jeu 6');

INSERT INTO JEU (GameId, Nom, Description, DateDeSortie, Prix, EstDLC, GamePass) VALUES (1, 'Jeu1', 'Description du jeu1', '2022-01-01', 59.99, FALSE, TRUE);
INSERT INTO JEU (GameId, Nom, Description, DateDeSortie, Prix, EstDLC, GamePass) VALUES (2, 'DLCJeu1', 'Description du dlc du jeu2', '2022-02-01', 29.99, TRUE, TRUE);
INSERT INTO JEU (GameId, Nom, Description, DateDeSortie, Prix, EstDLC, GamePass) VALUES (3, 'Jeu3', 'Description du jeu3', '2022-03-01', 39.99, FALSE, TRUE);
INSERT INTO JEU (GameId, Nom, Description, DateDeSortie, Prix, EstDLC, GamePass) VALUES (4, 'Jeu4', 'Description du jeu4', '2022-03-01', 59.99, FALSE, FALSE);

INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Français', 'FR');
INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Anglais', 'EN');
INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Espagnol', 'ES');
INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Allemand', 'DE');


INSERT INTO OBJET (ObjetId, Nom, Description) VALUES (1, 'Objet1', 'Description de l''objet1');
INSERT INTO OBJET (ObjetId, Nom, Description) VALUES (2, 'Objet2', 'Description de l''objet2');
INSERT INTO OBJET (ObjetId, Nom, Description) VALUES (3, 'Objet3', 'Description de l''objet3');
INSERT INTO OBJET (ObjetId, Nom, Description) VALUES (4, 'Objet4', 'Description de l''objet4');
INSERT INTO OBJET (ObjetId, Nom, Description) VALUES (5, 'Objet5', 'Description de l''objet5');



