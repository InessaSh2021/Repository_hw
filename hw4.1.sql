insert into Artist_list (first_name)
values 
('Sakis'),
('Celine'),
('Enrique'),
('Scorpions'),
('Maneskin'),
('Mylene'),
('Natalia'),
('Ricky');

insert into Artist_list (last_name)
values 
('Rouvas'),
('Dion'),
('Iglesias'),
(''),
(''),
('Farmer'),
('Oreiro'),
('Martin');

insert into Album_list (album_title)
values 
('Iparhi Agapi Edo'),
('Courage'),
('Euphoria'),
('Return to Forever'),
('Teatro dira'),
('LAutre'),
('Turmalina'),
('La Historia');

insert into Album_list (year_of_release)
values 
('2006'),
('2019'),
('2010'),
('2015'),
('2021'),
('1991'),
('2002'),
('2001');

insert into Album_list (album_id, track_id)
values 
('1', '1'),
('1', '9'),
('2', '2'),
('2', '10'),
('3', '3'),
('3', '11'),
('4', '4'),
('4', '12'),
('5', '5'),
('5', '13'),
('6', '6'),
('6', '14'),
('7', '7'),
('7', '15'),
('8', '8'),
('8', '16');


insert into Track_list (track_name1)
values 
('Irthes'),
('Courage'),
('I Like It'),
('All for One'),
('Zitti e buoni'),
('Regrets'),
('Cayendo'),
('Maria');

insert into Track_list (track_duration1)
values 
('3.14'),
('5.14'),
('3.14'),
('4.30'),
('3.50'),
('4.15'),
('4.15'),
('4.15');

insert into Track_list (track_name2)
values 
('Ela Edo'),
('Say Yes'),
('Ayer'),
('Gypsy Life'),
('Coraline'),
('LAutre'),
('No soporto'),
('La Copa de la Vida');

insert into Track_list (track_duration2)
values 
('3.50'),
('4.50'),
('4.40'),
('3.20'),
('4.20'),
('4.20'),
('4.20'),
('4.20');


insert into Genres_list (genrestitle)
values 
('pop'),
('dance musik'),
('pop'),
('hard rock'),
('rock'),
('sinthpop'),
('dance musik'),
('pop');

insert into List_of_collections (collectionstitle)
values 
('This Is My Live'),
('Celine Dion Concert'),
('Enrique Iglesias & Jennifer Lopez Tour'),
('World Wide Life'),
('Il ballo della vita'),
('Mylenium Tour'),
('Natalia Oreiro'),
('Sons of Rock');

insert into List_of_collections (collectionsyear)
values 
('2020'),
('2019'),
('2019'),
('2020'),
('2018'),
('2019'),
('2018'),
('2019');

INSERT INTO CollectionsTrackList (collections_id, track_id)
VALUES 
('1', '9'),
('2', '10'),
('3', '3'),
('4', '12'),
('5', '5'),
('6', '14'),
('7', '15'),
('8', '8');

INSERT INTO ArtistsGenre (artist_id, genre_id)
VALUES 
('1', '1'),
('2', '2'),
('3', '5'),
('4', '4'),
('5', '3'),
('6', '5'),
('7', '6'),
('8', '1');

INSERT INTO ArtistAlbumList (artist_id, album_id)
VALUES 
('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6'),
('7', '7'),
('8', '8');
