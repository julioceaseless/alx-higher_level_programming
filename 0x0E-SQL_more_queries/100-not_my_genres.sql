-- nested script
-- script that uses the hbtn_0d_tvshows database to list
-- all genres not linked to the show Dexter

SELECT tv_genres.name 
FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT genre_id FROM tv_show_genres
	RIGHT JOIN tv_shows ON show_id = id
	WHERE title = "Dexter")
ORDER BY tv_genres.name ASC;
