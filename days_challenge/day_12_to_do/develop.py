import numpy as np
import math
import re

def extra_cleaning(final_lst):
    clean_lst = []
    for monkey_ in final_lst:
        monkey_fin = [re.findall(r'\d+', monkey_[value_]) for value_ in range(0, len(monkey_))]
        clean_lst.append(monkey_fin)
    
    operation_lst = [idx_[2].replace("Operation: new = ", "").strip() for idx_ in final_lst]
    return clean_lst, operation_lst


def isDivisible(number, divisor, monkey_):

    if number % divisor == 0:
        return int(monkey_[4][0])
    else:
        return int(monkey_[5][0])


def test_condition(new, monkey_):

    # test
    test = int(monkey_[3][0])

    # condition
    return isDivisible(new, test, monkey_)


def get_worry_levels(nr_round, part, clean_lst, final_lst, operation_lst):

    dict_items_inspect = { i : 0 for i in range(0, len(final_lst))}
    dict_worry_levels = { i : [] for i in range(0, len(final_lst))}

    for i in range(0, nr_round):
        for idx_ in range(0, len(clean_lst)):
            if i == 0:
                items_lst = [int(s) for s in clean_lst[idx_][1]]
                worry_levels = dict_worry_levels[idx_].copy() + items_lst
                dict_worry_levels[idx_] = dict_worry_levels[idx_] + items_lst
                dict_items_inspect[idx_] = dict_items_inspect[idx_] + len(items_lst)
            else:
                worry_levels = dict_worry_levels[idx_].copy()

            for old in worry_levels:
                # operation
                new = eval(operation_lst[idx_])

                if part == 1:
                    new = math.floor(new/3)
                else:
                    worry_monkeys = [int(one_monkey[3][0]) for one_monkey in clean_lst]
                    worry_level = np.prod(worry_monkeys)
                    new = new % worry_level

                condition = test_condition(new, clean_lst[idx_])
                dict_items_inspect[condition] += 1 

                dict_worry_levels[condition].append(new)
                dict_worry_levels[idx_].remove(old)

    return dict_items_inspect, dict_worry_levels


def get_score(dict_worry_levels, dict_items_inspect, part, test):

    extra_items = {key: len(value) for key, value in dict_worry_levels.items()}
    final_score = {key: dict_items_inspect[key] - extra_items.get(key, 0) for key in dict_items_inspect}

    final_score = np.prod(sorted(final_score.values(), reverse=True)[:2])

    print(F"[ANSWER - PART {part}] Final value: {final_score}")

    if test:
        test_results(part, final_score)


def test_results(part, final_score):
    if part == 1:
        assert final_score == 10605
    else:
        assert final_score == 2713310158
