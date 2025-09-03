from function import *
from jusoFile import *

def newSeq():
    list = fileread()
    if len(list) == 0 : return 1
    seqs = [p.seq for p in list]
    return max(seqs) + 1

def searchSeq(seq):
    list = fileread()
    result = [p for p in list if p.seq==seq]
    if len(list) > 0 : return result[0]

while True :
    menuPrint('주소관리')
    menu = input('메뉴선택>')
    if menu == "0" :
        print("프로그램을 종료합니다.")  
        break
    elif menu == "1" : #입력
        person = Person()
        person.seq = newSeq()
        print(f"번호>{person.seq}")
        if person.seq =='' : continue 
        person.name = input("이름>")
        if person.name == '' : continue
        person.address = input("주소>")
        fileAppend(person)
        person.print()
    elif menu == "3" : #목록
        list = fileread()
        for person in list :
            person.print()
    elif menu == "4" : #삭제
        seq = inputNum("삭제번호>")
        list = fileread()
        result = [p for p in list if p.seq == seq]
        if len(result) == 0:
            print('삭제할 번호가 없습니다.')
            continue
        person = result[0]
        person.print()
        sel = input('삭제하실래요?(Y or y)>')
        if sel == 'Y' or sel =='y' :
            result = [p for p in list if p.seq!=seq]
            fileWrite(result)
            print("삭제성공!")
    elif menu == "5" : #수정 
        seq = inputNum("수정번호>")
        list = fileread()
        result = [person for person in list if person.seq==seq]
        if len(result) == 0 :
            print("검색 결과가 없습니다.")
            continue
        person = result[0]
        person.print()
        sel = input('수정하실래요?(Y or y)>') 
        if sel == 'Y' or sel == 'y' :
              name = input(f'이름:{person.name}>')
              if name != "" : person.name = name 
              address = input(f'주소:{person.address}>')
              if address != "" : person.address = address
              fileWrite(list)
              print("수정완료!")
    elif menu == "2" : #검색
        while True :
            value = input('검색어>')
            if value == '' : break 
            list = fileread()
            result = [p for p in list if (p.name.find(value) != -1) or (p.address.find(value) != -1)]
            if len(result) == 0 : 
                print("검색 내용이 없습니다.")
                continue
            for person in result : 
                person.print()
                print("검색완료!")