-- SQL script that creates a table users with these
-- requirements:id, email, name, country

CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL,
name VARCHAR(255),
country ENUM('US', 'CO', 'UN')
);
