create table if not exists EmployeesBosses (
id serial primary key not null,
List_of_employees_id integer not null referenses EmployeesBosses(id),
List_of_bosses_id integer not null references EmployeesBosses(id)
);

