-- Count the shows linked to each genre that has at least one show.
SELECT tv_genres.name AS genre,
       COUNT(DISTINCT tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY number_of_shows DESC, tv_genres.id ASC;
