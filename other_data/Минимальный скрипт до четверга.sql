create sequence cafe_seq start with 1 increment by 1;
create sequence user_seq start with 6000 increment by 1;
create sequence employee_seq start with 1000 increment by 1;
create sequence order_seq start with 2000 increment by 1;
create sequence order_item_seq start with 3000 increment by 1;
create sequence warehouse_seq start with 4000 increment by 1;
create sequence product_seq start with 5000 increment by 1;

create table cafe(
id integer not null,
cafe_name varchar(64) not null,
country varchar(64));
alter table cafe add constraint cafe_id_pk primary key(id);

create table "user"(
id integer not null,
user_name varchar(32) not null,
user_surname varchar(32) not null,
user_patronomic varchar(32),
user_birthday date
);
alter table "user" add constraint user_id_pk primary key(id);

create table employee (
id integer not null ,
employee_name varchar(32) not null,
employee_surname varchar(32) not null,
employee_patronomic varchar(32),
cafe_id integer not null,
post varchar(64) not null
);
alter table employee add constraint employee_id_pk primary key(id);

create table "order" (
id integer not null,
cafe_id integer not null,
user_id integer not null,
description varchar(128)
);
alter table "order" add constraint order_id_pk primary key(id);

create table order_item(
id integer not null,
order_id integer not null,
item_name varchar(64) not null,
quantity integer not null
);
alter table order_item add constraint order_item_id_pk primary key(id);

create table warehouse(
id integer not null,
cafe_id integer not null
);
alter table warehouse add constraint warehous_id_pk primary key(id);

create table product(
id integer not null,
warehouse_id integer not null,
product_name varchar(64) not null,
quantity integer
);
alter table product add constraint product_id_pk primary key(id);

alter table employee add constraint employee_cafe_fk foreign key(cafe_id)
references cafe(id);
alter table "order" add constraint order_user_fk foreign key(user_id)
references "user"(id);
alter table "order" add constraint order_cafe_fk foreign key(cafe_id)
references cafe(id);
alter table order_item add constraint order_item_order_fk foreign key(order_id)
references "order"(id);
alter table warehouse add constraint warehouse_cafe_fk foreign key(cafe_id)
references cafe(id);
alter table product add constraint product_warehouse_fk foreign key(warehouse_id)
references warehouse(id);