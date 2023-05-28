-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_test_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev.* TO 'hbnb_dev'@'localhost';

-- Grant select privilege on the perfomance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
