from O4_number_checker import numberChecker

answer = 0

ask_num = "what times tables do you want "
times_table = numberChecker(ask_num)

print("")

print('here is the {} times table'.format(times_table))
for x in range(1,13):
    answer = x * times_table
    print("{} times {} is {}".format(x,times_table, answer))
