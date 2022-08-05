CREATE EXTENSION pgcrypto;

DROP TABLE IF EXISTS project_2.reviews;
DROP TABLE IF EXISTS project_2.users;
DROP TABLE IF EXISTS project_2.books;

CREATE TABLE project_2.users (
	id SERIAL UNIQUE NOT NULL,
	username VARCHAR UNIQUE NOT NULL,
	password VARCHAR NOT NULL,
	fav_genre VARCHAR DEFAULT null,
	date_joined TIMESTAMP NOT NULL,
	is_admin BOOLEAN DEFAULT False
);

CREATE TABLE project_2.books (
	isbn VARCHAR PRIMARY KEY UNIQUE NOT NULL,
	title VARCHAR NOT NULL,
	author VARCHAR NOT NULL,
	edition INTEGER,
	genre VARCHAR,
	media_type VARCHAR
);

CREATE TABLE project_2.reviews (
	isbn VARCHAR NOT NULL,
	review VARCHAR NOT NULL,
	usr VARCHAR NOT NULL,
	rating VARCHAR NOT NULL,
	CONSTRAINT fk_usr FOREIGN KEY (usr) REFERENCES project_2.users(username),
	CONSTRAINT fk_isbn FOREIGN KEY (isbn) REFERENCES project_2.books(isbn)
);

SELECT * FROM project_2.reviews;
SELECT * FROM project_2.books;
SELECT * FROM project_2.users;
