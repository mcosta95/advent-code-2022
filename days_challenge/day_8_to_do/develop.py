import pandas as pd

def get_results_part_1(final_lst):

    final_lst = [list(value_) for value_ in final_lst]
    data_ = pd.DataFrame(final_lst)
    visible = (data_.shape[0] * 4) - 4

    for row_ in range(1, data_.shape[0]-1):
        for column_ in range(1, data_.shape[0]-1):

            value_ = int(data_[column_][row_])

            top_ = any([int(i) < value_ for i in list(data_[column_][:row_].values)])
            bottom_= any([int(i) < value_ for i in list(data_[column_][row_+1:].values)])

            left_ = any([int(i) < value_ for i in list(data_.iloc[column_][:row_].values)])
            right_ = any([int(i) < value_ for i in list(data_.iloc[column_][row_+1:].values)])

            score_ = any([top_, bottom_, left_, right_])

            if score_:
                visible += 1
    
    return visible


def get_score(final_lst, part, test):

    if part == 1:
        final_score = get_results_part_1(final_lst)
    #else:
    #    final_score = get_results_part_2(dict_translate_part_2, dict_win, dict_point, final_lst)

    print(F"[ANSWER - PART {part}] Final value: {final_score}")

    if test:
        test_results(part, final_score)


def test_results(part, final_score):
    if part == 1:
        assert final_score == 21
    else:
        assert final_score == 12
