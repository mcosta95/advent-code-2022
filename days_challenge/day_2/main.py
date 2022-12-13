# Library
FEATURE_DIR = r"./days_challenge/"

import sys

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_2.develop import get_score

# parameters
DAY_NR = 2
PART = 1
TEST = True

dict_translate_part_1 = {"rock": ["A", "X"], "scissors": ["C", "Z"], "paper": ["B", "Y"]}
dict_translate_part_2 = {"rock": "A", "scissors": "C", "paper": "B"}
dict_point = {"rock": 1, "scissors": 3, "paper": 2}
dict_win = {"X": "lose", "Y": "draw", "Z": "win"}


if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n", extra_clean=" ")

    # get scores
    final_score = get_score(dict_translate_part_1, dict_translate_part_2, dict_point, dict_win, final_lst, PART, TEST)
