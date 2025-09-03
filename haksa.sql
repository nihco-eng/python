create database haksa;
use haksa;
drop database haksa;

create table dept(
   dcode int primary key auto_increment,
    dname varchar(100) not null
);
drop table dept;
drop table student;

insert into dept(dname) values('컴퓨터정보공학과');
insert into dept(dname) values('전자공학과');
insert into dept(dname) values('건축공학과');

select * from dept;
select * from student;

create table student(
   id char(4) primary key,
    name varchar(50) not null,
    code int not null,
    foreign key(code) references dept(dcode)
);

insert into student(id, name, code) values('2501', '홍길동', 1);
insert into student(id, name, code) values('2502', '홍길동', 3);
insert into student(id, name, code) values('2503', '심청이', 2);
insert into student(id, name, code) values('2504', '강감찬', 2);
select * from student;

create view vstudent as
   select student.*, dept.dname
   from student, dept
   where code=dcode;
show variables like 'datadir';
select * from vstudent order by name;
commit;

select convert(max(id)+1, char(4)) as new_id from student;

ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';