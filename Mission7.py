# 함수를 만들 수 있게 되었으니
# 재미난 미션을 해보자.
# < up down 게임을 만들어라 >
# 지금까지 배웠던 것들을 모두 활용해보자.

# Hint 반복문, 조건, 함수 - 필요한 만큼 사용해보자.

# [ 조건 ]
# 사용자에게 입력을 받을 것
# 5회 안에 맞출 것 (이 이상은 실패)

com_num = 86 # 컴퓨터에 정해둔 임의의 (맞춰야 하는) 숫자

print("<< Up Down Game >>")
print("- 5회 안에 맞춰야하며 숫자를 입력하면 더 커야하는지 작아야하는지 알려줍니다.")
print("- 정답에 도전하세요!")

# 비교 함수 생성
def compare(user_num, com_num): # 유저의 숫자와 컴퓨터의 숫자를 인자로 사용
    if(user_num < com_num):
        print("Up!")
    elif(user_num > com_num):
        print("Down!")
    else:   # 정답일 경우 True라는 값을 반환하여 정답임을 알림
        return True

life = 5

while (life > 0):   # 기회가 0보다 클 경우 반복함.
    print("==================================")
    print("남은 기회는 {}회 입니다.".format(life))
    try:    # 숫자 이외의 값을 입력했을 경우(입력 과정에서 오류 발생 시)
        user_num = int(input("숫자를 입력해주세요! > "))    # 입력받은 숫자를 유저변수에 넣음
    except: # 오류 사항을 지적, 반복문 처음으로 돌아감
        print("문자가 아닌 숫자를 입력해주세요!")
        continue

    GameResult = compare(user_num, com_num) # 게임의 결과를 받아옴. 맞췄을 떄 반복문을 탈출하기 위함.
                 # 두 수의 일치를 비교하는 함수를 사용

    if(GameResult): # 비교 함수에서 정답신호(True)가 나왔다면
        print("딩동댕~! 정답입니다!")
        exit()

    life = life - 1 # 기회를 하나씩 사용함.

print()
print("다음 기회에...")
print(">>> Game Over <<<")  # 반복문의 조건이 거짓이 되어 반복문이 끝났을 경우 == 게임 종룐

# + 여기서 더 나아가서, 게임이 끝났을 경우 재시도를 권유
# Yes 를 입력하면 다시 시작, No를 입력하면 게임 종료
# 이런식으로 게임의 완성도를 높여나가 보자.

# Mission7의 업다운 게임 프로젝트를 통해 다양한 바리에이션들을 만들어보면 좋을 것 같다.
# 컴퓨팅적 사고나 코딩이 즐거워 질지도..?

# ex) 배팅, 보상 시스템을 넣어서 (user_coin) 누가누가 잘 맞추고 코인을 많이 벌었는지와 같이
# (틀리면 잃고, 맞추면 얻는 방식)
# 다양한 버전의 게임을 한번 만들어봤으면 좋겠다.
