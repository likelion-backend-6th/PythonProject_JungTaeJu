import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    dbname='library',
    user='postgres',
    password='1234'
)

cur = conn.cursor()


def book_add():
    print('책 추가 하기')
    title = input('책 제목 입력 : ')
    author = input('저자 입력 : ')
    pub = input('출판사 입력 : ')

    cur.execute(
        f"INSERT INTO books (title, author, publisher, borrowed) VALUES ('{title}', '{author}', '{pub}', 'false')")
    conn.commit()


def book_search():
    cur2 = conn.cursor()
    print('책 찾기')
    num = input('id로 찾기 : 1 입력\n이름으로 찾기 : 2 입력 \n입력 : ')
    search_info = input('검색 하려는 값 입력 : ')

    if num == '1':
        cur.execute(f"SELECT (id, title, author, publisher) FROM books WHERE id = {search_info}")
        cur2.execute(f"SELECT (borrowed) FROM books WHERE id = {search_info}")
    else:
        cur.execute(f"SELECT (id, title, author, publisher) FROM books WHERE title LIKE '%{search_info}%'")
        cur2.execute(f"SELECT (borrowed) FROM books WHERE title LIKE '%{search_info}%'")

    rows = cur.fetchall()
    rows2 = cur2.fetchall()
    if rows:
        for row, row2 in zip(rows, rows2):
            print(row[0])
            if not row2:
                print("대출 가능")
            else:
                print("대출 불가능")
    else:
        print("검색 결과 없음.")
    cur2.close()
# row 로 오는 튜플 분리,...

def book_borrow():
    print('책 대출')
    num = input('대출 하려는 책 id로 찾기 : 1 입력\n대출 하려는 책 이름으로 찾기 : 2 입력 \n입력 : ')
    search_info = input('검색 하려는 값 입력 : ')

    if num == '1':
        cur.execute(f"SELECT (id, borrowed) FROM books WHERE id = {search_info}")
    else:
        cur.execute(f"SELECT (id, borrowed) FROM books WHERE title LIKE '%{search_info}%'")

    rows = cur.fetchall()
    if rows:
        for row in rows:
            if row[0][3] == 'f':
                print(f"{search_info}..책을 대출합니다.")
                cur.execute(f"UPDATE books SET borrowed = 'true' WHERE id = {int(row[0][1])}")
                conn.commit()
            else:
                print("대출 불가능")
    else:
        print("검색 결과 없음.")


def book_return():
    print('책 반납')
    num = input('반납 하려는 책 id로 찾기 : 1 입력\n반납 하려는 책 이름으로 찾기 : 2 입력 \n입력 : ')
    search_info = input('검색 하려는 값 입력 : ')

    if num == '1':
        cur.execute(f"SELECT (id, borrowed) FROM books WHERE id = {search_info}")
    else:
        cur.execute(f"SELECT (id, borrowed) FROM books WHERE title LIKE '%{search_info}%'")

    rows = cur.fetchall()
    if rows:
        for row in rows:
            if row[0][3] == 't':
                print(f"{search_info}..책을 반납합니다.")
                cur.execute(f"UPDATE books SET borrowed = 'false' WHERE id = {int(row[0][1])}")
                conn.commit()
            else:
                print("반납 불가능")
    else:
        print("검색 결과 없음.")


def book_borrowed_info():
    print("현재 대출중인 책 목록")
    cur.execute(f"SELECT * FROM books WHERE borrowed = 'true'")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def book_list():
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def library_system():
    while True:
        print('\n\n도서 관리 시스템 입니다.')
        print('1. 도서 데이터 추가')
        print('2. 도서 정보 조회')
        print('3. 도서 대출')
        print('4. 도서 반납')
        print('5. 도서 대출 정보')
        print('6. 도서 목록 확인')
        order = input('목록에 없는 입력시 프로그램이 종료 됩니다.\n 메뉴 번호를 입력하여 실행 하십시오 : ')
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
        elif order == '6':
            book_list()
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

# # 1번 항목 borrowed false로 update
# cur.execute("UPDATE books SET borrowed = 'false' WHERE id = 1")
# conn.commit()


cur.close()
conn.close()
