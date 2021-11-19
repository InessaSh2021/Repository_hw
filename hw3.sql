create table if not exists  Album_list (
AlbumList_id integer primary key,
AlbumTitle varchar(50) not null,
YearOfRelease integer,
Album_id serial primary key
);
create table if not exists List_of_collections (
ListOfCollections_id integer,
CollectionsName varchar(50) not null,
CollectionsYear integer,
Collections_id serial primary key
);
create table if not exists Track_list (
TrackList_id integer primary key not null references List_of_collections(ListOfCollections_id),
TrackName varchar(50) not null,
TrackDuration real,
Track_id serial primary key not null references Album_list(AlbumList_id)
);
create table if not exists Genres_list (
GenresList_id integer,
GenresName1 varchar(50) not null,
GenresName2 varchar(50) not null,
GenresName3 varchar(50) not null,
GenresNameN varchar(50) not null,
Genres_id serial primary key
);
create table if not exists Artist_list (
ArtistList_id integer,
ArtistsName_Alias_1 varchar(50) not null,
ArtistsName_Alias_2 varchar(50) not null,
ArtisisName_Alias_3 varchar(50) not null,
ArtistsName_Alias_N varchar(50) not null,
Artist_id serial primary key not null references Album_list(Album_id)
);
create table if not exists ArtistGenre (
ListOfGenre_id integer not null references Genres_list(GenresList_id),
ListOfArtist_id integer not null references Artist_list(ArtistList_id) 
);
