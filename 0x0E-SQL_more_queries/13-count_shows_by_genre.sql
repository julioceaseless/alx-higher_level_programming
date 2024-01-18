-- display count of grouped entries

SELECT tg.name as genre, COUNT(tsg.genre_id) AS number_of_shows 
FROM tv_genres tg 
JOIN tv_show_genres tsg ON tsg.genre_id = tg.id 
GROUP BY tg.name 
ORDER BY number_of_shows DESC;
