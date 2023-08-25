#UpDwon Game
import random

print("[ UpDown Game ]")
print("- made in Seungwon -")

name = input("이름을 입력해주세요. > ") # 유저 이름 받아서 사용

print()
print("{}님 반갑습니다.".format(name))

def level_choice(): # 난이도를 선택하는 함수, 난이도를 선택하면 그에 맞는 기회(life)를 반환 시켜주는 함수이다.
    life = 0
    while(True):
        print()
        print("난이도를 선택해주세요.")
        level = input("1. 쉬움\n2. 보통\n3. 어려움\n난이도의 숫자 또는 문자를 입력하여 선택해주세요 > ")
        if(level == "1" or level == "쉬움"):
            level = "쉬움"
            life = 15
            print("{}는 기회가 15번 주어집니다.".format(level))
        elif(level == "2" or level == "보통"):
            level = "보통"
            life = 10
            print("{}는 기회가 10번 주어집니다.".format(level))
        elif(level == "3" or level == "어려움"):
            level = "어려움"
            life = 5
            print("{}는 기회가 5번 주어집니다.".format(level))
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            continue

        choice = input("{} 난이도로 하시겠습니까? [ Y / N ] > ".format(level))
        if(choice == "Y" or choice == "y"):
            return life
        elif(choice == "N" or choice == "n"):
            continue
        else:
            print("잘못 입력하셨습니다. 난이도 선택으로 돌아갑니다.")
            continue

life = level_choice() # 난이도 선택 후 선택한 난이도에 맞는 기회를 변수에 넣고 게임 시작

print()
print("게임을 시작합니다!")
print()
print("* 게임 룰 *")
print("- 컴퓨터가 1에서 100까지의 숫자중 무작위로 숫자 하나를 선정합니다.\n선택하신 난이도의 기회 만큼 숫자를 부를 수 있고, 컴퓨터는 입력한 숫자가 정답 숫자보다 커야하는지 작아야하는지 알려줍니다.")
print("기회를 전부 사용시 게임이 즉시 종료됩니다. 행운을 빕니다!")
print()

def compare(user, com): # 두 숫자를 비교하는 함수 (인자로 넣는 데이터를 이미 정수형태로 넣어줬기 때문에 형변환은 따로 안함)
    if(user > com):
        print("== Down! ==")
        return False
    elif(user < com):
        print("== Up! ==")
        return False
    else:    
        return True

com_num = random.randint(1,101) # 난수 생성(정수형태)

# print(com_num)  # 개발자용 정답 확인

while(True):
    print("{}님! 기회가 {}번 남았습니다! 신중하게 숫자를 입력해주세요!".format(name, life))
    try:
        user_num = int(input("> "))
    except:
        print("다시 입력해주세요.(숫자만 입력해주세요)")
        print()
        continue
    GameRes = compare(user_num, com_num)

    if(GameRes):
        print("정답입니다! 축하드립니다 ㅎㅎ")
        exit()
    else:
        life = life - 1

    if(life == 0):
        break

print("다음에 다시 도전하세요...")