DROP DATABASE IF EXISTS dbstime;
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
     PanierId int not null AUTO_INCREMENT,
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
     Role int default 1 not null,
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
     Prix float not null,
     constraint ID_OBJET primary key (ObjetId),
     constraint FK_JEU_OBJET foreign key (Jeu) references JEU (GameId)
);


create table OBJET_INSTANCE (
     Id int not null AUTO_INCREMENT,
     DateObtention date,
     Possesseur int,
     Objet int not null,
     Panier int,
     constraint ID_OBJET_INSTANCE primary key (ID),
     constraint FK_POSSESSEUR foreign key (Possesseur) references UTILISATEUR (UserId),
     constraint FK_PANIER_OBJET foreign key (Panier) references PANIER (PanierId),
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

create table PANIER_OBJET_INSTANCE(
     Panier int not null,
     Objet int not null,
     constraint ID_PANIER_OBJET primary key (Panier, Objet),
     constraint FK_PANIER_ foreign key (Panier) references PANIER (PanierId),
     constraint FK_JEU_PANIER_OBJET foreign key (Objet) references OBJET_INSTANCE (Id)
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
*        VIEW          *
***********************/

CREATE VIEW USERS_PASSWORDS AS
    SELECT UserId, Username, MDP
    FROM UTILISATEUR;

CREATE VIEW vue_entreprise_jeux AS
    SELECT E.Nom, E.Description, E.AdresseWeb, G.Nom as NomJeu
    FROM ENTREPRISE E
    JOIN JEU G ON G.Developpeur = E.NumSiret AND G.Editeur = E.NumSiret;

CREATE VIEW vue_jeux_langues AS
    SELECT J.GameId, J.Nom, J.Description, J.DateDeSortie, J.Prix, J.GamePass, J.Developpeur, J.Editeur, L.Langue
    FROM JEU J
    JOIN JEU_LANGUE_TEXTE JLT ON J.GameId = JLT.Jeu
    JOIN LANGUE L ON JLT.Langue = L.Langue;

CREATE VIEW vue_jeux_categories AS
    SELECT J.GameId, J.Nom, J.Description, J.DateDeSortie, J.Prix, J.GamePass, J.Developpeur, J.Editeur, C.Nom AS Categorie
    FROM JEU J
    JOIN CATEGORIE_JEU CJ ON J.GameId = CJ.Jeu
    JOIN CATEGORIE C ON CJ.Categorie = C.Nom;

CREATE VIEW CA_VENTE AS
SELECT * FROM (
    SELECT SUM(MontantTotal) AS MontantAnnuel, YEAR(DateAchat) as Annee
    FROM ACHAT
    GROUP BY YEAR(DateAchat)
) AS v
ORDER BY v.Annee DESC;

CREATE VIEW CA_VENTE_MENSUEL AS
SELECT * FROM (
    SELECT SUM(MontantTotal) AS MontantMensuel, YEAR(DateAchat) as Annee, MONTH(DateAchat) as Mois
    FROM ACHAT
    GROUP BY MONTH(DateAchat), YEAR(DateAchat)
) AS v
ORDER BY v.Annee DESC, v.Mois DESC;


/***********************
*        ROLE          *
***********************/

CREATE ROLE 'OPERATEUR', 'ADMIN', 'ENTREPRISE', 'COMPTABILITE', 'UTILISATEUR', 'NON_CONNECTE';

GRANT TRIGGER ON dbstime.* TO 'OPERATEUR';
GRANT TRIGGER ON dbstime.* TO 'ADMIN';
GRANT TRIGGER ON dbstime.* TO 'ENTREPRISE';
GRANT TRIGGER ON dbstime.* TO 'COMPTABILITE';
GRANT TRIGGER ON dbstime.* TO 'UTILISATEUR';
GRANT TRIGGER ON dbstime.* TO 'NON_CONNECTE';

GRANT ALL PRIVILEGES ON *.* TO 'OPERATEUR' WITH GRANT OPTION;

GRANT SELECT, INSERT, UPDATE, DELETE ON dbstime.* TO 'ADMIN';

GRANT SELECT, INSERT, UPDATE, DELETE ON dbstime.JEU TO 'ENTREPRISE';
GRANT SELECT, UPDATE ON dbstime.ENTREPRISE to 'ENTREPRISE';
GRANT SELECT ON dbstime.UTILISATEUR to 'ENTREPRISE';

GRANT SELECT ON dbstime.CA_VENTE to 'COMPTABILITE';
GRANT SELECT ON dbstime.CA_VENTE_MENSUEL to 'COMPTABILITE';
GRANT SELECT ON dbstime.UTILISATEUR to 'COMPTABILITE';

GRANT SELECT ON dbstime.ABONNEMENT to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE, DELETE ON dbstime.PANIER to 'UTILISATEUR';
GRANT SELECT ON dbstime.CATEGORIE to 'UTILISATEUR';
GRANT SELECT ON dbstime.LANGUE to 'UTILISATEUR';
GRANT SELECT ON dbstime.MOYEN_PAIEMENT to 'UTILISATEUR';
GRANT SELECT ON dbstime.CATEGORIE to 'UTILISATEUR';
GRANT SELECT ON dbstime.SOLDE to 'UTILISATEUR';
GRANT SELECT ON dbstime.CATEGORIE to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE, DELETE ON dbstime.ADRESSE to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.UTILISATEUR to 'UTILISATEUR';
GRANT SELECT ON dbstime.ENTREPRISE to 'UTILISATEUR';
GRANT SELECT ON dbstime.ENTREPRISE_ADRESSE to 'UTILISATEUR';
GRANT SELECT ON dbstime.JEU to 'UTILISATEUR';
GRANT SELECT ON dbstime.OBJET to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.OBJET_INSTANCE to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.TRANSACTION to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.CATEGORIE to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.UTILISATEUR_ABONNEMENT to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.UTILISATEUR_JEU to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE, DELETE ON dbstime.PANIER_JEU to 'UTILISATEUR';
GRANT SELECT ON dbstime.JEU_LANGUE_TEXTE to 'UTILISATEUR';
GRANT SELECT ON dbstime.JEU_LANGUE_AUDIO to 'UTILISATEUR';
GRANT SELECT ON dbstime.IMAGE_JEU to 'UTILISATEUR';
GRANT SELECT ON dbstime.CATEGORIE_JEU to 'UTILISATEUR';
GRANT SELECT, INSERT ON dbstime.AVIS to 'UTILISATEUR';
GRANT SELECT, INSERT ON dbstime.EVALUATION to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE ON dbstime.ACHAT to 'UTILISATEUR';
GRANT SELECT, INSERT, UPDATE, DELETE ON dbstime.PANIER_OBJET_INSTANCE to 'UTILISATEUR';
GRANT SELECT ON vue_entreprise_jeux to 'UTILISATEUR';
GRANT SELECT ON vue_jeux_langues to 'UTILISATEUR';
GRANT SELECT ON vue_jeux_categories to 'UTILISATEUR';

GRANT SELECT ON dbstime.USERS_PASSWORDS to 'NON_CONNECTE';
GRANT INSERT ON dbstime.UTILISATEUR to 'NON_CONNECTE';
GRANT INSERT ON dbstime.PANIER to 'NON_CONNECTE';
GRANT CREATE USER ON *.* to 'NON_CONNECTE';


-- DO NOT CHANGE PASSWORDS ! --

CREATE USER 'op01'@'%' IDENTIFIED BY 'pa55w0rd';
GRANT 'OPERATEUR' TO 'op01';

CREATE USER 'admin01'@'%' IDENTIFIED BY 'pa55w0rd';
GRANT 'ADMIN' TO 'admin01';

CREATE USER 'entreprise01'@'%' IDENTIFIED BY 'pa55w0rd';
CREATE USER 'entreprise02'@'%' IDENTIFIED BY 'pa55w0rd';
CREATE USER 'entreprise03'@'%' IDENTIFIED BY 'pa55w0rd';
GRANT 'ENTREPRISE' TO 'entreprise01';
GRANT 'ENTREPRISE' TO 'entreprise02';
GRANT 'ENTREPRISE' TO 'entreprise03';

CREATE USER 'compta01'@'%' IDENTIFIED BY 'pa55w0rd';
GRANT 'COMPTABILITE' TO 'compta01';

CREATE USER 'nobody'@'%' IDENTIFIED BY 'no_password';
GRANT 'NON_CONNECTE' TO 'nobody';
