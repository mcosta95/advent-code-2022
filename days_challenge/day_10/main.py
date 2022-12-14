# Library
FEATURE_DIR = r"./days_challenge/"

import sys
import pandas as pd
import numpy as np

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_10.develop import score_cycles, get_score

# parameters
DAY_NR = 10
PART = 2
TEST = False

if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n")

    # get score cycles
    score_cycles = score_cycles(final_lst)

    # get score
    get_score(final_lst, PART, TEST)





        
        