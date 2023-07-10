# PythonProject_JungTaeJu

# 1-1. 미션 요구사항 분석 

전체적으로 메뉴를 구성하여 메인메뉴에서 특정 기능을 실행시 해당 메뉴 기능이 실행 되도록 합니다.<br>
ex) 메인 메뉴에서 데이터 입력 기능 선택시 정보를 입력받아 데이터베이스에 저장. <br>
이를 함수로 구현해볼까 합니다. <br>
전체 메뉴를 무한루프로 실행하여 종료 명령이 올때까지 루프를 돌게 하려합니다. 

데이터베이스에 저장할 정보로는 도서 ID, TITLE, AUTHOR, PUBLISHER가 있습니다. <br>
추가적으로 대출 가능정보를 저장할수 있을것 같습니다.

# 1-2. 미션 체크리스트

[V] 메인 메뉴 선택 메뉴 구현. <br>
[V] 데이터베이스 생성, 테이블 생성.<br>

### 0. CLI 기반 메뉴 (기본)

[V] (기본) 사용자는 콘솔을 통해 메뉴를 선택할 수 있습니다.<br>
[V] (기본) 사용자가 선택한 메뉴에 따라 해당 기능을 실행합니다.<br>
[V] (기본) 사용자는 메뉴를 통해 프로그램을 종료할 수 있습니다.<br>
[] (심화) 사용자는 메뉴를 통해 이전 메뉴로 돌아갈 수 있습니다.<br>
[] (심화) 메뉴 선택시 콘솔을 삭제하여 사용자가 선택한 메뉴만 출력합니다.<br>

### 1. 데이터 입력 기능 (기본)

[V] (기본) 사용자는 콘솔을 통해 도서의 정보를 입력하여 데이터베이스에 저장합니다.<br>
[V] (기본) 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함합니다.<br>
[] (심화) 파일을 통해 도서의 정보를 입력하여 데이터베이스에 저장합니다. (csv, json, xml 등)<br>

### 2. 도서 정보 조회 기능 (기본)

[V] (기본) 사용자는 도서의 ID 혹은 이름을 입력하여 도서의 정보를 조회 합니다.<br>
[V] (기본) 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함합니다.<br>
[V] (심화) 도서의 상태(대출 가능, 대출 중)가 표시됩니다.<br>
[V] (심화) 도서의 상태는 도서가 대출 가능한 상태인지, 대출 중인 상태인지를 나타냅니다.<br>
[] (심화) 도서가 대출 중인 상태인 경우, 도서의 대출 정보를 함께 출력합니다.<br>

### 3. 도서 대출 기능 (기본)

[V] (기본) 사용자는 콘솔을 통해 도서의 ID 혹은 이름을 입력하여 도서를 대출합니다.<br>
[V] (기본) 대출하면 도서의 상태를 대출중으로 변경합니다.<br>
[V] (심화) 대출중인 도서를 모두 출력합니다.<br>
[V] (심화) 도서가 이미 대출 중일 경우, 대출이 불가능하다고 출력합니다.<br>

### 4. 도서 반납 기능 (기본)

[V] (기본) 반납을 원하는 도서의 ID 혹은 이름을 입력하여 반납합니다.<br>
[V] (기본) 반납하면 도서의 상태가 대출 가능으로 변경됩니다.<br>

### 5. 대출 정보 조회 기능 (심화)
[V] 대출한 도서의 정보를 모두 조회할 수 있습니다.<br>
[] 대출 정보는 도서의 ID, 이름, 저자, 출판사, 대출 날짜, 반납일자로 구성됩니다.<br>
[] 대출 정보는 대출 날짜를 기준으로 내림차순으로 정렬됩니다.<br>

### 6. 종료 기능 (기본)

[V] 사용자는 프로그램을 종료할 수 있습니다.<br>


# 2-1. 미션 진행 내용 요약

일단 기본미션부터 주어진 내용을 확실히 구현하는것을 목표로 했습니다.<br>
중간에 select 문의 fetchall의 결과인 튜플이 분해가 생각대로 되지않아서 단순 문자 순서로 했습니다.
검색기능은 id로 검색하기와 제목으로 검색하기를 분리하였으며,
대출과 반납 기능은 검색기능을 기반으로 검색한 책 대여여부 정보를 바꿔주도록 했습니다.



# 2-2. 회고

*구현 과정에서 아쉬웠던 점 / 궁금했던 점을 정리합니다.*

(작성 TIP) 
추후 리팩토링 시, 어떤 부분을 추가적으로 진행하고 싶은지에 대해 구체적으로 작성해보시기 바랍니다. 