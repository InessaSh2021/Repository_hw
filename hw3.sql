create table if not exists  Album_list (
AlbumList_id integer primary key not null,
AlbumTitle varchar(50) not null,
YearOfRelease integer,
Album_id integer primary key not null references Track_list(TrackList_id)
);

create table if not exists List_of_collections (
ListOfCollections_id integer,
CollectionsName varchar(50) not null,
CollectionsYear integer,
Collections_id serial primary key not null
);

create table if not exists CollectionsTrackList(
id serial primary key,
id_list_of_collections integer not null references List_of_collections(id_list_of_collections),
track_id integer not null references Track_list(track_id)
);

create table if not exists Track_list (
TrackList_id integer primary key not null,
TrackName varchar(50) not null,
TrackDuration real,
Track_id serial primary key not null 
);

create table if not exists Genres_list (
GenresList_id integer primary key not null,
GenresName1 varchar(50) not null,
GenresName2 varchar(50) not null,
GenresName3 varchar(50) not null,
GenresNameN varchar(50) not null,
Genres_id serial 
);

create table if not exists Artist_list (
ArtistList_id integer primary key not null,
ArtistsName_Alias_1 varchar(50) not null,
ArtistsName_Alias_2 varchar(50) not null,
ArtisisName_Alias_3 varchar(50) not null,
ArtistsName_Alias_N varchar(50) not null,
Artist_id serial not null 
);

create table if not exists ArtistGenre (
id serial primary key,
ListOfGenre_id integer not null references Genres_list(GenresList_id),
ListOfArtist_id integer not null references Artist_list(ArtistList_id)
); 

create table if not exists ArtistAlbumList (
id serial primary key,
id_list_of_artist integer not null references Artist_list(ArtistList_id),
id_album_list integer not null references Album_list(AlbumList_id)
);
