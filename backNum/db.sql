/* 
VSCode-MySQL
https://velog.io/@helloaltjs/VSCode-MySql-%EC%97%B0%EB%8F%99

파이썬과 MySQL 데이터베이스 연동하기(+ pymysql 라이브러리 설치)
https://hongong.hanbit.co.kr/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BC-mysql-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0-pymysql-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EC%84%A4/


DB에 저장할 것:
COLUMN:
등번호
이름
나이
포지션
들어온 날짜
나간 날짜
primary-key

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
alter table backNum add shirtsize int;
수정
alter table backNum modify shirtsize rename column shirtsize to shirtsize;

삭제
alter table backNum drop shirtsize;
=================================================================================================
CREATE TABLE 할 때 primary-key를 넣을 것(데비터베이스의 제1 정규성(데이터 정규화)을 지켜야 한다)
https://youtu.be/Y1FbowQRcmI?si=Jai7HNJs3ndsGj2z 


*/
CREATE databases football
;

show databases
;

CREATE TABLE backNum(
    num INT unique, -- unique는 겹치면 안 됨 => 겹치면 오류
    backname CHAR(15), 
    age INT, 
    pos CHAR(8)
)
;

DESC backNum
;

USE football
;

INSERT INTO backNum(
    num, 
    backname, 
    age, 
    pos
)
VALUES(
    1, 
    'jeongseyun', 
    20, 
    'GK/RW'
)
;
# 일일히 다 넣어야 하나? => 테이블 삽입 기능 있는지 알아보기

UPDATE backNum(SET pos='GK' WHERE num=1)
;

DELETE 
FROM backNum 
WHERE num=1
    AND pos='GK' 
;

ALTER TABLE backNum
;

ADD shirtsize INT
;

ALTER TABLE backNum 
MODIFY shirtsize rename column shirtsize TO shirtsize
;

ALTER TABLE backNum 
DROP shirtsize
;