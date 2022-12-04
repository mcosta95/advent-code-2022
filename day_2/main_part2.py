import sys

sys.path.insert(0, '.')

from day_2 import read_data

final_lst = read_data(folder="day_2", filename="data", split="\n", extra_clean=" ")

dict_translate = {"rock": "A", "scissors": "C", "paper": "B"}
dict_win = {"X": "lose", "Y": "draw", "Z": "win"}
dict_point = {"rock": 1, "scissors": 3, "paper": 2}


def rules_(dict_point, oponent_, me_):
    rules_win = {"scissors": "rock", "paper": "scissors", "rock": "paper"}

    score_ = 0
    if me_ == "win":
        score_ = 6
        me_ = rules_win[oponent_]
        score_ += dict_point[me_]

    elif me_ == "draw":
        score_ = 3 #draw
        me_ = oponent_
        score_ += dict_point[me_]

    else:
        score_ = 0
        me_ = [key for key, value in rules_win.items() if oponent_ in value][0]
        score_ += dict_point[me_]

    return score_



final_score = []

for round_ in final_lst:

    oponent_ = [key for key,value in dict_translate.items() if round_[0] in value][0]
    me_ = [value for key,value in dict_win.items() if round_[1] in key][0]

    score_ = rules_(dict_point, oponent_, me_)
    
    final_score.append(score_)


# get the answer
result = sum(final_score)

print(F"[ANSWER - PART 2] Final results: {result}")
