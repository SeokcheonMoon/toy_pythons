

#답항별 갯수표시
list_score=[10,15,10,5]
list_input=[2,1,1,2]
list_answer=[2,1,1,2]



# list_input 과 list_answer가 매칭시 점수 부여
# 총합 점수


# sum = 0 

# for index in [0,1,2,3] : 
    
#     if list_input[index] == list_answer[index] :
#         pass
#         sum = sum + list_score[index]
        
#     print("당신 응답 합계 : {}점".format(sum))  


# 점수 합계 구하기
def sum() :
    num_sum = 0 

    for index in [0,1,2,3] : 
    
        if list_input[index] == list_answer[index] :
            pass
            num_sum = num_sum + list_score[index]
    return num_sum
print("당신 응답 합계 : {}점".format(sum()))    

# 점수 등급 매기기
def grade() :

    str_grade = ""

    if sum() >= 30 :
        pass
        str_grade = "A"
    elif sum() >= 20 :
        pass
        str_grade = "B"
    else :
        pass
        str_grade = "F"

    return str_grade

print("학점은 {} 입니다.".format(grade()))  










