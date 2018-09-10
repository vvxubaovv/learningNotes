use test;

drop table if exists test1;

create table if not exists test1(
id int primary key auto_increment,
name varchar(20)
);

insert into test1(name) values('xubao1');
insert into test1(name) values('xubao2');
insert into test1(name) values('xubao3');
insert into test1(name) values('xubao4');
insert into test1(name) values('xubao5');

#切换定界符

delimiter //
drop function if exists find//
create function find(_id int) returns varchar(20)
begin
	return(select name from test1 where id=_id);
end//

drop function if exists find1//
create function find1(_id int) returns varchar(20)
begin
	set @ret=(select name from test1 where id=_id);
	return @ret;
end//

-- drop function if exists find2//
-- ERROR 1415 (0A000) at line 33: Not allowed to return a result set from a function
-- create function find2(_id int) returns varchar(20)
-- begin
-- 	set @ret='';
-- 	select @ret:=name from test1 where id=_id;
-- 	return @ret;
-- end//

drop function if exists find3//
create function find3(_id int) returns varchar(20)
begin
	select name from test1 where id=_id into @ret;
	return @ret;
end//

delimiter ;

select find(1);
select find(2);
select find(3);

select find1(4);
select find1(5);

select find3(1);

# -----------------------------------

delimiter //

drop function if exists check_table_exists//
create function check_table_exists(_db varchar(30),_table varchar(30)) returns bool
begin
	set @ret=(select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA=_db and TABLE_NAME=_table limit 1);
	return @ret=_table;
end//

drop function if exists check_column_exists//
create function check_column_exists(_db varchar(30),_table varchar(30),_column varchar(30)) returns bool
begin
	set @ret=(select column_name from information_schema.columns where table_schema=_db and table_name=_table and column_name=_column);
	return @ret=_column;
end//

delimiter ;

select check_table_exists('test','test1');
select check_table_exists('test','test2');

select check_column_exists('test','test1','id');
select check_column_exists('test','test1','id1');

#-----------------------------------------------------------

delimiter //

drop function if exists if_column_exists_change//
create function if_column_exists_change(_db varchar(20),_table varchar(20),_column varchar(20)) returns int
begin
 IF check_column_exists(_db,_table,_column) then
 set @a=1;
 end IF;
 return 1;
end//

delimiter ;

select if_column_exists_change('test','test1','id');
