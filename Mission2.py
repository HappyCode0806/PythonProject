# 프로그램을 실행해보고 그 결과를 똑같이 나오도록 코딩 해보자. (리스트를 이용할 것)

# 코딩에 정답은 없다.

# 1번 답안================================================================
userInfo = ['', '']

userInfo[0] = input("이름을 말씀해주세요 : ")

print("안녕하세요~! 좋은 아침입니다! "+ userInfo[0] +"님!")
print("저는 과일 좋아하는데!")

userInfo[1] = input("좋아하는 과일 있으세요? : ")

print("아하~ " + userInfo[1] + "라는 과일을 좋아하시는군요!")
print("제가 바로! " + userInfo[1] +" 준비해드리겠습니다!")



# 2번 답안 ================================================================
dataList = []
userName = input("이름을 말씀해주세요 : ")

dataList.append(userName)

print("안녕하세요~! 좋은 아침입니다! " + dataList[0] + "님!")

print("저는 과일 좋아하는데!")

userFruit = input("좋아하는 과일 있으세요? : ")

dataList.append(userFruit)

print("아하~ " + dataList[1] + "라는 과일을 좋아하시는군요!")
print("제가 바로! " + dataList[1] + "준비해드리겠습니다!")
