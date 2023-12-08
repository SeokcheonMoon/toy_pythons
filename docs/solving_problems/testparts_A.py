def solve_result(answer_list):
    correct=[2,1,1,2]
    score=[]
    score_problem=[10,15,10,5]
    sum_score=0

    for i in range(len(correct)):
        if answer_list[i] == correct[i]:
            score.append(score_problem[i])
            pass
        pass
    for i in range(len(score)):
        sum_score += score[i]
        pass
    if sum_score >= 30:
        sum_level = "A"
        pass
    elif sum_score >= 20:
        sum_level = 'B'
        pass
    else :
        sum_level = 'C'
        pass
    print("응답한 내용 : ", end=" ")
    for i in range(len(correct)):
        print("{}번 {}".format(i+1,answer_list[i]), end=" ")
        pass
    print("\n당신 응답 합계 : {}점".format(sum_score))
    print("학점은 {} 입니다.".format(sum_level))
    pass

solve_result()
