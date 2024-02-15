-- lists all the cities of California that are found in the database hbtn_0d_usa
-- lists all rows of the column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
