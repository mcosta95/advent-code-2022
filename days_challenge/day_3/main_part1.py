import sys

sys.path.insert(0, '.')

import string

from days_challenge.day_3 import read_data

data_into_list = read_data(folder="days_challenge/day_3", filename="data", split="\n")

final_score = []
for one_item in data_into_list:
    len_ = len(one_item)
    half_len = len(one_item)/2

    part_1 = one_item[:int(half_len)]
    part_2 = one_item[int(half_len): int(len_)]

    value_ = list(set(part_1) & set(part_2))[0]

    alpha_lst = list(string.ascii_lowercase) + list(string.ascii_lowercase.upper())
    score_ = alpha_lst.index(value_) + 1
    final_score.append(score_)


# get the answer
result = sum(final_score)

print(F"[ANSWER - PART 1] Final results: {result}")