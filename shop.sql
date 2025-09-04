create database shop;
use shop;
drop database shop;

create table product(
	code char(3) primary key,
    name varchar(100) not null,
    price int default 0
);
drop table product;

insert into product(code, name, price) values('101', '냉장고', 3500000);
insert into product(code, name, price) values('102', '세탁기', 2300000);
insert into product(code, name, price) values('103', '스타일러', 1700000);
select * from product;

create table sale(
	seq int primary key auto_increment,
    code  char(100) not null,
    date datetime,
    qnt int default 0,
	price int default 0,
    foreign key(code) references product(code)
);

insert into sale(code, date, qnt, price) values('101', now(), 12, 3250000);
insert into sale(code, date, qnt, price) values('102', now(), 5, 2100000);
insert into sale(code, date, qnt, price) values('103', now(), 6, 1500000);
insert into sale(code, date, qnt, price) values('103', now(), 15, 1700000);

desc sale;
drop table sale;
select * from sale;
delete from product where code = '';

select * from product where code = '101';

commit;
create view view_sale as
	select sale.*, pro.name, pro.price as pro_price, date_format(date, '%Y-%m-%d') as fdate
	from product as pro, sale
	where pro.code = sale.code;
    
select * from view_sale where name like '%%';

drop view view_sale;

select * from hollys;

select * from gmarket;
select * from books;