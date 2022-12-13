import sys

sys.path.insert(0, '.')

from days_challenge import read_data
from functools import reduce  # forward compatibility for Python 3
import operator


final_lst = read_data(folder="days_challenge/day_7", filename="data_test", split="\n")


def nested_set(dic, keys, value, create_missing=True):
    d = dic
    for key in keys[:-1]:
        if key in d:
            d = d[key]
        elif create_missing:
            d = d.setdefault(key, {})
        else:
            return dic
    if keys[-1] in d or create_missing:
        d[keys[-1]] = value
    return dic

command_execute_idx = [idx for idx, s in enumerate(final_lst) if '$' in s]
if len(final_lst) not in command_execute_idx:
    command_execute_idx.append(len(final_lst))


final_result = {"/": {}}
curr_dir = "/"
dir_path = ["/"]
for idx_ in range(1, len(command_execute_idx)-1):
    curr_idx = command_execute_idx[idx_]
    next_idx = command_execute_idx[idx_ + 1]

    if "$ ls" in final_lst[curr_idx]:
        dict_ = { i : {} for i in final_lst[curr_idx+1: next_idx]}
        final_result = nested_set(final_result, dir_path, dict_, create_missing=True)
    if "$ cd" in final_lst[curr_idx]:
        if "$ cd .." in final_lst[curr_idx]:
            del dir_path[-1]
        else:
            curr_dir = "dir " + final_lst[curr_idx].replace("$ cd", "").strip()
            dir_path.append(curr_dir)

a = 1

data_score = {}

d = final_result
for key in list(d.keys()):
    print(key)
    final_files = [int(tuple(value_.split())[0]) for value_ in list(d[key].keys())  if "dir" not in value_]
    data_score[key] = sum(final_files)
    d = d[key]



# cd value - changes directory
# cd .. - moves out directory
# cd / - change to the outer most 
