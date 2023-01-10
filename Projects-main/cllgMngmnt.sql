show databases;
use college;
show tables;
create database school;

drop table studentLoginDets;
drop table teacherLoginDets;
drop table users;
drop trigger stuLogin;
drop trigger teachLogin;

select * from studentDets;
select * from teacherDets;
select * from users;

/* Tables */
create table studentDets (
	reg_no INT NOT NULL unique PRIMARY KEY,
    name VARCHAR(100) not null,
    DateOfBirth DATE not null,
    phoneNo int,
    emailAdd varchar(100),
    password varchar(100) not null,
    Address varchar(100),
    Course varchar(100) not null
);

insert into studentDets values(5,'aas','2001-01-18',985463214,'afd@gmail.com','esdd','chennai','CSE');

create table teacherDets (
	reg_no INT NOT NULL unique PRIMARY KEY,
    name VARCHAR(100) not null,
    DateOfBirth DATE not null,
    phoneNo int,
    emailAdd varchar(100),
    password varchar(100) not null,
    Address varchar(100),
    Course varchar(100) not null
);

insert into teacherDets values(1,'a','2001-02-18',98563214,'asd@gmail.com','asdd',null,'CSE');
 
create table users (
	reg_no int,
    password varchar(100),
    privilege varchar(100));

    
/* Triggers */
CREATE trigger stuLogin 
after insert
on studentDets
for each row
insert into USERS values(NEW.reg_no,NEW.password,'Student');

CREATE trigger teachLogin 
after insert 
on teacherDets
for each row
insert into USERS values(NEW.reg_no,NEW.password,'Teacher');
