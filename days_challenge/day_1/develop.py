def get_order_data(final_lst):

    sum_lst = [sum(list(map(int, values_))) for values_ in final_lst]
    sum_lst.sort(reverse=True)
    return sum_lst


def get_score(sum_lst, part, test):

    if part==1:
        final_score = sum_lst[0]
    else:
        final_score = sum(sum_lst[:3])

    print(F"[ANSWER - PART {part}] Final value: {final_score}")

    if test:
        test_results(part, final_score)
        

def test_results(part, final_score):
    if part == 1:
        assert final_score == 24000
    else:
        assert final_score == 45000
