import sys
import string

sys.path.insert(0, '.')

# opening the file in read mode
my_file = open("day_3/data.txt", "r")
  
# reading the file
data = my_file.read()

# prepare the data
data_into_list = data.split('\n')

group_lst = [data_into_list[n:n+3] for n in range(0, len(data_into_list), 3)]
alpha_lst = list(string.ascii_lowercase) + list(string.ascii_lowercase.upper())

final_score = []
for group_ in group_lst:
    value_ = list(set(group_[0]) & set(group_[1]) & set(group_[2]))[0]
    score_ = alpha_lst.index(value_) + 1
    final_score.append(score_)


# get the answer
result = sum(final_score)

print(F"[ANSWER - PART 2] Final results: {result}")
#print(F"[ANSWER - PART 2] Max top 3 value: {top_3}")
