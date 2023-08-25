num1 = 100
num2 = 50

if(num1 > num2):
    print("비교 시작!")
    print("num1이 더 큽니다!")

# 위 방식은 아래와 같이 작동된다.

res = num1 > num2 # res는 result의 약자로 사용됨.

if(res):
    print("비교 시작!")
    print("num1이 더 큽니다!")

"""
- 설명 -
if() 함수의 사용 방법을 잘 생각해보면
if(조건문), 여기서 조건문이 참.
즉, True라는 boolean값의 조건이 충족되었을 때 실행된다.

위 코드에서 res의 값은 뭘까?
num1 > num2 라는 비교 연산을 해보니 True라는 boolen 값이 나오고,
이 값은 res로 들어간다.
조건문의 res가 True(라는 값을 가지고 있으므로)이므로 
조건이 실행되는 원리다.
if() 함수가 실행되는 원리에 대해 이해해보자!

그렇기에 if()문 안에는 boolean 값이 올수도 있고,
if(num1 > num2)와 같이 직접적인 조건문을 작성해주어도 된다.

"""

print(res)

if(True):
    print("무조건 실행됩니다!")
if(False):
    print("이건 절대로 실행이 안됩니다.")