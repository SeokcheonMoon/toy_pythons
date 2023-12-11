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