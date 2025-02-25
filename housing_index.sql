-- Create Table

CREATE TABLE housing_index (
	Date TEXT NOT NULL,
	geography VARCHAR(100) NOT NULL,
    housing_category VARCHAR(50) NOT NULL,
    index_value DECIMAL(10, 1) NOT NULL
);

SELECT *
FROM housing_index;

