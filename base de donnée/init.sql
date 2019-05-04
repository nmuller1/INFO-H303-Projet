set timezone='UTC';

CREATE TABLE  user_ (
   id          INT PRIMARY KEY ,
   pseudo      VARCHAR(20) ,
   password    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL  UNIQUE
);

CREATE TABLE  CHARGER_USER  (
   id        INT PRIMARY KEY REFERENCES user_(id) ON DELETE CASCADE,
   lastname  VARCHAR(20) NOT NULL,
   firstname VARCHAR(20) NOT NULL,
   password    VARCHAR(64) NOT NULL,
   phoneNum  VARCHAR(20) NOT NULL,
   road    VARCHAR(255) NOT NULL,
   roadNum    VARCHAR(255) NOT NULL,
   codePostal    VARCHAR(255) NOT NULL,
   commune    VARCHAR(255) NOT NULL,
   hireDate    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL
);

CREATE TABLE mechanic(
   id int PRIMARY KEY ,
   firstname VARCHAR(20) NOT NULL,
   lastname  VARCHAR(20) NOT NULL,
   phoneNum  VARCHAR(20) NOT NULL,
   road    VARCHAR(255) NOT NULL,
   roadNum    VARCHAR(255) NOT NULL,
   codePostal    VARCHAR(255) NOT NULL,
   commune    VARCHAR(255) NOT NULL
);

ALTER TABLE mechanic ALTER COLUMN id TYPE BIGINT;