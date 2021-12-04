def isSmaller(num1, num2, invert = False):
    if invert == False:
        if num1 < num2:
            return True
    else:
        if num1 > num2:
            return True

a = isSmaller(13,45, invert = True)
print(a)