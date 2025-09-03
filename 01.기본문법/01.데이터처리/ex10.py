jumin = '990120-2155011'
gender = jumin[7]
result = gender == '1' or gender == '3'

print(f'{gender} 결과는 {result}')

yy=jumin[0:2]
print(yy)

mm=jumin[2:4]
print(mm)

dd=jumin[4:6]
print(dd)
print(f'{yy}년 {mm}월 {dd}일')
print(jumin[-7:])
print(jumin[-1:])