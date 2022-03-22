func = ["add", "subtract", "multiply","divide"]

def calculate(a,b,asmd):
    if asmd == "add" :
        answer = a + b
        print("{} + {} = {}".format(a,b,answer))
    elif asmd == "subtract" :
        answer = a - b
        print("{} - {} = {}".format(a, b, answer))
    elif asmd == "multiply" :
        answer = a * b
        print("{} * {} = {}".format(a, b, answer))
    else:
        answer = a / b
        print("{} / {} = {}".format(a, b, answer))


def asknumber(q):
    while True:
        try:
            num = int(input(q))
            break
        except:
            print("<error> please enter a number")
    return num


num1 = asknumber("enter a number: ")
num2 = asknumber("enter another number: ")
while True:
    asmd = input("would you like to add, subtract, multiply or divide? ")
    if asmd in func:
        break
    else:
        print("<error> please enter \"add\", \"subtract\", \"multiply\" or \"divide\" the 2 numbers")



calculate(num1, num2, asmd)