
def numberChecker(ask):
    while True:
        try:
            num = int(input(ask))
            break
        except:
            print("<error> pleas enter a number")
            print("")
    return num
