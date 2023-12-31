# 또다른 반복문
# for
# for 반복문은 특징이 있는데, 이 특징을 잘 알아야 적재적소에서 while, for를 선택하여 쓸 수 있다.

dataList = ["치킨", "피자", "햄버거"]

# 위와 같은 데이터 리스트가 있다고 했을 때, 리스트의 모든 요소를 출력하는 코드를 짠다고 해보자

print(dataList[0])
print(dataList[1])
print(dataList[2])

# 좋다. 위와 같이 출력할 수 있다. 하지만 리스트의 요소가 100개, 1000개라면?
# 비효율적이다...

print()
input("while 반복문을 사용한 코드를 보려면 Enter를 눌러주세요.")
print()

# while 반복문을 사용해서도 출력할 수 있다.
count = 0
while (count < len(dataList)):
    print(dataList[count])
    count = count + 1   # 무한반복문이 되지 않으려면 꼭 넣어주어야한다.

# 하지만 위와 같은 상황은 for문이 훨씬 효율적이다.
# for문을 이용해보자.

print()
input("for 반복문을 사용한 코드를 보려면 Enter를 눌러주세요.")
print()

# for 반복문
for food in dataList:
    print(food)
# 완성...
# 문법을 자세히 알아보자.


"""
< for 문법 >
for "새로운 변수명 지정" in "리스트":
    실행할 명령 

위와 같이 사용한다.
새로운 변수명은 for 안에서 사용할 변수를 말하는 것이고, 새로 만들어 주면 된다.
뒤에는 리스트가 온다.
그리고 새로운 변수와 리스트 사이에 "in"을 꼭 써준다.

위 반복문은 이렇게 돌아간다.
1. 리스트의 첫 요소를 꺼내서 새로운 변수에 할당한다.
2. 반복문 내부에서 새로운 변수를 사용하며 명령을 실행한다.
3. 리스트에서 꺼내온 다음 요소를 꺼내 다시 새로운 변수에 할당한다.
2-3 반복
4. 더이상 꺼낼 데이터가 없다면 종료한다.

"""


# 그렇다면 응용해서
# while이 아닌, for문을 이용해서 1~10까지 출력하는 프로그램을 만들어보자.

print()
input("for 반복문을 사용한 1~10까지 출력하는 코드 결과를 보려면 Enter를 눌러주세요.")
print()

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numList:
    print(num)

# 나름 잘 만들었다. 그런데 1~100 아니면 1000까지 출력한다고 하면 리스트에 다 넣을 건가...?
# 그래서 for에서 많이 사용하는 "range" 함수를 소개한다.

print()
input("range를 사용한 1~100까지 출력하는 코드 결과를 보려면 Enter를 눌러주세요.")
print()

numList = range(1, 101) # range를 사용하면 시작과 끝범위까지 리스트를 만들어준다.

for num in numList:
    print(num)

# ??? : 왜 100까지 하는데 101이라고 한거죠?
# python 에서는 끝 범위를 지정할 때 "끝 숫자 - 1"까지 받기 때문에, 
# 이런 사항도 고려를 해야한다.
# range(시작, 끝) -.> 시작 부터 끝-1 까지
# for문에 냅다 range를 박아 넣을 수도 있다. (굳이 변수를 쓸 필요 없음)

print()
input("range를 사용한 1~10까지 출력하는 코드 결과를 보려면 Enter를 눌러주세요.")
print()

for num in range(1, 11):
    print(num)

# 이제 슬슬 눈치쳈을 수 있다. for문은 실행해야할 명령의 횟수가 정해져 있는 경우 굉장히 유용하다.
# 리스트의 내용을 출력하는 방식으로 사용할 수도 있지만,
# 리스트의 크기만큼 반복한다는 사실도 알 수 있다.
# 그렇다면 이를 이용해서 "hello"라는 문장을 10번 출력해보자.

print()
input("for를 이용해 hello를 10번 출력하는 코드 결과를 보려면 Enter를 눌러주세요.")
print()

for i in range(1, 11):
    print("Hello")