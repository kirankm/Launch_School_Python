-- CREATE DATABASE IF NOT exists billing;

-- \c billing

DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS services CASCADE;
DROP TABLE IF EXISTS customer_service_map;

CREATE TABLE customers(
    id serial PRIMARY KEY,
    name text NOT NULL,
    payment_token char(8) UNIQUE NOT NULL check (payment_token ~ '^[A-Z]{8}$')
);

CREATE TABLE services(
    id serial PRIMARY KEY,
    description text NOT NULL,
    price numeric(10,2) NOT NULL check(price >= 0)
);

CREATE TABLE customer_service_map(
    id serial PRIMARY KEY,
    customer_id int NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    service_id int NOT NULL REFERENCES services(id),
    CONSTRAINT unique_customer_service_ids UNIQUE(customer_id, service_id)
);

INSERT INTO customers
(name, payment_token) VALUES
('Pat Johnson', 'XHGOAHEQ'),
('Nancy Monreal', 'JKWQPJKL'),
('Lynn Blake', 'KLZXWEEE'),
('Chen Ke-Hua', 'KWETYCVX'),
('Scott Lakso', 'UUEAPQPS'),
('Jim Pornot', 'XKJEYAZA');


INSERT INTO services
(description, price) VALUES
('Unix Hosting', 5.95),
('DNS', 4.95),
('Whois Registration', 1.95),
('High Bandwidth', 15.00),
('Business Support', 250.00),
('Dedicated Hosting', 50.00),
('Bulk Email', 250.00),
('One-to-one Training', 999.00);

INSERT INTO customer_service_map
(customer_id, service_id) VALUES
(1, 1), (1, 2), (1, 3),
(3, 1), (3, 2), (3, 3), (3,4), (3,5),
(4, 1), (4, 4),
(5, 1), (5, 2), (5, 6), 
(6, 1), (6, 7), (6, 6);




SELECT s.* 
FROM customer_service_map m 
RIGHT OUTER JOIN 
services s 
ON s.id = m.service_id 
WHERE m.id IS NULL;

SELECT c.name, string_agg(s.description, ',') as services
FROM customers c 
LEFT OUTER JOIN customer_service_map m 
ON c.id = m.customer_id 
LEFT OUTER JOIN services s 
ON s.id = m.service_id
GROUP BY c.name;


SELECT sum(price) as gross
FROM customer_service_map m 
JOIN services s 
ON s.id = m.service_id;


INSERT INTO customers
(name, payment_token) VALUES
('John Doe', 'EYODHLCN');

INSERT INTO customer_service_map
(customer_id, service_id) VALUES
(7, 1), (7, 2), (7, 3);
