import sys

sys.path.insert(0, '.')

from days_challenge.day_2 import read_data

final_lst = read_data(folder="days_challenge/day_2", filename="data", split="\n", extra_clean=" ")


dict_translate = {"rock": ["A", "X"], "scissors": ["C", "Z"], "paper": ["B", "Y"]}
dict_point = {"rock": 1, "scissors": 3, "paper": 2}

def rules_(dict_point):
    score_ = 0
    if me_ == oponent_:
        score_ = 3 #draw
        score_ += dict_point[me_]

    elif me_=="rock" and oponent_=="scissors":
        score_ = 6
        score_ += dict_point[me_]

    elif me_=="scissors" and oponent_=="paper":
        score_ = 6
        score_ += dict_point[me_]

    elif me_=="paper" and oponent_=="rock":
        score_ = 6
        score_ += dict_point[me_]

    else:
        score_ = 0
        score_ += dict_point[me_]

    return score_


final_score = []

for round_ in final_lst:

    me_ = [key for key,value in dict_translate.items() if round_[1] in value][0]
    oponent_ = [key for key,value in dict_translate.items() if round_[0] in value][0]

    score_ = rules_(dict_point)
    
    final_score.append(score_)


# get the answer
result = sum(final_score)

print(F"[ANSWER - PART 1] Final results: {result}")