-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_shows 
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
AND tv_shows.title = "Dexter"
RIGHT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NULL ORDER BY tv_genres.name;
