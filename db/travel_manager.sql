DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;

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
