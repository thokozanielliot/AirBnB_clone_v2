-- this script prepares a MySQL server for the project
-- Create project development database with the name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Createing new user name: hbnb_dev with all privileges on the db hbnb_dev_db
-- with the password: hbnb_dev_pwd if it deosn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localgost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Granting all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Granting the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
