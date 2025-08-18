#7.리스트
'''
#5p 리스트생성
numList = [0, 0, 0, 0]
hap = 0
numList[0] = int(input("숫자 : "))
numList[1] = int(input("숫자 : "))
numList[2] = int(input("숫자 : "))
numList[3] = int(input("숫자 : "))
hap = numList[0] + numList[1] + numList[2] + numList[3]
print("합계 ==> " ,hap)

#8p 리스트를 하나씩 추가하기
numList=[]
numList.append(0)
numList.append(0)
numList.append(0)
numList.append(0)
print(numList)

#9p for문을 활용한 리스트 값 추가
numList=[]
for i in range(0,4):
    numList.append(0)
print(numList)

#10p for문을 활용한 리스트에 값 대입
numList = []
for i in range(0,4):    #리스트자리 만드어주기
    numList.append(0)
hap = 0

for i in range(0,4):
    numList[i] = int(input("숫자:"))

hap = numList[0]+numList[1]+numList[2]+numList[3]
print("합계 ==>",hap)

#15p 리스트 값 접근하기
numList = [10,20,30,40,50]
print(numList[2:])
print(numList[:2])
print(numList[:])       #처음부터 끝까지
print(numList[::2])     #처음부터 끝까지 step만큼 건너뛰기

#18p 리스트 덧셈과 곱셈
numList = [10,20,30]
myList = [40,50,60]

print(numList + myList)     #리스트 요소들이 합쳐짐
print(numList * 3)          #곱한 횟수만큼 리스트 반복

#22p 오늘의 명언 랜덤 출력
import random
wisesay=('티끌모아태산'
               ,'삶이 있는 한 희망은 있다'
               ,'언제나 현재에 집중할 수 있다면 행복할 것이다.'
               ,'피할 수 없으면 즐겨라'
               ,'내일은 내일의 태양이 뜬다')
#today=random.randint(0,len(wisesay)-1)
#print("오늘의 명언 ==> ",wisesay[today])
today=random.choice(wisesay) #random.choice / random.randint 두 방법 가능
print("오늘의 명언 ==> ",today)

#25p 리스트값 변경
numList=[10,20,30]
numList[0]=100  
numList[1:2]=[150,200]
print(numList)

#27p 리스트 값 슬라이싱
populatin=['Seoul',9765,'Busan',3441,'Incheon',2954]
print("서울 인구:",populatin[1])
print("인천 인구:",populatin[-1])
cities=populatin[0::2]
popu_2=populatin[1::2]
print("도시 리스트: ",cities)
print("인구의 합: ",sum(popu_2))

# 29p 리스트 값 삽입/삭제/개수 세기
numList = [10,20,30]
numList.append(123)
print(numList)
numList.insert(1,456)
print(numList)
del(numList[1])
print(numList)
del(numList)        #전체 삭제 됨
print(numList)

numList = [10,20,30]
numList.remove(10)
print(numList)
'''
numList = [10,20,30,10,10]
numList.remove(10)      #중복된 모든값이 아닌, 첫번째 값만 삭제
print(numList)
numList.count(10)       #찾을 값이 몇개인지 확인
numList.index(30)       #인덱스 위치 찾기, 중복이면 첫번째값만
numList.extend([50,60]) #리스트를 기존 리스트 끝에 삽입
print(numList)
numList.pop()           #제일 뒤 값 뽑아내서 삭제
len(numList)
sum(numList)
max(numList)
min(numList)

#36p any,all(0,공백문자열 false)
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
