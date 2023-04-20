CREATE DATABASE IF NOT EXISTS dbstime;
use dbstime;

create table ABONNEMENT (
     Type char(1) not null,
     Prix int not null,
     constraint IDABONNEMENT primary key (Type));

create table PANIER (
     PanierId int not null,
     Montant float(1) not null,
     constraint IDACHAT primary key (PanierId));

create table ADRESSE (
     AdresseId int not null,
     Numéro varchar(1) not null,
     Rue varchar(1) not null,
     Ville varchar(1) not null,
     CodePostal int not null,
     Pays varchar(1) not null,
     constraint IDADRESSE primary key (AdresseId));

create table AVIS (
     Date date not null,
     Note int not null,
     Commentaire varchar(1) not null,
     constraint IDAVIS primary key (Date, , ));

create table BOITE DEV (
);

create table CATEGORIE_JEU (
     Nom varchar(1) not null,
     Description varchar(1) not null,
     constraint IDCATEGORIE_JEU primary key (Nom));

create table EDITEUR (
);

create table achat (
     MontantTotal float(1) not null,
     DateAchat date not null);

create table MOYEN_PAIEMENT (
     MoyenPaiementId int not null,
     Nom varchar(1) not null,
     taxeDuMoyen int not null,
     constraint IDMOYEN_PAIEMENT primary key (MoyenPaiementId));

create table ENTREPRISE (
     NumSiret int not null,
     Nom varchar(1) not null,
     Description varchar(1) not null,
     AdresseWeb char(1) not null,
     constraint IDENTREPRISE primary key (NumSiret));

create table IMAGE_JEU (
     URL_image varchar(1) not null,
     Alt varchar(1) not null,
     constraint IDIMAGE_JEU primary key (URL_image));

create table JEU (
     GameId int not null,
     Nom varchar(1) not null,
     Description varchar(1) not null,
     DateDeSortie date not null,
     Prix float(1) not null,
     EstDLC char default 'False' not null,
     GamePass char not null,
     constraint IDJEUX primary key (GameId));

create table LANGUE_JEU (
     Langue varchar(1) not null,
     Raccourci varchar(1) not null,
     constraint IDLANGUE primary key (Langue));

create table OBJET (
     ObjetId int not null,
     Nom varchar(1) not null,
     Description varchar(1) not null,
     constraint IDOBJET primary key (ObjetId));

create table OBJET_INSTANCE (
     ID int not null,
     DateObtention date not null,
     constraint IDOBJET_INSTANCE primary key (ID));

create table SOLDE (
     SoldeId char(1) not null,
     TauxSolde int not null,
     DateDebutSolde date not null,
     DateFinSolde date not null,
     constraint IDSOLDE primary key (SoldeId));

create table TRANSACTION (
     TransactionId int not null,
     DateMiseEnVente date not null,
     DateVente [0-1] date not null,
     PrixVente int not null,
     constraint IDMARCHE primary key (TransactionId));

create table UTILISATEUR (
     UserId varchar(1) not null,
     Username varchar(1) not null,
     Prénom varchar(1) not null,
     Nom varchar(1) not null,
     Email varchar(1) not null,
     MDP varchar(1) not null,
     DateInscription date not null,
     DateNaissance date not null,
     Portefeuille float(1) not null,
     constraint IDUTILISATEUR primary key (UserId));
