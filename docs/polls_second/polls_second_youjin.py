# source from ../polls_first/polls_first_seokcheon.py

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]


for quest_count in [0,1,2,3] : 
    print("{}. {}".format(quest_count+1,list_question[quest_count]))
    for answer_count in [0,1,2] :
        print(" {}.{}".format(answer_count+1,list_answer[answer_count]), end="")
    print("")
    if quest_count < 3 :
        print("----------")
    else :    
        print("")
    


    
   
