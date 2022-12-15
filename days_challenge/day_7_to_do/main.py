# Library
FEATURE_DIR = r"./days_challenge/"

import sys
import pandas as pd

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
import networkx as nx
import re
from day_7.develop import get_score

# parameters
DAY_NR = 7
PART = 1
TEST = False

if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n")

    command_execute_idx = [idx for idx, s in enumerate(final_lst) if '$' in s]
    if len(final_lst) not in command_execute_idx:
        command_execute_idx.append(len(final_lst))

    G = nx.DiGraph()

    final_result = {"/": {}}
    G.add_node("/")
    curr_dir = "/"
    dir_path = ["/"]
    for idx_ in range(1, len(command_execute_idx)-1):

        curr_idx = command_execute_idx[idx_]
        next_idx = command_execute_idx[idx_ + 1]
        command_execute = final_lst[curr_idx]

        if "$ ls" in command_execute:
            for value in final_lst[curr_idx+1: next_idx]:
                if "dir" in value:
                    G.add_edge(curr_dir, value, weight=0)
                else:
                    lst_value = value.split(" ")
                    G.add_edge(curr_dir, lst_value[1], weight=int(lst_value[0]))

        if "$ cd" in command_execute:
            if "$ cd .." in command_execute:
                del dir_path[-1]
                curr_dir = dir_path[-1]

            else:
                new_dir = "dir " + command_execute.replace("$ cd", "").strip()
                G.add_edge(curr_dir, new_dir, weight=0)
                curr_dir = new_dir
                dir_path.append(curr_dir)

    dict_data = nx.to_dict_of_dicts(G)

    final_dict = {}
    extra_sum = {}
    dir_names = [dir_ for dir_ in list(G.nodes()) if "dir" in dir_] 
    dir_names.reverse()

    for one_dir in dir_names:
        print(one_dir)
        final_dict[one_dir] = sum([value_["weight"] for key_, value_ in dict_data[one_dir].items()])
        print(final_dict)
        
        check_any_more_dir = [dir_ for dir_ in list(dict_data[one_dir].keys()) if "dir" in dir_]
        if len(check_any_more_dir) >= 1:
            for value_one in check_any_more_dir: 
                final_dict[one_dir] += final_dict[value_one]

    final_dict["/"] = G.size(weight="weight")

    final_score = sum([v for k, v in final_dict.items() if v <= 100000])
    
    print(final_score)
    a = 1


