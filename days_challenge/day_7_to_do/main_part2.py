import sys

sys.path.insert(0, '.')

from days_challenge import read_data

final_lst = read_data(folder="days_challenge/day_6", filename="data", split="\n", extra_clean=",")[0][0]

final_lst = list(final_lst)
n = 14
result = [final_lst[i:i+n] for i in range(len(final_lst)-n+1)]

idx_score = 0
for idx_ in range(len(result)):
    if len(set(result[idx_])) == n:
        idx_score = idx_ + n
        break

print(F"[ANSWER - PART 2] Final results: {idx_score}")