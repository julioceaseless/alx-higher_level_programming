-- not a comedy

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id  NOT IN (
	SELECT show_id
	FROM tv_show_genres
	LEFT JOIN tv_genres
	ON genre_id = id
	WHERE name = "Comedy")
ORDER BY tv_shows.title ASC;
