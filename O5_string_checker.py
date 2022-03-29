
def string_check(inp):
    while True:
        name = input(inp)
        if name.isdigit():
            print('<error> please enter a string not a number')
            print("")
        else:
            break
    return name

