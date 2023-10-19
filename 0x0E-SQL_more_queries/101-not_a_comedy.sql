-- Script that lists all shows without the genre Comedy.
SELECT title FROM tv_shows WHERE title NOT IN (
    SELECT tv_shows.title FROM tv_genres, tv_show_genres, tv_shows
    WHERE tv_genres.id = tv_show_genres.genre_id
    AND tv_show_genres.show_id = tv_shows.id AND tv_genres.name = 'Comedy')
ORDER BY title ASC;
