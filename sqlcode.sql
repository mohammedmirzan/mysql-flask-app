create database crud;
use crud;
show tables;

create table users(
ID int not null auto_increment primary key,
NAME varchar(50) not null,
AGE int not null,
CITY varchar(30) not null,
PHONE_NUMBER int not null
);

insert into users (NAME,AGE,CITY,PHONE_NUMBER) values ('Mirzan',23,'Kandy',0768787222);
insert into users (NAME,AGE,CITY,PHONE_NUMBER) values ('Raafiq',22,'Colombo',0768720022),('Ayyash',21,'Matara',0765550213);

delete from users where ID=2;
select * from users;