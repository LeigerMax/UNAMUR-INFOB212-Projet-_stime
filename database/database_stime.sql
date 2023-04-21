CREATE DATABASE IF NOT EXISTS dbstime;
use dbstime;

create table ABONNEMENT (
     Type char(1) not null,
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
     GamePass char not null,
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


INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Français', 'FR');
INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Anglais', 'EN');
INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Espagnol', 'ES');
INSERT INTO LANGUE_JEU (Langue, Raccourci) VALUES ('Allemand', 'DE');
