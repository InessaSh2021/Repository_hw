create table if not exists List_of_employees (
id serial primary key,
name1 varchar(50) not null,
name2 varchar(50) not null,
name3 varchar(50) not null,
nameN varchar(50) not null
);
create table if not exists List_of_bosses (
id serial primary key,
name1 varchar(50) not null,
name2 varchar(50) not null,
name3 varchar(50) not null,
nameN varchar(50) not null
);
create table if not exists EmployeesBosses (
id serial primary key,
List_of_employees_id integer not null references List_of_employees(id),
List_of_bosses_id integer not null references List_of_bosses(id)
);

