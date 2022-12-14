import numpy as np

def score_cycles(final_lst):
    score_cycles = {}
    cycle = 1
    X = 1
    for instruction_ in final_lst:
        if "noop" in instruction_:
            score_cycles[cycle] = X
            cycle += 1

        elif "addx" in instruction_:
            score_cycles[cycle] = X
            cycle += 1
            score_cycles[cycle] = X
            cycle += 1
            X += int(instruction_.replace("addx", "").strip())
            score_cycles[cycle] = X
    return score_cycles


def get_results_part_1(final_lst):
    lst_cycles = [20, 60, 100, 140, 180, 220]
    score = [score_cycles(final_lst)[nr_cycle]* nr_cycle for nr_cycle in lst_cycles]
    final_result = np.sum(score)
    return final_result

def overlap(pixel_pos, sprite_pos):
    return sprite_pos - 1 <= pixel_pos <= sprite_pos + 1


def get_results_part_2(final_lst):

    cycle = 1
    for row in range(6):
        for pixel_pos in range(40):
            if cycle <= 240:
                pixel = '#' if overlap(pixel_pos, score_cycles(final_lst)[cycle]) else '.'
                print(pixel, end='')
                cycle += 1
        
        print('')


def get_score(final_lst, part, test):

    if part == 1:
        final_score = get_results_part_1(final_lst)
        print(F"[ANSWER - PART {part}] Final value: {final_score}")
        
    else:
        print(F"[ANSWER - PART {part}]")
        get_results_part_2(final_lst)
    
    if test:
        test_results(part, final_score)


def test_results(part, final_score):
    if part == 1:
        assert final_score == 13140
