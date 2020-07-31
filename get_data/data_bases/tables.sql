DROP TABLE orders;
DROP TABLE art;
DROP TABLE users;

CREATE TABLE users
(
id_user SERIAL PRIMARY KEY,
user_type VARCHAR(10),
name VARCHAR(100),
phone NUMERIC (20),
email VARCHAR(50),
address VARCHAR(150),
city VARCHAR (100)
-- PRIMARY KEY (id_user)
);

CREATE TABLE art
(
id_art SERIAL PRIMARY KEY,
name_art VARCHAR (50),
width INTEGER,
heigth INTEGER,
description VARCHAR (100),
id_user INTEGER,

FOREIGN KEY (id_user) REFERENCES users (id_user)
);

CREATE TABLE orders
(
id_order SERIAL PRIMARY KEY,
id_user INTEGER,
id_art INTEGER,
price INTEGER,
date_time INTEGER,
approved BOOLEAN,

FOREIGN KEY (id_user) REFERENCES users (id_user),
FOREIGN KEY (id_art) REFERENCES art (id_art)
);

SELECT * FROM USERS;
SELECT * FROM ART;
SELECT * FROM ORDERS;

-- insert value into users table

INSERT INTO users (id_user, user_type, name, phone, email, address, city)
VALUES (1, 'artista', 'gilberto gil', 557199887766, 'gil@gmail.com', 'rua das chuvas fortes', 'salvador')

INSERT INTO users (id_user, user_type, name, phone, email, address, city)
VALUES (3, 'artista', 'caetano veloso', 557199554433, 'caetano@gmail.com', 'rua dos mares', 'salvador')

UPDATE users
SET id_user = 2
WHERE id_user = 3;

INSERT INTO users (user_type, name, phone, email, address, city)
VALUES 
('artista', 'chico buarque', 552147755667, 'chico@buarque.com', 'Rua das Ipanemas', 'rio de janeiro'),
('publico', 'lincoln clarete', 1999999999, 'lincoln@clarete.li', 'Rua do Brooklyn', 'NYC')


-- insert values into art
INSERT INTO art (name_art, width, heigth, description)
VALUES ('la vem o pato', 10, 15, 'arte moderna')

SELECT * FROM art


SELECT * 
FROM users
-- ORDER BY uses ASC by default
ORDER BY city DESC, phone DESC;

-- return the length of the selected column
SELECT user_type, LENGTH(address) 
FROM users;

-- return unique values
SELECT DISTINCT user_type
FROM users;

-- return the first column from the distinct value
SELECT DISTINCT ON (user_type) user_type, email
FROM users;


SELECT * 
FROM users
WHERE name = 'gilberto gil' OR city = 'salvador';


SELECT *
FROM users
WHERE city in ('rio de janeiro');

SELECT *
FROM users
WHERE user_type LIKE 'art%';

SELECT *
FROM users
WHERE city LIKE 'salv%'

SELECT * 
FROM users
WHERE user_type LIKE 'art%' AND LENGTH(email) > 16
-- LIMIT 10
-- FETCH FIRST 2 ROW ONLY;

SELECT *
FROM users
WHERE name LIKE 'cae%'

SELECT *
FROM users
WHERE CITY in ('salvador', 'rio de janeiro')

SELECT *
FROM users
WHERE id_user NOT BETWEEN 1 AND 4;

