# 1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)
#    1) var name, 2) name = value, 3) set name, 4) name == value
#    - 정답: 2

# 2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)
#    1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다
#    - 정답: 1

# 3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)
#    1) if-else, 2) for-in, 3) while, 4) def
#    - 정답: 1

# 4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)
#    1) class, 2) def, 3) import, 4) return
#    - 정답: 2

class Problems :
    list_top = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)"
                ," 1) var name, 2) name = value, 3) set name, 4) name == value"
                ," - 정답: 2"
                ,"2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)"
                ," 1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다"
                ," - 정답: 1"
                ,"3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)"
                ," 1) if-else, 2) for-in, 3) while, 4) def"
                ," - 정답: 1"
                ,"4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
                ," 1) class, 2) def, 3) import, 4) return"
                ," - 정답: 2"
                ]

    list_statistics = [0,0,0,0]   # 답항만큼 0을 넣어줌
    for num_count in [0,3,6,9]:
        # str_content = list_top[num_count]
        # print("{}".format(str_content))
        str_question = list_top[num_count] #0,3,6,9문항
        print("{}".format(str_question))
        str_answer = list_top[num_count+1] #변수의값+1, 1,4,7,10답항
        print("{}".format(str_answer))

        str_question_result = input(" -정답: ")
        num_question_result = int(str_question_result)  # 문자를 숫자로 변환
        index = num_question_result - 1 # index 위치값 적용
        list_statistics[index] = list_statistics[index] + 1


        print("")
        pass
problems = Problems()
print(problems.str_question_result)
print(problems.solve_result)

# # 리스트를 튜플로 변환하여 출력
# tuple_answers = tuple(list_answers)
# print("정답리스트 : {}".format(tuple_answers))