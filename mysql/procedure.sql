-- mysql的set和declare区别
-- 1. 类型声明
-- set 不需要声明类型，declare必须指定类型
-- 
-- 2. 位置
-- set 位置可以任意, declare 必须在复合语句的开头，在任何其它语句之前
-- 
-- 3.作用范围
-- DECLARE 定义的变量的作用范围是BEGIN … END块内，只能在块中使用。
-- SET 定义的变量用户变量，作用范围是会话/全局
--     如SET @var=12的定义，则var的作用域为整个会话，为会话变量.
--     如SET global var=12的定义，则var的作用域为全局，为全局变

#存储过程
use test;

delimiter //
drop procedure if exists test1//
create procedure test1()
begin
select * from test1;
end//

drop procedure if exists test2//
create procedure test2(in a int)
begin
select * from test1 where id=a;
end//

drop procedure if exists test3//
create procedure test3(in a int,out b int)
begin
select (id+1) into b from test1 where id=a;
end//

drop procedure if exists test4//
create procedure test4(inout a int)
begin
select (id+1) into a from test1 where id=a;
end//

drop procedure if exists test5//
create procedure test5(inout a int)
begin
if a=1
then
select (id+1) into a from test1 where id=a; #当查不出来时不改变a
elseif a=2  #此处小坑
then
select (id+50) into a from test1 where id=a;
else
select (id+100) into a from test1 where id=a;
end if;
end//

delimiter ;

call test1;
call test2(1);
set @b=1;
call test3(2,@b);
select @b;

set @a=1;
call test4(@a);
select @a;


set @c=2;
call test5(@c);
select @c;