-- Recreate table
DROP TABLE IF EXISTS people;
CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
);

-- Seed data
insert into people (first_name, last_name) values ('Virat', 'Kohli');
insert into people (first_name, last_name) values ('Virat', 'Sharma');
insert into people (first_name, last_name) values ('Shahrukh', 'Khan');
insert into people (first_name, last_name) values ('Salman', 'Khan');
insert into people (first_name, last_name) values ('Rohit', 'Sharma');
insert into people (first_name, last_name) values ('Sachin', 'Tendulkar');
insert into people (first_name, last_name) values ('Sachin', 'Pilot');
insert into people (first_name, last_name) values ('Sara', 'Tendulkar');