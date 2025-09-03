from function import *
from productFile import *


def newCode():
    list = fileread()
    if len(list) == 0 : return 1
    codes = [p.code for p in list]
    return max(codes) + 1


while True :
    menuPrint('상품관리')
    menu = input('메뉴선택:')
    if menu == '0' : break
    
    elif menu == '1' :
        product = Product()
        product.code = newCode()
        print(f"번호>{product.code}")
        if product.code =='' : continue 
        product.name = input("이름>")
        if product.name == '' : continue
        product.price = int(input("가격>"))
        fileAppend(product)
        product.print()
    
    elif menu == '2' :
        while True :
            value = input('검색어>')
            if value == '' : break 
            list = fileread()
            result = [p for p in list if (p.name.find(value) != -1) or (p.price.find(value) != -1)]
            if len(result) == 0 : 
                print("검색 내용이 없습니다.")
                continue
            for product in result : 
                product.print()
                print("검색완료!")
   
    elif menu == '3' :
        sort = inputNum('1.코드순|2.이름순|3.최저가|4.최고가>')
        if sort == '' : break
        list = fileread()
        result = []
        if sort == 1 : result = sorted(list, key=lambda p:p.code)
        elif sort == 2 : result = sorted(list, key=lambda p:p.name)
        elif sort == 3 : result = sorted(list, key=lambda p:p.price)
        elif sort == 4 : result = sorted(list, key=lambda p:p.price, reverse=True)
        print()
        for p in result :
            p.print()
    
    elif menu == '4' :
        code = inputNum("삭제번호>")
        list = fileread()
        result = [p for p in list if p.code == code]
        if len(result) == 0 :
            print("삭제할 상품이 없습니다.")
            
            continue
        product = result[0]
        product.print()
        sel = input('삭제하시겠습니까? (Y or y)')
        if sel == 'y' or sel == "Y" :
            result = [p for p in list if p.code != code]
            fileWrite(result)
            print("삭제완료!")
    
    elif menu == '5' :
        code = inputNum("수정코드>")
        list = fileread()
        result = [p for p in list if p.code == code]
        if len(result) == 0 :
            print("수정할 상품이 없습니다.")
            continue
        p= result[0]
        p.print()
        sel = input('수정하시겠습니까? (Y or y)')
        if sel == 'y' or sel == "Y" :
            p.name = input('수정이름>')
            p.price = int(input('수정가격'))
            fileWrite(list)
            print("수정완료!")
    
    else : 
        print('0~5 숫자를 입력하세요!')