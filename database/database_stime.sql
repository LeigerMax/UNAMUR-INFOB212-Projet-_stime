CREATE DATABASE IF NOT EXISTS dbstime;
use dbstime;

CREATE TABLE user(
    userid int not null AUTO_INCREMENT,
    Username varchar(100) NOT NULL,
    Password varchar(256) NOT NULL,
    FirstName varchar(100) NOT NULL,
    LastName varchar(100) NOT NULL,
    BirthDate DATE NOT NULL,
    DateInscription DATETIME NOT NULL,
    PRIMARY KEY (userid)
);

INSERT INTO user(Username, Password, FirstName, LastName, BirthDate, DateInscription)
VALUES("john_a", "password", "John", "Andersen", "2000-01-01", NOW()),
      ("emma_e", "password", "Emma", "Smith", "1998-02-03", NOW());
