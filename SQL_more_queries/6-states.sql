-- Create the database and its states table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the states table with an automatically assigned ID.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
