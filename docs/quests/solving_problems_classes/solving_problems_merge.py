# - 사용 repository : toy_pythons
# - 팀원 각자 소스(업무) 개발 : 최소 function 2개로 class로 묶음
# - 문제 풀고(class), 점수 따른 학점 출력(class) 서로 머지함.
# - 최종 머지 해결 후 링크
# - 실행 이미지 공유

# # class basic format
# class Class_name :
#     def __init__(self) :   
#         pass
#         return 0

class PythonQuiz:
    def __init__(self):
        self.list_question = [
            'Python에서 변수를 선언하는 방법은? (점수: 10점)'
            ,'Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)'
            ,'Python에서 조건문을 작성하는 방법은? (점수: 10점)'
            ,'Python에서 함수를 정의하는 방법은? (점수: 5점)'    
        ]
        self.list_answer = [
            '1) var name 2) name = value 3) set name 4) name == value'
            ,'1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다'
            ,'1) if-else, 2) for-in, 3) while, 4) def'
            ,'1) class, 2) def, 3) import, 4) return'
        ]

    def test(self):
        num_print_answer=[]
        for num_count in range(len(self.list_question)) :
            print("{}. {}".format(num_count+1, self.list_question[num_count])) 
            print("{}".format(self.list_answer[num_count]))
            num_print_answer.append(int(input("-정답 : ")))
            print("")      
        return num_print_answer

class SolveQuiz:
    def __init__(self, correct = [2,1,1,2], score_problem = [10,15,10,5]):
        self.correct = correct
        self.score_problem = score_problem

    def solve_result(self, list_answer):
        score=[]
        sum_score=0

        for i in range(len(self.correct)):
            if list_answer[i] == self.correct[i]:
                score.append(self.score_problem[i])
                pass
        for i in range(len(score)):
            sum_score += score[i]
            pass
        if sum_score >= 30:
            sum_level = "A"
        elif sum_score >= 20:
            sum_level = 'B'
        else :
            sum_level = 'C'

        print("응답한 내용 : ", end=" ")
        for i in range(len(self.correct)):
            print("{}번 {}".format(i+1,list_answer[i]), end=" ")
        print("\n당신 응답 합계 : {}점".format(sum_score))
        print("학점은 {} 입니다.".format(sum_level))

quiz = PythonQuiz()
solver = SolveQuiz()

answers = quiz.test()
solver.solve_result(answers)

# self.correct = correct라는 구문은 SolveQuiz 클래스의 인스턴스가 생성될 때(즉, SolveQuiz()가 호출될 때) correct라는 매개변수를 입력받아
# 인스턴스 내부 변수인 self.correct에 저장하는 역할을 합니다.

# 이때 correct는 디폴트 값으로 [2,1,1,2]를 가지고 있습니다. 따라서 SolveQuiz()를 호출할 때 correct 매개변수를 따로 전달하지 않으면,
# self.correct는 [2,1,1,2]라는 값을 가집니다. 만약 SolveQuiz([1,2,3,4])와 같이 호출한다면 self.correct는 [1,2,3,4]라는 값을 가집니다.

# 이렇게 인스턴스 내부 변수(self.correct)를 사용하는 이유는 메소드 간에 데이터를 공유하기 위함입니다. self.correct는 SolveQuiz 클래스 내부의 모든 메소드에서 접근하고 수정할 수 있습니다.

# self.correct 변수 없이도 코드를 정상적으로 진행할 수 있습니다. 하지만 이 경우, solve_result 메소드에서 정답 리스트를 직접 입력하거나
# 다른 방법으로 정답 리스트를 받아와야 합니다. 그러나 이런 방식은 코드의 유연성을 떨어뜨리고, 메소드 간 데이터 공유가 어려워져서
# 일반적으로는 인스턴스 변수를 사용하는 것이 더 바람직합니다.




# __init__ 메소드는 클래스의 인스턴스가 생성될 때 자동으로 호출되는 초기화 메소드입니다.
# 이 메소드 안에서는 인스턴스의 초기 상태를 설정하는 코드를 작성합니다.

# self.list_question과 self.list_answer는 인스턴스 변수로, PythonQuiz 클래스의 각 인스턴스가 별도로 가지는 변수입니다.
# 이 변수들은 인스턴스가 생성될 때 초기화되며, 클래스의 다른 메소드에서도 사용할 수 있습니다.

# 이 경우, self.list_question과 self.list_answer는 퀴즈의 문제와 답변을 저장하고 있습니다.
# 이 변수들을 __init__ 메소드 안에 선언함으로써, PythonQuiz 클래스의 인스턴스가 생성될 때 자동으로 이 변수들이 초기화되고,
# 이후 test 메소드 등에서 이 변수들을 사용할 수 있게 됩니다.

# 따라서, self.list_question과 self.list_answer를 __init__ 메소드 안에 넣은 이유는
# PythonQuiz 클래스의 각 인스턴스가 퀴즈의 문제와 답변을 별도로 가질 수 있도록 하기 위함입니다.
# 이는 클래스의 메소드 간에 데이터를 공유하거나, 인스턴스의 상태를 유지하는 등의 역할을 합니다.