set timezone='UTC';

CREATE TABLE  nUser (
   id          INT PRIMARY KEY ,
   pseudo      VARCHAR(20) ,
   password    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL  UNIQUE
);

CREATE TABLE  CHARGER_USER  (
   id        INT PRIMARY KEY REFERENCES nUser(id) ON DELETE CASCADE,
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

CREATE TABLE scooters(
   numero   INT PRIMARY KEY,
   miseEnService  VARCHAR(64) NOT NULL,
   modele  VARCHAR(64) NOT NULL,
   plainte  BOOLEAN NOT NULL,
   charge   INT check( charge between 0 and 4 )
);

CREATE TABLE reloads(
   scooter    INT NOT NULL REFERENCES scooters(numero),
   user_id      INT NOT NULL REFERENCES nUser(id),
   initialLoad  INT check( initialLoad between 0 and 4 ),
   finalLoad    INT check( finalLoad between 0 and 4 ),
   sourceX  DECIMAL NOT NULL,
   sourceY DECIMAL NOT NULL,
   destinationX DECIMAL NOT NULL,
   destinationY DECIMAL NOT NULL,
   startTime Timestamp NOT NULL,
   endTime Timestamp
);

CREATE TABLE reparations(
   scooter INT NOT NULL REFERENCES scooters(numero), 
   userID  INT NOT NULL REFERENCES nUser(id),
   mechanic DECIMAL, 
   complainTime Timestamp NOT NULL, 
   repaireTime Timestamp,
   commentaire TEXT
);

CREATE TABLE trips(
   scooter INT NOT NULL REFERENCES scooters(numero),
   userID  INT NOT NULL REFERENCES nUser(id),
   sourceX  DECIMAL NOT NULL,
   sourceY DECIMAL NOT NULL,
   destinationX DECIMAL NOT NULL,
   destinationY DECIMAL NOT NULL,
   startTime Timestamp NOT NULL,
   endTime Timestamp
);