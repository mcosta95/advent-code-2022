# Library
FEATURE_DIR = r"./days_challenge/"

import sys
import pandas as pd

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_8.develop import get_score

# parameters
DAY_NR = 8
PART = 1
TEST = False

if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n")

    get_score(final_lst, PART, TEST)





