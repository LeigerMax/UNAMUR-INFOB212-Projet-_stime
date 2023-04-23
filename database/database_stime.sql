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

create TABLE UTILISATEUR_ABONNEMENT (
    Utilisateur int not null,
    Abonnement varchar(255) not null,
    DateDebut date not null,
    Duree int not null,
    constraint ID_UTILISATEUR_ABONNEMENT primary key (Utilisateur, Abonnement, DateDebut),
    constraint FK_UTILISATEUR foreign key (Utilisateur) references UTILISATEUR (UserId),
    constraint FK_ABONNEMENT foreign key (Abonnement) references ABONNEMENT (Type)
);

create table PANIER (
     PanierId int not null,
     Montant float not null,
     constraint ID_PANIER primary key (PanierId)
);

create table PANIER_JEU (
     Panier int not null,
     Jeu int not null,
     constraint ID_PANIER_JEU primary key (Panier, Jeu),
     constraint FK_PANIER foreign key (Panier) references PANIER (PanierId),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId)
);

create table ADRESSE (
     AdresseId int not null,
     Numero varchar(10) not null,
     Rue varchar(255) not null,
     Ville varchar(255) not null,
     CodePostal int not null,
     Pays varchar(255) not null,
     constraint ID_ADRESSE primary key (AdresseId)
);

create table AVIS (
     AvisId int not null,
     Jeu int not null,
     Auteur int not null,
     Date date not null,
     Note int not null,
     Commentaire varchar(255) not null,
     constraint ID_AVIS primary key (AvisId),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId),
     constraint FK_AUTEUR foreign key (Auteur) references UTILISATEUR (UserId)
);

create table EVALUATION (
     Utilisateur int not null,
     Avis int not null,
     Approuve BOOLEAN not null,
     constraint ID_EVALUATION primary key (Utilisateur, Abonnement, DateDebut),
     constraint FK_UTILISATEUR foreign key (Utilisateur) references UTILISATEUR (UserId),
     constraint FK_AVIS foreign key (Avis) references AVIS (AvisId)
)

create table CATEGORIE (
     Nom varchar(255) not null,
     Description varchar(255) not null,
     constraint ID_CATEGORIE primary key (Nom)
);

create table CATEGORIE_JEU (
     Jeu int not null,
     Categorie varchar(255) not null,
     constraint ID_CATEGORIE_JEU primary key (Jeu, Categorie),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId),
     constraint FK_CATEGORIE foreign key (Categorie) references CATEGORIE (Nom),
);

create table ACHAT (
     AchatId int not null,
     MontantTotal float not null,
     DateAchat date not null,
     Utilisateur int not null,
     MoyenPaiement int not null,
     Panier int not null,
     constraint ID_ACHAT primary key (AchatId),
     constraint FK_UTILISATEUR foreign key (Utilisateur) references UTILISATEUR (UserId),
     constraint FK_MOYEN_PAIEMENT foreign key (MoyenPaiement) references MOYEN_PAIEMENT (MoyenPaiementId),
     constraint FK_PANIER foreign key (Panier) references PANIER (PanierId)
);

create table MOYEN_PAIEMENT (
     MoyenPaiementId int not null,
     Nom varchar(255) not null,
     taxeDuMoyen int not null,
     constraint ID_MOYEN_PAIEMENT primary key (MoyenPaiementId)
);

create table ENTREPRISE (
     NumSiret varchar(255) not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     AdresseWeb char(255) not null,
     EstBoiteDev BOOLEAN not null,
     EstEditeur BOOLEAN not null,
     constraint IDENTREPRISE primary key (NumSiret)
);

create table ENTREPRISE_ADRESSE (
     Entreprise varchar(255) not null,
     Adresse int not null,
     constraint ID_ENTREPRISE_ADRESSE primary key (Entreprise, Adresse),
     constraint FK_ENTREPRISE foreign key (Entreprise) references ENTREPRISE (NumSiret),
     constraint FK_ADRESSE foreign key (Adresse) references ADRESSE (AdresseId)
);

create table IMAGE_JEU (
     URL_image varchar(255) not null,
     Alt varchar(255) not null,
     Jeu int not null,
     constraint ID_IMAGE_JEU primary key (URL_image),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId)
);

create table JEU (
     GameId int not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     DateDeSortie date not null,
     Prix float not null,
     GamePass BOOLEAN default false not null,
     Developpeur varchar(255) not null,
     Editeur varchar(255) not null,
     Solde int not null,
     EstDLC BOOLEAN default FALSE not null,
     DLC int not null,
     constraint ID_JEU primary key (GameId),
     constraint FK_DEVELOPPEUR foreign key (Developpeur) references (ENTREPRISE) NumSiret,
     constraint FK_EDITEUR foreign key (Editeur) references (ENTREPRISE) NumSiret,
     constraint FK_SOLDE foreign key (Solde) references (SOLDE) SoldeId,
     constraint FK_DLC foreign key (DLC) references (JEU) GameId
);

create table LANGUE (
     Langue varchar(255) not null,
     Raccourci varchar(255) not null,
     constraint ID_LANGUE primary key (Langue)
);

create table JEU_LANGUE_TEXTE (
     Langue varchar(255) not null,
     Jeu int not null,
     constraint ID_JEU_LANGUE_TEXTE primary key (Langue, Jeu),
     constraint FK_LANGUE foreign key (Langue) references LANGUE (Langue),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId)
);

create table JEU_LANGUE_AUDIO (
     Langue varchar(255) not null,
     Jeu int not null,
     constraint ID_JEU_LANGUE_TEXTE primary key (Langue, Jeu),
     constraint FK_LANGUE foreign key (Langue) references LANGUE (Langue),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId)
);

create table OBJET (
     ObjetId int not null,
     Nom varchar(255) not null,
     Description varchar(255) not null,
     Jeu int not null,
     constraint ID_OBJET primary key (ObjetId),
     constraint FK_JEU foreign key (Jeu) references (JEU) GameId
);

create table OBJET_INSTANCE (
     Id int not null,
     DateObtention date not null,
     Possesseur int not null,
     Objet int not null,
     Panier int not null,
     constraint ID_OBJET_INSTANCE primary key (ID),
     constraint FK_POSSESSEUR foreign key (Possesseur) references (UTILISATEUR) UserId,
     constraint FK_PANIER foreign key (Panier) references (PANIER) PanierId,
     constraint FK_OBJET foreign key (Objet) references (OBJET) ObjetId
);

create table SOLDE (
     SoldeId int not null,
     TauxSolde int not null,
     DateDebutSolde date not null,
     DateFinSolde date not null,
     constraint ID_SOLDE primary key (SoldeId)
);

create table TRANSACTION (
     TransactionId int not null,
     DateMiseEnVente date not null,
     DateVente date not null,
     PrixVente float not null,
     Revendeur int not null,
     Acheteur int,
     Objet int not null,
     constraint ID_TRANSACTION primary key (TransactionId),
     constraint FK_REVENDEUR foreign key (Revendeur) references (UTILISATEUR) UserId,
     constraint FK_ACHETEUR foreign key (Acheteur) references (UTILISATEUR) UserId,
     constraint FK_OBJET foreign key (Objet) references (OBJET_INSTANCE) Id
);

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
     AdresseLivraison int not null,
     AdresseFacturation int not null,
     constraint ID_UTILISATEUR primary key (UserId),
     constraint FK_ADRESSE_LIVRAISON foreign key (AdresseLivraison) references ADRESSE (AdresseId),
     constraint FK_ADRESSE_FACTURATION foreign key (AdresseFacturation) references ADRESSE (AdresseId)
);

create table UTILISATEUR_JEU (
     Utilisateur int not null,
     Jeu int not null,
     GamePass BOOLEAN not null,
     constraint ID_UTILISATEUR_JEU primary key (Utilisateur, Jeu),
     constraint FK_UTILISATEUR foreign key (Utilisateur) references UTILISATEUR (UserId),
     constraint FK_JEU foreign key (Jeu) references JEU (GameId)
);


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



