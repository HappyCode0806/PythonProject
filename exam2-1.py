#datatype

name = "leeseungwon"
num1 = 1
float1 = 1.5

print(type(name))
# type() 함수 : 함수 안에 숫자, 문자, Boolean, 변수 등을 넣으면 해당 타입을 반환해 준다.
# str 문자열

typenum = type(num1)
print(typenum)
# int 정수

print(type(float1))
# float 실수(소수)

testnum = 1
teststr = "1"

# print(testnum + teststr)
# "지원하지 않는 연산" 오류 발생, 다른 데이터 유형끼리 연산은 할 수 없으니 내가 쓰는 데이터의 유형은 항상 잘 체크하자

######################################################
# Bool : Boolean
# 참과 거짓 : True, False - True와 False 자체가 정수, 문자열과 같은 데이터 타입이므로 쌍따옴표(")를 하지 않아도 된다."
#              1     0

data = True
print(type(data))
# 결과 : <class 'bool'>

# 위에 기록해둔 것처럼, True는 1, False는 0 으로 표현, 사용이 가능하다. 이때문에 재미난 연산이 가능해진다

data1 = True
data2 = 3

print(data1 + data2)
# 결과 값 : 4

"""
* 비교 연산자

data1 = 1
data2 = 1

print(data1 + data2) - 덧셈 연산
print(data1 == data2) - 비교 연산

print(type(data1 == data2))
-> 결과 값 : <class 'bool'>

"""