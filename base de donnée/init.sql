set timezone='UTC';

CREATE TABLE  user_ (
   id          INT PRIMARY KEY ,
   pseudo      VARCHAR(20) ,
   password    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL  UNIQUE
);

CREATE TABLE  CHARGER_USER  (
   id        INT PRIMARY KEY REFERENCES user_(id) ON DELETE CASCADE,
   firstname VARCHAR(20) NOT NULL,
   lastname  VARCHAR(20) NOT NULL,
   phoneNum  VARCHAR(20) NOT NULL,
   road    VARCHAR(255) NOT NULL,
   roadNum    VARCHAR(255) NOT NULL,
   codePostal    VARCHAR(255) NOT NULL,
   commune    VARCHAR(255) NOT NULL
);

SELECT * FROM user_;
SELECT * FROM charger_user;