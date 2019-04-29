set timezone='UTC';

CREATE TABLE  user (
   id          INT PRIMARY KEY ,
   pseudo      VARCHAR(20) ,
   password    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL  UNIQUE,
);

CREATE TABLE  CHARGER_USER  (
   id        INT PRIMARY KEY REFERENCES user(id) ON DELETE CASCADE,
   firstname VARCHAR(20) NOT NULL,
   lastname  VARCHAR(20) NOT NULL,
   adress    VARCHAR(255) NOT NULL,
   phoneNum  VARCHAR(20) NOT NULL,
);