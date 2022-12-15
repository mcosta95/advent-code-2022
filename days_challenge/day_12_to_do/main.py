# Library
FEATURE_DIR = r"./days_challenge/"

import sys
import pandas as pd
import re
import numpy as np
import math

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_11.develop import extra_cleaning, get_worry_levels, get_score

# parameters
DAY_NR = 11
PART = 1
TEST = True
NR_ROUND = 20


if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n\n", extra_clean="\n")

    # extra cleaning
    clean_lst, operation_lst = extra_cleaning(final_lst)

    # development
    dict_items_inspect, dict_worry_levels = get_worry_levels(NR_ROUND, PART, clean_lst, final_lst, operation_lst)

    # score
    get_score(dict_worry_levels, dict_items_inspect, PART, TEST)

