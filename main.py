import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    dbname='library',
    user='postgres',
    password='1234'
)

cur = conn.cursor()

def book_search():
    pass


def book_add():
    print('책 추가 하기')
    title = input('책 제목 입력 : ')
    author = input('저자 입력 : ')
    pub = input('출판사 입력 : ')

    cur.execute(f"INSERT INTO books (title, author, publisher, borrowed) VALUES ('{title}', '{author}', '{pub}', 'false')")
    conn.commit()



def book_borrow():
    pass


def book_return():
    pass


def book_borrowed_info():
    pass


def library_system():
    while True:
        print('도서 관리 시스템 입니다.')
        print('1. 도서 데이터 추가')
        print('2. 도서 정보 조회')
        print('3. 도서 대출')
        print('4. 도서 반납')
        print('5. 도서 대출 정보')
        order = input('목록에 없는 입력시 프로그램이 종료 됩니다.\n메뉴 번호를 입력하여 실행 하십시오 : ')
        if order == '1':
            book_add()
        elif order == '2':
            book_search()
        elif order == '3':
            book_borrow()
        elif order == '4':
            book_return()
        elif order == '5':
            book_borrowed_info()
        else:
            break


library_system()


# cur.execute('''
#     CREATE TABLE books (
#         id SERIAL PRIMARY KEY ,
#         title VARCHAR(50),
#         author VARCHAR(50),
#         publisher VARCHAR(50),
#         borrowed BOOLEAN,
#         borrowed_date DATE)
# ''')
# conn.commit()
cur.execute("UPDATE books SET borrowed = 'false' WHERE id = 1")
conn.commit()
# 1번 항목 borrowed false로 update

cur.execute("SELECT * FROM books")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
