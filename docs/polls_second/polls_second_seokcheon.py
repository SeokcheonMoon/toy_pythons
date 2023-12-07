# source from ../polls_first/polls_first_youjin.py

# # 완성본
# 1. 상품의 품질에 대해 어떻게 생각하시나요?
# 1. 좋음     2. 중간     3. 좋아지길
# ----------
# 2. 상품의 가격에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길
# ----------
# 3. 상품의 디자인에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길
# ----------
# 4. 상품에 대한 전반적인 만족도는 어떠신가요?    
# 1. 좋음     2. 중간     3. 좋아지길

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]

list_statistics = [0,0,0]
list_score = [3,2,1]
for num_first in [0,1,2,3]:
    # str_question = list_question[num_first] 
    print("{}. {}".format(num_first+1, list_question[num_first]))

    for num_second in [0,1,2]: 
        # str_answer = list_answer[num_second]
        print(" {}. {}".format(num_second+1, list_answer[num_second]),end="")
    print("")

    str_question_result = input("당신 생각은 몇 번 : ")
    num_question_result = int(str_question_result)
    index = num_question_result - 1
    list_statistics[index]=list_statistics[index]+1

    if num_first < 3 :
        pass 
        print("----------")
    else :
        print("")
    

print("설문자 답항별 갯수 표시 : ({},".format(list_statistics))

print(list_score[index])

print("답항 가중 평균 : {}+{}+{}/ 3+2+1 =".format(list_statistics*list_score[index]),list_statistics*list_score[index],list_statistics*list_score[index])

