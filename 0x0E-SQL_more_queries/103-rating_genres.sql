-- Script lists all genres in database by their rating
--	Each record should display tv_genres.name - rating sum

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_genres
RIGHT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
