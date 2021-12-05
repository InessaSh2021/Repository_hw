SELECT genrestitle, COUNT(artistsname_alias) FROM ArtistGenre ag
JOIN Genres_list g ON ag.genre_id = g.genre_id;
JOIN Artisi_list a ON ag.artist_id = a.artisi_id;

SELECT COUNT(track_name) FROM Track_lict t
WHERE year_of_release BETWEEN 2018 AND 2020;
JOIN Album_list a ON t.track_id = a.track_id;

SELECT AVG(track_duration) FROM Album_list a
JOIN Track_list t ON a.track_id = t.track_id;

SELECT artistsname FROM ArtistAlbumList aa
WHERE year_of_release != 2020;
JOIN Artist_list a ON aa. artist_id = a.artist_id;
JOIN Album_list al ON aa.album_id = al.album_id;

SELECT collectionstitle FROM List_of_collections lc
HAVING artistsname = Mylene Farmer;
JOIN CollectionsTrackList cl ON lc.collection_id = cl.collection_id;
JOIN Track_list t ON cl.track_id = t.track_id;
JOIN Album_list a ON t.track_id = a.track_id;
JOIN ArtistAlbumList aa ON a.album_id = aa.album_id;
JOIN Artist_list al ON aa.artist_id = al.artisi_id;

SELECT album_title FROM Album_list a
HAVING artistsname = 1 AND COUNT(genrestitle) > 1;
JOIN ArtistAlbumList aa ON a.album_id = aa.album_id;
JOIN Artist_list al ON aa.artist_id = al.artist_id;
JOIN ArtistsGenre ag ON al.artist_id = ag.artist_id;
JOIN Genres_list gl ON ag.genre_id = al.genre_id;


SELECT track_name FROM CollectionsTrackList cl
JOIN Track_list t ON cl.track_id = t.track_id;
JOIN List_of_collections lc ON cl.collection_id = lc.collection_id;
HAVING track_id != collection_id;

SELECT artistsname FROM Artist_list a
JOIN ArtistAlbumList aa ON a.artist_id = aa.artist_id;
JOIN Album_list al ON aa.album_id = al.album_id;
JOIN Track_list t ON al.track_id = t.track_id;
HAVING track_duration = min();

SELECT album_title FROM Album_list a
JOIN Track_list t ON a.track_id = t.track_id;
HAVING SUM(track_name) = min ();























