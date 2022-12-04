import sys

sys.path.insert(0, '.')

from days_challenge.day_4 import read_data

final_lst = read_data(folder="days_challenge/day_4", filename="data", split="\n", extra_clean=",")

final_score = []

for pair_ in final_lst:
    pair_1_min, pair_1_max = pair_[0].split("-")
    pair_2_min, pair_2_max = pair_[1].split("-")

    pair_1_set = set(range(int(pair_1_min), int(pair_1_max)+1))
    pair_2_set = set(range(int(pair_2_min), int(pair_2_max)+1))

    overlap_ = pair_1_set & pair_2_set

    if len(overlap_) > 0:
        final_score.append(1)
    else:
        final_score.append(0)

# get the answer
result = sum(final_score)

print(F"[ANSWER - PART 2] Final results: {result}")