-- script displays the top 3 of cities temperatures during JUly and AUG

SELECT city, avg(value) AS temp
FROM temperatures
WHERE month > 6 AND month < 9
GROUP BY city 
ORDER BY temp DESC LIMIT 3;
