select album_title, year_of_release from Album_list 
WHERE year_of_release = 2018;

select track_name, track duration from Track_list
ORDER BY length DESC
LIMIT 1;

select track_name from Track_list 
where track_duration < 3,5;

select collectionstitle from List_of_collections 
where collectionstitle NOT LIKE '%% %%';

select collectionstitle from List_of_collections 
WHERE collectionsyear BETWEEN 2018 AND 2020;

select track_name from Track_list 
where track_name like '%%my%%';
