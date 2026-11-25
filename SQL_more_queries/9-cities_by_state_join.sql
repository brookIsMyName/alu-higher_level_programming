-- List each city with its state in ascending order by city ID.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
