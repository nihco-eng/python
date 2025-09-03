#새로운 코드를 생성하는 함수 
def newCode(list) :
    if len(list) == 0 :
        return 1
    
    codes = []
    for s in list :
        codes.append(s['code'])
    return max(codes) + 1

def inputNum(title) :
    while True :
        num = input(f"{title}>")
        if num.isnumeric() :
            return int(num)
        elif num == "" :
            return num
        else :
            print("숫자로 입력하세요!")


def search(list, code) :
    for index, item in enumerate(list) :
        if item['code'] == code :
            return index 
        

#메뉴출력함수
def menuPrint(title):
    print(f"\n***************{title}******************")
    print("------------------------------------------")
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료")
    print("------------------------------------------")

#아이템 출력 함수
def itemPrint(item) :
    keys = item.keys()
    for key in keys :
        if isinstance(item[key], int) :
            print(f"{item[key]:,}", end ="\t")
        else :
            print(item[key], end="\t")
    print('\n-------------------------------------------')

if __name__ == '__main__' :
    sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':15000000, 'qnt':3},
    ]
    itemPrint(sale[1])