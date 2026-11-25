-- List scores of at least 10 and their names, highest score first.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
