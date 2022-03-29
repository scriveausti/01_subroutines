def higher_number(n1,n2):
    if n1 > n2 :
        print("{} is the highest number".format(n1))
    else:
        print("{} is the highest number".format(n2))

number1 = int(input("enter a number "))
number2 = int(input("enter another number "))

higher_number(number1,number2)
