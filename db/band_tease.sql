DROP TABLE IF EXISTS bands;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS users_bands;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255)
);

CREATE TABLE bands (
    id SERIAL PRIMARY KEY,
    band_name VARCHAR(255),
    favourite_song VARCHAR(255),
    favourite_album VARCHAR(255),
    fun_fact VARCHAR(255)
);

CREATE TABLE users_bands (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    band_id INT REFERENCES bands(id) ON DELETE CASCADE

);