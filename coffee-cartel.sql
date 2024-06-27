DROP DATABASE IF EXISTS coffee_cartel_db;
CREATE DATABASE coffee_cartel_db;



DROP TABLE IF EXISTS transactions_details;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions_details (
    transaction_details_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    location VARCHAR(255),
    total_amount DECIMAL(10, 2),
    payment_method VARCHAR(50)
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(255),
    item_price DECIMAL(10, 2)
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    item_id INTEGER NOT NULL,
    transaction_details_id INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items (item_id),
    FOREIGN KEY (transaction_details_id) REFERENCES transactions_details (transaction_details_id)
);

INSERT INTO transactions_details (timestamp, location, total_amount, payment_method) VALUES
('2023-09-05 09:00:00', 'Leeds', 7.8, 'CARD'),
('2023-09-05 09:01:00', 'Leeds', 4.0, 'CASH'),
('2023-09-05 09:03:00', 'Leeds', 6.4, 'CARD'),
('2023-09-05 09:04:00', 'Leeds', 3.55, 'CARD'),
('2023-09-05 09:06:00', 'Leeds', 4.4, 'CASH');

INSERT INTO items (item_name, item_price) VALUES
('Large Iced americano', 2.50),
('Large Hot Chocolate', 1.70),
('Large Filter coffee', 1.80),
('Large Chai latte', 2.60),
('Large Speciality Tea - English breakfast', 1.60),
('Regular Iced americano', 2.15),
('Regular Hot Chocolate', 1.40),
('Regular Chai latte', 2.30),
('Regular Filter coffee', 1.50),
('Regular Speciality Tea - English breakfast', 1.30);