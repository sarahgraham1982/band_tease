DROP TABLE IF EXISTS bands;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE bands (
    id SERIAL PRIMARY KEY,
    band_name VARCHAR(255),
    genre VARCHAR(255),
    favourite_song VARCHAR(255),
    favourite_album VARCHAR(255),
    fun_fact VARCHAR(255),
    tee_image VARCHAR(255),
    user_id INT REFERENCES users(id)
);
