import sys
import string

sys.path.insert(0, '.')

# opening the file in read mode
my_file = open("day_4/data.txt", "r")
  
# reading the file
data = my_file.read()

# prepare the data
data_into_list = data.split('\n')
final_lst = [iter_.split(",") for iter_ in data_into_list]

final_score = []

for pair_ in final_lst:
    pair_1_min, pair_1_max = pair_[0].split("-")
    pair_2_min, pair_2_max = pair_[1].split("-")

    pair_1_set = set(range(int(pair_1_min), int(pair_1_max)+1))
    pair_2_set = set(range(int(pair_2_min), int(pair_2_max)+1))

    if pair_1_set.issubset(pair_2_set):
        final_score.append(1)
    elif pair_2_set.issubset(pair_1_set):
        final_score.append(1)
    else:
        final_score.append(0)

# get the answer
result = sum(final_score)

print(F"[ANSWER - PART 1] Final results: {result}")