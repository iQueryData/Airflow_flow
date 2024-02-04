create schema dummy_schema;

create table dummy_schema.dummy(
    id serial,
    names varchar
);

insert into dummy_schema.dummy(names) values ('jon');