-- Create the localhost account with server-wide privileges.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all server-wide privileges to the account.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
