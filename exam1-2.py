#calc
print("calc")

num1 = input("숫자를 입력해주세요 : ") # 입력 값 1
num2 = input("숫자를 입력해주세요 : ") # 입력 값 1

print(num1+num2)
#출력 결과 : 11

"""
input() 함수는 입력 받은 datatype이 chracter, string(문자열)이다. python은 문자열 + 문자열을 했을 경우 
두 문자를 서로 이어주기 때문에 11이 나오게 된 것이다.
그렇다면 이를 숫자로 계산되게 하려면 어떻게 해야할까.
"""

num1 = int(num1)
num2 = int(num2)
# 위와 같이 형 변환 함수를 사용하면 된다. int() - 정수, float() - 실수, str() - 문자열

print(num1 + num2)
#출력 결과 : 2

"""
위 처럼 변수의 형태를 변환하여 다시 그 변수에 할당할 수도 있지만
num1 = int(input("숫자를 입력해주세요 : "))
위 코드처럼 입력을 받고 바로 형변환을 한 뒤 변수에 할당해 줄 수 있다.
"""