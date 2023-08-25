# 성적 관리 프로그램

print("[ 성적 평가 프로그램 ]")
print("* 본 프로그램은 시험 점수를 입력하면 그에 맞는 학점을 주는 프로그램 입니다.")

print("본 프로그램을 종료하고 싶다면 언제든지 \"exit\"라고 입력해주세요")
    
print()

def exit_check(command):
    command = str(command)
    if(command == "exit"):
        exit()

def input_name_score(): # 이름과 점수를 입력 받고 출력해준다.
    print("학점을 확인할 학생의 이름과 점수를 입력해주세요.")
    print("- 학생 이름")
    name = input("> ")
    exit_check(name)    # 입력하는 과정에서 종료 커맨드 입력 시 프로그램 종료하는 함수 호출 및 검사
    print("- 점수")
    score = input("> ") 
    exit_check(score)   # 입력하는 과정에서 종료 커맨드 입력 시 프로그램 종효하는 함수 호출 및 검사
    try:
        score = int(score)  # 종료하지 않았을 경우 점수를 정수 형태로 변화 시켜봄
    except:
        print("점수는 숫자를 입력해주세요.")    # 오류 발생 시 점수는 숫자를 입력하라는 오류 출력 후 다시 입력 시점으로 돌아감
        print()
        input_name_score()
    if(score > 100 or score < 0):
        print("점수는 0부터 100점까지만 입력할 수 있습니다.")
        input_name_score()
    print("{} 학생의 학점은 다음과 같습니다.".format(name))
    return score

def Grade(score):   # 점수에 따른 학점 부여 함수
    if(score == 100):
        print("{}점 - A+".format(score))
        print()
    elif(score < 100 and score >= 90):
        print("{}점 - A".format(score))
        print()
    elif(score < 90 and score >=80):
        print("{}점 - B+".format(score))
        print()
    elif(score < 80 and score >=70):
        print("{}점 - B")
        print()
    elif(score < 70 and score >=60):
        print("{}점 - C+".format(score))
        print()
    elif(score < 60 and score >=50):
        print("{}점 - C")
        print()
    else:
        print("{}점 - F (재수강 필요)".format(score))
        print()

while(True):
    student = input_name_score()
    Grade(student)