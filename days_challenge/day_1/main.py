# Library
FEATURE_DIR = r"./days_challenge/"

import sys

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_1.develop import get_order_data, get_score

# parameters
DAY_NR = 1
PART = 1
TEST = False

if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n\n", extra_clean="\n")
    
    # development
    sum_lst = get_order_data(final_lst)

    # get scores
    final_score = get_score(sum_lst, PART, test=TEST)


