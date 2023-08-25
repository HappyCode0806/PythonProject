# 프로그램을 실행해보고 그 결과를 똑같이 나오도록 코딩 해보자. (사전형(Dictionary)를 이용할 것)

# 코딩에 정답은 없다.

userDictionary = {}

userDictionary["name"] = input("이름을 말씀해주세요 : ")

print("안녕하세요~! 좋은 아침입니다! " + userDictionary["name"] + "님!")

print("저는 과일 좋아하는데!")

userDictionary["fruit"] = input("좋아하는 과일 있으세요? : ")

print("아하~ " + userDictionary["fruit"] + "라는 과일을 좋아하시는군요!")
print("제가 바로! " + userDictionary["fruit"] + "준비해드리겠습니다!")

# 미션을 수행할수록 코드의 가독성을 높일 수 있는 방법을 익힐 수 있다.