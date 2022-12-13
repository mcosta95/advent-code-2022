# Library
FEATURE_DIR = r"./days_challenge/"

import sys
import pandas as pd
import numpy as np

sys.path.insert(0, FEATURE_DIR)

from utils import read_data
from day_9.develop import get_score

# parameters
DAY_NR = 9
PART = 1
TEST = True

if __name__ == '__main__':

    if TEST:
        filename_ = "data_test"
    else:
        filename_ = "data"

    # import data
    final_lst = read_data(folder=f"days_challenge/day_{DAY_NR}/data", filename=filename_, split="\n")

    moves_ = [move_.split(" ")[0] for move_ in final_lst]
    nr_moves = [int(move_.split(" ")[1]) for move_ in final_lst]

    shape_ = max(nr_moves)
    
    motions_matrix = np.zeros((shape_, shape_))
    score_matrix = np.zeros((shape_, shape_))

    # H - 1 & T - 2
    # set starting point
    curr_row = shape_-1
    curr_col = 0
    motions_matrix[curr_row][curr_col] = 1
    score_matrix[curr_row][curr_col] = 1

    for idx_ in range(shape_):
        idx_ = 0
        move = moves_[idx_]
        nr_ = nr_moves[idx_]

        if move == "R":
            for move in list(range(1, nr_+1)):
                # update head
                motions_matrix[curr_row][curr_col+1] = 1

                
                # update tail
                motions_matrix[curr_row][curr_col+1] = 2
                curr_col = curr_col+2


        # update head

        # update tail



    



    get_score(final_lst, PART, TEST)





