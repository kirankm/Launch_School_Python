-- CREATE DATABASE IF NOT EXISTS animals;

\c animals

DROP TABLE IF EXISTS birds;

CREATE TABLE birds(
    id serial PRIMARY KEY,
    name varchar(25),
    age int,
    species varchar(15)
);
