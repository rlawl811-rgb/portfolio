
numList=[0,0,0,0,]
hap=0
numList[0]=int(input("숫자1: "))
numList[1]=int(input("숫자2: "))
numList[2]=int(input("숫자3: "))
numList[3]=int(input("숫자4: "))
hap=numList[0]+numList[1]+numList[2]+numList[3]
print("합계 ==> ",hap)

fact=1
friends_num=5
for i in range(1,friends_num+1,1):
    fact=fact*i

print("A,B,C,D,E 학생들을 순서대로 세우는 경우의 수:",fact)
    
i=0
gob=1
for i in range(1,11,1):
    gob=gob*i
    print(gob)

i=0
hap=0
for i in range(0,11,1):
    hap=hap+i
print(hap)

i,hap=0,0
for i in range(1001,2000,2):
    hap=hap+i
    print("1000에서 2000까지 홀수의 합:",hap)

i,hap=0,0
for i in range(500,1001,2):
    hap+=i
print(hap)

for i in range(3):
    for k in range(2):
        print("난생처음은 쉽습니다.^^(i값:",i,"k값:",k,")")

for i in range(2,10,1):
    for k in range(1,10,1):
        print(i,"x",k,"=",i*k)

import random
count=0
dice1,dice2,dice3=0,0,0
while True:
    count+=1
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    if dice1==dice2==dice3:
        break
print("3개 주사위는 모두",dice1,"입니다.")
print("같은 숫자가 나오기까지",count,"번 던졌습니다.")

import random
count=0
for count in range(0,10,1):
    count+=1
    computer=random.randint(1,5)
    print("게임",count,"회",end="")
    human=int(input("컴퓨터가 생각한 숫자는?"))
    if computer == human:
        print("맞혔네요. 축하합니다!!")
        break
    else :
        print("아까워요.",computer,"였는데요. 다시 해보세요.ㅠ")

num1,num2,num3,num4=0,0,0,0
hap=0
num1=int(input("숫자 : "))
num2=int(input("숫자 : "))
num3=int(input("숫자 : "))
num4=int(input("숫자 : "))
hap=num1+num2+num3+num4
print("합계 ==> ",hap)

numList=[0,0,0,0]
hap=0
numList[0] = int(input("숫자 : "))
numList[1] = int(input("숫자 : "))
numList[2] = int(input("숫자 : "))
numList[3] = int(input("숫자 : "))
hap=numList[0]+numList[1]+numList[2]+numList[3]
print("합계 ==> ",hap)

numList=[]
for i in range(0,4):
    numList.append(0)
hap=0
for i in range(0,4):
    numList[i] = int(input("숫자 : "))
hap=numList[0]+numList[1]+numList[2]+numList[3]
print("합계 ==> ",hap)

import random
wisesay=('티끌모아태산'
               ,'삶이 있는 한 희망은 있다'
               ,'언제나 현재에 집중할 수 있다면 행복할 것이다.'
               ,'피할 수 없으면 즐겨라'
               ,'내일은 내일의 태양이 뜬다')
#today=random.choice(wisesay) #random.choice / random.randint 두 방법 가능
#print("오늘의 명언 ==> ",today)
today=random.randint(0,len(wisesay)-1)
print("오늘의 명언 ==> ",wisesay[today])

numList=[10,20,30]
numList[0]=100  #리스트값 변경
numList[1:2]=[150,200]
print(numList)

populatin=['Seoul',9765,'Busan',3441,'Incheon',2954]
print("서울 인구:",populatin[1])
print("인천 인구:",populatin[-1])
cities=populatin[0::2]
popu_2=populatin[1::2]
print("도시 리스트: ",cities)
print("인구의 합: ",sum(popu_2))

#리스트의 메소드들
numList=[10,20,30,40] 
numList.index(10)       #인덱스 위치 찾기
numList.append(10)      #리스트끝에 값 추가
numList.insert(1,123)   #리스트 값 삽입. insert(위치,값)
numList.extend([50,60]) #리스트를 기존 리스트 끝에 삽입
del(numList[1])         #인덱스로 삭제
numList.remove(10)      #값으로 삭제. 중복된 모든값x, 최초값만 삭제.
del(numList)            #리스트 전체 삭제
numList.pop()           #제일 뒤 값 뽑아내서 삭제
print(numList)

#any,all(0,공백문자열 false)
a_list=[10,20,30]
b_list=[0,10,20,30]
c_list=[0,""]
               
any(a_list),any(b_list),any(c_list)
all(a_list),all(b_list),all(c_list)
#오름차순정렬 sort, 내림차순정렬 sort(reverse=True)
numList.sort()
numList.sort(reverse=True)
#리스트 반전
numList.reverse()
#리스트 복사
numList2 = numList.copy()

aList=['Kim','Park','Lee','Hong']
bList=aList #id같음. 변경시 함께 반영

aList=['Kim','Park','Lee','Hong']
bList=list(aList) #id다름. 변경시 미반영

#심사위원 점수 결과 구하기
print("홍길동 선수 경기 끝났습니다~~ 짝짝짝")
score=[]
for i in range(5):
    jumsu= int(input("평가 점수 ==> "))
    score.append(jumsu)
hap=0
for i in range(5):
    hap+=score[i]

print("심사위원 평가 점수 : ",hap/5)

#리스트 함축
[x for x in range(10)]
[x**2 for x in range(10)] #0에서 9까지 숫자의 제곱 값
st='Hello World'
[x.upper() for x in st] #문자열 각각에 대해 upper() 메소드 적용

a=['welcome','to','the','python','world']
first_a = [s[0].upper() for s in a] #첫 알파벳에 대한 대문자 변환
print(first_a)

s=["Hello","12345","World","67890"]
numbers=[x for x in s if x.isdigit()] #숫자만 반환
print(numbers)

#숫자쪼개기
[int(x) for x in input('정수를 여러개 입력하세요 : ').split()]
#숫자만 뽑아서 쪼개기
[int(x) for x in input('정수를 여러개 입력하세요 :').split() if x.isdigit()]

