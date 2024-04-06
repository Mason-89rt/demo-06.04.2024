create table user(
id integer primary key autoincrement,
login varchar,
password varchar,
email varchar,
role_id integer,
foreign key (role_id) references role(id)
);
create table staff(
id integer primary key autoincrement,
name varchar,
surname varchar,
user_id integer,
foreign key (user_id) references user(id)
);
create table role(
id integer primary key autoincrement,
name varchar
);
create table patient(
id integer primary key autoincrement,
name varchar,
surname varchar,
address varchar,
phone varchar,
gender_id integer,
foreign key (gender_id) references gender(id)
);
create table gender(
id integer primary key autoincrement,
name varchar
);



