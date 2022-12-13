# Library
FEATURE_DIR = r"./days_challenge/"

import sys
import pandas as pd
import re
import numpy as np
import math

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_11.develop import get_score

# parameters
DAY_NR = 11
PART = 2
TEST = False

def isDivisible(number, divisor, monkey_):
    if number % divisor == 0:
        return int(monkey_[4][0])
    else:
        return int(monkey_[5][0])

def test_condition(monkey_):
    # test
    test = int(monkey_[3][0])

    # condition
    return isDivisible(new, test, monkey_)


if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n\n", extra_clean="\n")

    clean_lst = []
    for monkey_ in final_lst:
        monkey_fin = [re.findall(r'\d+', monkey_[value_]) for value_ in range(0, len(monkey_))]
        clean_lst.append(monkey_fin)
    
    operation_lst = [idx_[2].replace("Operation: new = ", "").strip() for idx_ in final_lst]

    dict_items_inspect = { i : 0 for i in range(0, len(final_lst))}
    dict_next_round = { i : [] for i in range(0, len(final_lst))}

    for idx_ in range(0, len(clean_lst)):
        items_lst = [int(s) for s in clean_lst[idx_][1]]
        iterator_lst = dict_next_round[idx_].copy() + items_lst
        dict_next_round[idx_] = dict_next_round[idx_] + items_lst
        dict_items_inspect[idx_] = dict_items_inspect[idx_] + len(items_lst)

    # round
    nr_round = 10000

    i = 0
    while i <= nr_round:
        for idx_ in range(0, len(clean_lst)):

            for old in dict_next_round[idx_].copy():
                # operation
                new = eval(operation_lst[idx_])

                #if PART==1:
                #    new = math.floor(new/3)

                condition = test_condition(clean_lst[idx_])
                dict_items_inspect[condition] += 1 

                dict_next_round[condition].append(new)
                dict_next_round[idx_].remove(old)
        i += 1


    extra_items = {key: len(value) for key, value in dict_next_round.items()}
    final_score = {key: dict_items_inspect[key] - extra_items.get(key, 0) for key in dict_items_inspect}

    final_result = np.prod(sorted(final_score.values(), reverse=True)[:2])

    print(final_score)
    print(final_result)