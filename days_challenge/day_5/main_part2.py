import sys

sys.path.insert(0, '.')

from days_challenge import read_data
from math import ceil
import pandas as pd

final_lst = read_data(folder="days_challenge/day_5", filename="data", split="\n", extra_clean=",")

idx_number = final_lst.index(['']) - 1
nr_lists = int(final_lst[idx_number][0].split()[-1])

# clean matrix
df_initial = pd.DataFrame(columns=range(1, nr_lists+1))

for row_ in final_lst[:idx_number]:
    one_ = row_[0]
    stride = ceil(len(one_) / nr_lists)
    parts = [one_[i:i+stride].strip() for i in range(0, len(one_), stride)]
    df_initial.loc[0] = parts
    df_initial.index = df_initial.index + 1

df_initial = df_initial.sort_index(ascending=True)

df_dict = df_initial.to_dict('list')

for key_, value_ in df_dict.items():
   df_dict[key_] = list(filter(None, value_))

# clean rules
rules_ = final_lst[idx_number+2:]
rules_clean = [iter_[0].split(" ") for iter_ in rules_]

for rule_ in rules_clean:

    move_ = int(rule_[rule_.index("move") + 1])
    from_ = int(rule_[rule_.index("from") + 1])
    to_ = int(rule_[rule_.index("to") + 1])

    to_move_from = df_dict[from_][-move_:]

    del df_dict[from_][-move_:]

    df_dict[to_] = df_dict[to_] + to_move_from
        
final_result = ""
for key_, value_ in df_dict.items():
   final_result = final_result + value_[-1]

final_result = final_result.replace("[", "").replace("]", "")

print(F"[ANSWER - PART 1] Final results: {final_result}")