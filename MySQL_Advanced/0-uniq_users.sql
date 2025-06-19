-- creates user table with specified requirements
CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    id INT AUTO_INCREMENT NOT NULL,
    UNIQUE KEY unique_email (email),
    PRIMARY KEY (id)
);
