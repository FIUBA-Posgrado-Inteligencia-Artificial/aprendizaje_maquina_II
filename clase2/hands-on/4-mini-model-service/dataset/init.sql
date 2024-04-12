CREATE TABLE salary_data (
    usr_id INT,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    email TEXT,
    phone TEXT,
    date_of_birth DATE,
    job TEXT,
    experience TEXT,
    salary MONEY
);

COPY salary_data
FROM '/docker-entrypoint-initdb.d/salaries.csv'
DELIMITER ','
CSV HEADER;
