DROP DATABASE IF EXISTS coffee_cartel_db;
CREATE DATABASE coffee_cartel_db;



DROP TABLE IF EXISTS transactions_details CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;

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
