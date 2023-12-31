# 크기가 작다고 출력하고 싶다면 어떻게 해야할까

num1 = 10
num2 = 50

if(num1 > num2):
    print("num1이 더 큽니다!")

print("num1이 더 작습니다!")

# 결과 값 : num1이 더 작습니다!

# 얼핏 보기에 성공한 코드 처럼 보인다. 하지만 다음 코드를 실행시켜보자

input("다음 코드를 실행시키려면 Enter키를 눌러주세요.")
print()

num1 = 100 # 10 -> 100 , num1이 더 큰 상황
num2 = 50

if(num1 > num2):
    print("num1이 더 큽니다!")

print("num1이 더 작습니다!")

# 결과 값 : num1이 더 큽니다!
#          num1이 더 작습니다!

# 조건에 맞지 않으면 실행되지 않는 다는 점을 이용하여 크기를 비교해보자.

input("다음 코드를 실행시키려면 Enter키를 눌러주세요.")
print()

# 이번에는 숫자를 입력받아 크기를 비교해 보자.

num1 = int(input("num1에 넣을 숫자를 입력해주세요 : ")) # input() 함수는 str(문자열) 형태로 받기 때문에
num2 = int(input("num2에 넣을 숫자를 입력해주세요 : ")) # 비교를 위해서는 int형으로 형변환을 시켜줘야 한다.

if(num1 > num2):
    print("num1이 더 큽니다!")
if(num1 < num2):
    print("num1이 더 작습니다!")

# 위 코드 처럼 if를 2번 사용해도 작동은 된다. 하지만 효율이 떨어진다.
# if문을 참이든 거짓이든 검사를 꼭 하기 때문에, if문이 많아지면 그만큼 시간이 오래걸린다.
# 이때 사용하는게 if문과 같이 사용하는 else 문이다.

# else문은 뒤에 따로 조건이 붙지 않는다. 그러면 언제 실행되는걸까?
# 바로 if문에서 어떠한 조건도 해당되지 않을 때 실행된다.

input("다음 코드를 실행시키려면 Enter키를 눌러주세요.")
print()

num1 = int(input("num1에 넣을 숫자를 입력해주세요 : ")) # input() 함수는 str(문자열) 형태로 받기 때문에
num2 = int(input("num2에 넣을 숫자를 입력해주세요 : ")) # 비교를 위해서는 int형으로 형변환을 시켜줘야 한다.

print("else를 사용한 결과에요.")

if(num1 > num2) :
    print("num1이 더 큽니다!")
else :   # num1과 num2를 비교했을 떄 if문이 거짓이라면 당연히 num1이 더 작을테니 이런 조건문도 가능하다.
    print("num1이 더 작습니다!")

# 하지만 크지 않다고 해서 무조건 작은게 아니다.
# 똑같을 수 있기 때문이다. 그렇기에 조건을 하나 더 넣고 싶다.

# 여기에 또 하나의 조건문을 넣고 싶으면 어떻게 해야할까?
"""
if(num1 > num2) :
    print("num1이 더 큽니다!")
else :
+   if(머시기 머시기...)
    print("num1이 더 작습니다!")
"""
# 위 주석처리된 코드처럼 else에 if 문을 또 사용하면 되지 않을까?
# 하지만 이렇게 코드를 작성하면 코드가 지저분해진다.
# 이때 또다른 조건을 추가하는 방법은 바로 elif문을 사용하는 것이다.

# elif문은 if 조건에 맞지 않을 경우 실행되는 조건문으로, 다른 조건을 확인하는거기에 elif(조건문) 형식으로 작성해야한다.

input("다음 코드를 실행시키려면 Enter키를 눌러주세요.")
print()
print("elif 조건까지 사용한 결과입니다.")

num1 = int(input("num1에 넣을 숫자를 입력해주세요 : ")) # input() 함수는 str(문자열) 형태로 받기 때문에
num2 = int(input("num2에 넣을 숫자를 입력해주세요 : ")) # 비교를 위해서는 int형으로 형변환을 시켜줘야 한다.

if(num1 > num2):
    print("num1이 더 큽니다!")
elif(num1 == num2):    # num1과 num2를 비교했을 때 같을 수 있기에 또 다른 조건을 확인할 수 있도록 했다.
    print("num1과 num2가 같습니다!")
else:    # num1과 num2를 비교했을 떄 if문과 elif문의 조건이 모두 거짓이라면 당연히 num1이 더 작을테니 이런 조건문이 가능하다.
    print("num1이 더 작습니다!")

"""
이로써 조건문을 전부 배웠다.

조건문은

if(조건문):
    명령문
elif(조건문):
    명령문
else:
    명령문

과 같은 형식으로 작성된다.
"""