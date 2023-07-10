import psycopg2
from psycopg2 import sql


def book_search():
    pass


def book_add():
    pass


def book_borrow():
    pass


def book_return():
    pass


def book_borrowed_info():
    pass


def library_system():
    while True:
        print('도서 관리 시스템 입니다.')
        print('1. 데이터 입력')
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


library_system()
