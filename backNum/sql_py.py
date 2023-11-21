import sqlite3

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def retrive():
    connection=sqlite3.connect()
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM backNum''')
    result=dictfetchall(cursor)
    print(result) 
    
def insert():
    connection=sqlite3.connect()
    cursor=connection.cursor()
    cursor.execute("""
    INSERT INTO backNum(
        age,
        BACKNAME
    )
    VALUES(
        ?, 
        ?
    )
    """, [20, 'asdf'])
    cursor.commit()

if __name__=='__main__':
    retrive()
    

'''
sqlite -> mysql로 바꿔야 함
def retrive() 함수의 connect() 괄호 안에 로컬 서버 주소를 넣음 -> 검색

~/.bashrc 
환경변수 설정

.gitignore에 환경변수 파일을 넣어놓음 => git에 환경변수 파일이 안 올라감
'''