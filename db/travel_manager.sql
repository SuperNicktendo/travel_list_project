DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS visited;
DROP TABLE IF EXISTS wishlist;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT NOT NULL REFERENCES countries(id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE visited (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL REFERENCES cities(id),
    user_id INT NOT NULL REFERENCES users(id)
);

CREATE TABLE wishlist (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL REFERENCES cities(id),
    user_id INT NOT NULL REFERENCES users(id)
);