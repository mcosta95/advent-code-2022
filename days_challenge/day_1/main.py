import sys

sys.path.insert(0, '.')


# opening the file in read mode
my_file = open("days_challenge/data.txt", "r")
  
# reading the file
data = my_file.read()
data_into_list = data.replace('\n\n', ' ').split(' ')

# prepare the data
final_lst = [iter_.split("\n") for iter_ in data_into_list]
sum_lst = [sum(list(map(int, values_))) for values_ in final_lst]

# get the answer
sum_lst.sort(reverse=True)
top_3 = sum(sum_lst[:3])
max_value = max(sum_lst[0])

print(F"[ANSWER - PART 1] Max value: {max_value}")
print(F"[ANSWER - PART 2] Max top 3 value: {top_3}")
