-- Create the database for the read-only account.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the localhost account for reading the database.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Grant read access to the exercise database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
