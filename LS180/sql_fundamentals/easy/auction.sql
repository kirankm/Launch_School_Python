DROP TABLE IF EXISTS bidders CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS bids;

CREATE TABLE bidders (
    id serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE items (
    id serial PRIMARY KEY,
    name text NOT NULL,
    initial_price decimal(6,2) NOT NULL CHECK(initial_price > 0),
    sales_price decimal(6,2) CHECK(sales_price > 0)
);

CREATE TABLE bids (
    id serial PRIMARY KEY,
    bidder_id int NOT NULL REFERENCES bidders(id) ON DELETE CASCADE,
    item_id int NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    amount decimal(6,2) NOT NULL CHECK(amount > 0)
);

CREATE INDEX bidder_item_index ON bids (bidder_id, item_id);


\copy bidders (id, name) FROM bidders.csv DELIMITER ',' CSV HEADER;
\copy items (id, name, initial_price, sales_price) FROM items.csv DELIMITER ',' CSV HEADER;

\copy bids (id, bidder_id, item_id, amount) FROM bids.csv DELIMITER ',' CSV HEADER;