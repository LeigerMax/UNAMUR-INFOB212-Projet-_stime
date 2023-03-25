CREATE DATABASE IF NOT EXISTS dbstime;
use dbstime;

CREATE TABLE user(
    userid int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    PRIMARY KEY (userid)
);

INSERT INTO user(FirstName, Surname)
VALUES("John", "Andersen"), ("Emma", "Smith");  