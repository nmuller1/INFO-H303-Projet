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
   phoneNum  VARCHAR(20) NOT NULL,
   road    VARCHAR(255) NOT NULL,
   roadNum    VARCHAR(255) NOT NULL,
   codePostal    VARCHAR(255) NOT NULL,
   commune    VARCHAR(255) NOT NULL
);

CREATE TABLE mechanic(
   id    DECIMAL PRIMARY KEY ,
   firstname VARCHAR(20) NOT NULL,
   lastname  VARCHAR(20) NOT NULL,
   password    VARCHAR(64) NOT NULL,
   phoneNum  VARCHAR(20) NOT NULL,
   road    VARCHAR(255) NOT NULL,
   roadNum    VARCHAR(255) NOT NULL,
   codePostal    VARCHAR(255) NOT NULL,
   commune    VARCHAR(255) NOT NULL,
   hireDate    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL
);

CREATE TABLE reloads(
   scooter    INT NOT NULL,
   user_id      INT NOT NULL,
   initialLoad  INT check( initialLoad between 0 and 4 ),
   finalLoad    INT check( finalLoad between 0 and 4 ),
   sourceX  DECIMAL NOT NULL,
   sourceY DECIMAL NOT NULL,
   destinationX DECIMAL NOT NULL,
   destinationy DECIMAL NOT NULL,
   startTime VARCHAR(64) NOT NULL,
   endTime VARCHAR(64) NOT NULL
);

CREATE TABLE reparations(
   scooter INT NOT NULL, 
   userID  INT NOT NULL, 
   mechanic DECIMAL NOT NULL, 
   complainTime VARCHAR(64) NOT NULL, 
   repaireTime VARCHAR(64) NOT NULL,
   commentaire TEXT
);

CREATE TABLE scooters(
   numero   INT PRIMARY KEY,
   miseEnService  VARCHAR(64) NOT NULL,
   modele  VARCHAR(64) NOT NULL,
   plainte  BOOLEAN NOT NULL,
   charge   INT check( charge between 0 and 4 )
);

CREATE TABLE trips(
   scooter INT NOT NULL, 
   userID  INT NOT NULL,
   sourceX  DECIMAL NOT NULL,
   sourceY DECIMAL NOT NULL,
   destinationX DECIMAL NOT NULL,
   destinationy DECIMAL NOT NULL,
   startTime VARCHAR(64) NOT NULL,
   endTime VARCHAR(64) NOT NULL
);