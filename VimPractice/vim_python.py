print("hello world!")

print()

while(True):
    print("[ Simple Shell ]")
    try:
        user_com = input("> ")
    except:
        print("오류가 발생했습니다. 올바른 명령어를 입력해주세요")
        continue
    if(user_com == "exit"):
        break
    elif(len(user_com) > 15):
        print("명령어를 다시 입력해주세요.")
    else:
        print("{}를 실행했습니다.".format(user_com))
    print("========================")

        




