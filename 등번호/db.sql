/* 
DB에 저장할 것:
등번호-이름-나이-포지션 

기능:
https://www.w3schools.com/sql/sql_alter.asp
레코드 추가, 수정, 삭제

추가-insert into(새로운 팀원): 
insert into backNum(num, name, age, pos) values(1, 'jeongseyun', 20, 'GK/RW')

삭제(나가는 팀원): 
delete from backNum where num=1;

수정-update(등번호, 나이, 포지션):
update backNum(set pos='GK' where num=1);


테이블 안의 필드 바꾸기(추가, 수정, 삭제)
추가
alter table backNum add size int;
수정
alter table backNum modify size;
rename column size to shirtsize

삭제
alter table backNum drop size;
*/
create databases football;
show databases;
create table backNum(num int, name char(15), age int, pos char(8));
desc backNum;

use football;

insert into backNum(num, name, age, pos) values(1, 'jeongseyun', 20, 'GK/RW')
# 일일히 다 넣어야 하나? => 테이블 삽입 기능 있는지 알아보기

update backNum(set pos='GK' where num=1);

delete from backNum where num=1;
