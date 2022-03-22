def equal(a, b):
    while a != b:
        if a > b:
            b = b + 1
        else:
            b = b - 1
    return b


print(equal(5,7))