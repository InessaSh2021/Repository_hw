create table if not exists  Album_list (
album_id serial primary key not null,
track_id: integer
album_title varchar(50),
year_of_release integer
);

create table if not exists List_of_collections (
collection_id serial primary key not null,
collectionstitle varchar(50),
collectionsyear integer
);

create table if not exists CollectionsTrackList(
collections_id integer not null references List_of_collections(collection_id),
track_id integer not null references Track_list(track_id)
);

create table if not exists Track_list (
track_id serial primary key not null references Album_list(album_id) ,
track_name varchar(50),
track_duration real 
);

create table if not exists Genres_list (
genre_id serial primary key not null,
genrestitle varchar(30)
);

create table if not exists Artist_list (
artist_id serial primary key not null,
artistsname: varchar(50)
);

create table if not exists ArtistsGenre (
genre_id integer not null references Genres_list(genre_id),
artist_id integer not null references Artist_list(artist_id)
); 

create table if not exists ArtistAlbumList (
artist_id integer not null references Artist_list(artist_id),
album_id integer not null references Album_list(album_id)
);








