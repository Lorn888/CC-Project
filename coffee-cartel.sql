DROP DATABASE IF EXISTS coffee_cartel_db;
CREATE DATABASE coffee_cartel_db;



DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    location VARCHAR(255),
    total_amount DECIMAL(10, 2),
    payment_method VARCHAR(50)
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    transaction_id INTEGER,
    item_name VARCHAR(255),
    item_price DECIMAL(10, 2),
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
);

INSERT INTO transactions (timestamp, location, total_amount, payment_method) VALUES
('2023-09-05 09:00:00', 'Leeds', 7.8, 'CARD'),
('2023-09-05 09:01:00', 'Leeds', 4.0, 'CASH'),
('2023-09-05 09:03:00', 'Leeds', 6.4, 'CARD'),
('2023-09-05 09:04:00', 'Leeds', 3.55, 'CARD'),
('2023-09-05 09:06:00', 'Leeds', 4.4, 'CASH');

INSERT INTO items (transaction_id, item_name, item_price) VALUES
(1, 'Regular Iced americano', 2.15),
(1, 'Large Hot Chocolate', 1.70),
(1, 'Regular Iced americano', 2.15),
(1, 'Large Filter coffee', 1.80),
(2, 'Large Chai latte', 2.60),
(2, 'Regular Hot Chocolate', 1.40),
(3, 'Regular Chai latte', 2.30),
(3, 'Regular Filter coffee', 1.50),
(3, 'Large Chai latte', 2.60),
(4, 'Regular Iced americano', 2.15),
(4, 'Regular Hot Chocolate', 1.40),
(5, 'Large Speciality Tea - English breakfast', 1.60),
(5, 'Regular Filter coffee', 1.50),
(5, 'Regular Speciality Tea - English breakfast', 1.30);
