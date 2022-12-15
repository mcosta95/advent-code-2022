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

    shape_ = sum(nr_moves)
    
    motions_matrix = np.zeros((shape_, shape_), dtype=str)
    score_matrix = np.zeros((shape_, shape_), dtype=str)

    # H - 1 & T - 2
    # set starting point
    curr_H_row = shape_-1
    curr_H_col = 0
    curr_T_row = shape_-1
    curr_T_col = -1

    motions_matrix[curr_H_row][curr_H_col] = "H"

    for idx_ in range(shape_):
        move = moves_[idx_]
        nr_ = nr_moves[idx_]

        if move == "R":
            for nr__ in list(range(1, nr_+1)):
                # update head
                motions_matrix[curr_H_row][curr_H_col+1] = "H"
                motions_matrix[curr_H_row][curr_H_col] = "."
                curr_H_col += 1
                
                # update tail
                if all(x in "".join(motions_matrix[curr_H_row-1]) for x in ["H", "T"]):
                    motions_matrix[curr_T_row][curr_T_col+1] = "T"
                    motions_matrix[curr_T_row][curr_T_col] = "."
                    curr_T_col += 1
                    score_matrix[curr_T_row][curr_T_col] = "T"
        
        if move == "U":
            for nr__ in list(range(1, nr_+1)):
                # update head
                motions_matrix[curr_H_row-1][curr_H_col] = "H"
                motions_matrix[curr_H_row][curr_H_col] = "."
                curr_H_row -= 1
                
                # update tail
                if all(x in "".join(motions_matrix[curr_H_row-1]) for x in ["H", "T"]):
                    motions_matrix[curr_T_row-1][curr_T_col] = "T"
                    motions_matrix[curr_T_row][curr_T_col] = "."
                    curr_T_col -= 1
                    score_matrix[curr_T_row][curr_T_col] = "T"
                else:
                    



        # update head

        # update tail



    



    get_score(final_lst, PART, TEST)





