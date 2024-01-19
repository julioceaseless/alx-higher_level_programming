-- script displays the top 3 of cities temperatures during JUly and AUG

SELECT city, avg(value) AS avg_temp
FROM temperatures
WHERE month > 6 and month < 9
GROUP BY city 
ORDER BY avg_temp DESC LIMIT 3;
