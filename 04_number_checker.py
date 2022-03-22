
def numberChecker(num):
    try:
        if int(num):
            print("{} is an integer".format(num))
    except:
        print("{} is not a integer".format(num))

word_num = input("enter anything number or letters ")

numberChecker(word_num)