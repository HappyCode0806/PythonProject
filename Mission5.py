# 지금까지 배웠던 것들을 이용하여 "simple shell"을 만들어 보자.

"""
< 조건 >
1) 사용자로부터 명령어를 입력받는다.
2) 사용자가 받은 명령어를 출력해본다. ex) "@@" 명령어를 실행했습니다.
3) 위 사항을 무한히 반복할 것
4) exit 라고 사용자가 입력하면, 프로그램 종료
5) 명령어가 10글자 이상이면 -> "잘못됐어요!" 라는 문구 출력 // 문자열의 길이를 확인하는 방법은 len() 함수를 사용하면 됨!
"""

# 내가 만든 코드
while (True):
    print("-- simple shell --")
    try:
        command = input("> ")
        if(len(command) >= 10):
            print("잘못됐어요!")
        elif(command == "exit"):
            break
        else:
            print(command + " 명령어를 실행했습니다.")

    except:
        print("잘못 입력하셨습니다.")

print()
input("프로그램이 종료되었습니다. 예시 답안의 코드 결과를 확인하시려면 Enter키를 눌러주세요.")
print()

# 예시 답안 , if 2개만으로 끝내버렸네...

print("[+] Simple Shell")

while (True):
    cmd = input("> ")

    if(cmd == "exit"):
        break

    if(len(cmd) > 10):
        print("[+] 잘못된 명령어입니다.")
        continue # continue까지 사용함!

    print(cmd + " 가 실행되었습니다.")
