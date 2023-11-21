/* 
DB에 저장할 것:
등번호-이름-나이-포지션 

기능:
추가(새로운 팀원), 삭제(나가는 팀원), 수정(등번호, 나이, 포지션)
*/
create databases football;
show databases;
create table backNum(num int, name char(15), age int, pos char(8));
desc backNum;

use football;

insert into backNum(num, name, age, pos) values(1, 'jeongseyun', 20, 'GK/RW')

