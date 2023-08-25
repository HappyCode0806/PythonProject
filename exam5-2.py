# exam5-1.py 의 마지막 예제에 break
# break와 같이 자주 사용하는 함수가 있는데,
# 바로 continue이다

while (True):
    num = int(input("숫자를 입력해주세요 : "))

    if(num == 0):
        print("0을 입력하셨네요!")
        continue    # continue를 사용하면 이후 실행될 코드들을 읽지 않고 반복문 처음으로 돌아가 다시 실행한다.

    print("0을 입력해주세요.")

print("입력한 숫자는 " + "num" + "입니다.")
