set timezone='UTC';

CREATE TABLE  user_  (
   id          INT PRIMARY KEY ,
   pseudo      VARCHAR(20) ,
   password    VARCHAR(64) NOT NULL,
   cardNum        VARCHAR(64) NOT NULL  UNIQUE,
);