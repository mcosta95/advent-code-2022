def rules_part_1(dict_point, me_, oponent_):
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


def rules_part_2(dict_point, oponent_, me_):
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


def get_results_part_2(dict_translate, dict_win, dict_point, final_lst):

    final_score = []

    for round_ in final_lst:

        oponent_ = [key for key,value in dict_translate.items() if round_[0] in value][0]
        me_ = [value for key,value in dict_win.items() if round_[1] in key][0]

        score_ = rules_part_2(dict_point, oponent_, me_)
        
        final_score.append(score_)

    final_score = sum(final_score)
    
    return final_score


def get_results_part_1(dict_translate, dict_point, final_lst):

    final_score = []
    for round_ in final_lst:
        
        me_ = [key for key,value in dict_translate.items() if round_[1] in value][0]
        oponent_ = [key for key,value in dict_translate.items() if round_[0] in value][0]

        score_ = rules_part_1(dict_point, me_, oponent_)
        
        final_score.append(score_)

    final_score = sum(final_score)
    
    return final_score



def get_score(dict_translate_part_1, dict_translate_part_2, dict_point, dict_win, final_lst, part, test):

    if part == 1:
        final_score = get_results_part_1(dict_translate_part_1, dict_point, final_lst)
    else:
        final_score = get_results_part_2(dict_translate_part_2, dict_win, dict_point, final_lst)

    print(F"[ANSWER - PART {part}] Final value: {final_score}")

    if test:
        test_results(part, final_score)
        

def test_results(part, final_score):
    if part == 1:
        assert final_score == 15
    else:
        assert final_score == 12
