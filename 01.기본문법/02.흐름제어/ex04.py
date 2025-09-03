#1~100 합계
tot = 0
for j in range(1, 101):
    tot += j

print(tot)

#2~100 짝수합계
k1 = 0
for i in range(2, 101, 2) :
    k1 += i
print(k1)
#1~99 홀수 합계
k2 = 0
for i in range(1, 100, 2) :
    k2 += i
print(k2)