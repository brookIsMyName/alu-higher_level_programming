-- List California cities in ascending order by city ID.
SELECT id, name
FROM cities
WHERE state_id = (
    -- Look up California's ID by name.
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
