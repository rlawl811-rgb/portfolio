# 6. 반복문
'''
#3p 반복문 사용
for i in range(3):
    print("난생처음 파이썬은 재미있습니다.^^")

for i in range(0,3,1):
    print("난생처음 파이썬은 재미있습니다.^^")

for i in [0, 1, 2]:   #range 함수 없음
    print("난생처음 파이썬은 재미있습니다.^^")

for i in range(1,11,1):
    print(i,end=' ')

#9p 학생 줄 세우기
fact=1
friends_num=5
for i in range(1,friends_num+1,1):
    fact=fact*i
print("A, B, C, D, E 학생들의 순서대로 세우는 경우의 수 :",fact)

#12p for문을 활용하여 합계 구하기
i=1
hap=0
for i in range(1,11,1):
    hap+=i
print(hap)

#16p for문을 활용한 반복적인 덧셈
#1,000~2,000 사이 홀수 합
i,hap=0,0
for i in range(1001,2001,2):
    hap+=i
    
print("1000에서 2000까지의 홀수의 합: ",hap)

#21 구구단 계산기 만들기
i=0
k=0
for i in range(2,10,1):
    for k in range(1,10,1):
        print(i,"x",k,"=",i*k)
    print("")
    
#for문 vs while문
for i in range(0,3,1):
    print(i,": 난생처음 파이썬은 재미있습니다.")

i=0
while (i<3):
    print(i,": 난생처음 파이썬은 재미있습니다.")
    i+=1   #강제로 1을 증가시키는 행을 추가해야 함

#30p 랜덤값 추출
import random
random.randint(1,45)
random.choice(["김밥","라면","떡볶이","순대","오뎅"])

for i in "Hello":
    print("i=",i)

while True:
    print("ㅎ",end=" ") #강제중지 ctrl+c

#30p while 무한반복
hap=0
num1,num2=0,0
while True:
    num1=int(input("숫자1 ==>"))
    num2=int(input("숫자1 ==>"))
    hap=num1+num2
    print(num1,"+",num2,"=",hap)


for i in range(1,1001,1):
    print("반복문을",i,"회 실행합니다")
    break

#32p 반복문을 탈출하는 break문
hap = 0
num1, num2 = 0
while True :
    num1 = int(input("숫자1 ==> "))
    if num1 == 0:
        break
    num2 = int(input("숫자2 ==> "))

    hap = num1+num2
    print(num1,"+",num2,"=",hap)

print("0을 입력해서 계산을 종료합니다.")

#34p 처음으로 돌아가는 continue문
i, hap = 0,0

for i in range(1,101,1):
    if i%4 == 0:
        continue

    hap+=i

print("1~100의 합계(4의 배수 제외) : ", hap)

#38 주사위 3개 동시에 던져 동일한 숫자 나오기
import random
count = 0
dice1, dice2, dice3 = 0,0,0

while True :
    count+=1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    if(dice1 == dice2) and (dice2 == dice3):
        break
print("3개 주사위는 모두",dice1,"입니다.")
print("같은 숫자가 나오기까지", count,"번 던졌습니다.")

#40p 컴퓨터와 인간의 숫자 맞히기 대결
import random

computer, user = 0,0

for i in range(1,11,1):
    computer = random.randint(1,5)
    print("게임",i,"회:",end='')
    user = int(input("컴퓨터가 생각한 숫자는 ?"))
    if computer == user:
        print("맞혔네요. 축하합니다!!")
    else:
        print("아까워요. ",computer, "였는데요. 다시 해보세요.ㅠ")
print("게임을 마칩니다")
            

#43p 사용자 암호 입력 후 로그인하기
password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오:")
print("**로그인 성공**")

#45p 사용자 입력 기반 사칙연산

print("1)덧셈 2)뺄셈 3)곱셈 4)나눗셈")
calcul = int(input("어떤 연산을 원하는 지 번호를 입력하세요:"))
if 1<= calcul <= 4:
    print("연산을 원하는 숫자 두개를 입력하세요")
    num1 = int(input())
    num2 = int(input())
    cal_aft=0

    if calcul == 1:
        cal_aft = num1+num2
        print(num1,"+",num2,"=",cal_aft)
    elif calcul == 2:
        cal_aft = num1-num2
        print(num1,"-",num2,"=",cal_aft)
    elif calcul == 3:
        cal_aft = num1*num2
        print(num1,"*",num2,"=",cal_aft)
    elif calcul == 4:
        cal_aft = num1/num2
        print(num1,"/",num2,"=",cal_aft)
else:
    print("잘못 입력하셨습니다")
'''   
#47p 삼각형 별 만들기
num = int(input("숫자를 입력하세요:"))
for i in range(1,num+1):
    print('*'*i)

num = int(input("숫자를 입력하세요:"))
for i in range(1,num+1):
    print(' '*(num-i)+'*'*i)

#48p 사용자 입력 반복 연산
    
