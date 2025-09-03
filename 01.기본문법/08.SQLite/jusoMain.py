from function import *
from jusoDB import *



while True :
    menuPrint('주소관리')
    menu = input('메뉴선택>')
    if menu=='0':
        print("프로그램을 종료합니다.")
        break
    elif menu == '1': #입력
        p = Person()
        while True :
            p.name = input('이름>')
            if p.name == '' :
                print("이름을 입력하세요!")
                continue
            else :
                break
        while True :
            p.address = input('주소>')
            if p.address == '' :
                print("주소를 입력하세요")
                continue
            else :
                break
        insert(p)
        print("입력완료")
    elif menu == '2': #검색
        seq = inputNum('검색번호>')
        row = read(seq)
        if row == None :
            print("검색번호가 없습니다.")
        else :
            print(row)
            print("검색완료")

    elif menu == '3': #목록
        rows = list()
        for row in rows:
            person = Person()
            person.seq = row[0]
            person.name = row[1]
            person.address = row[2]
            person.print()
    elif menu == '4': #삭제
        seq = inputNum('삭제번호>')
        row = read(seq)
        if row == None :
            print("삭제번호가 없습니다.")
        else :
            sel = input(f'{row}를 삭제하시겠습니까? (y or Y)')
            if sel == 'y' or sel=='Y' :
                delete(seq)
                print("삭제완료")

    elif menu == '5': #수정
        p = Person()
        p.seq = inputNum('수정번호>')
        row = read(p.seq)
        if row == None :
            print('수정할 번호가 없습니다.')
        else :
            sel = input(f'{row}를 수정하시겠습니까? (y or Y)')
            if sel == 'y' or sel=='Y' :
                p.name = input('이름수정>')
                p.address = input('주소수정>')
                update(p)
                print("수정완료")