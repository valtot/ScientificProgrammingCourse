def checkNum(num):
    if all([char.isdigit() for char in num]) == True:
        return True
    else:
        return False

def greatestCD(num1, num2):
    n01 = max([num1,num2])
    n02 = min([num1,num2])
    while n02 != 0:
        a = divmod(n01,n02)
        n01 = a[0]
        n02 = a[1]
    return n01


dval1 = input("type the first number\n")

while not(checkNum(val1)):
    if val1 == 'q':
        break
    val1 = input("Uncorrect value. Insert a number of press q to quit\n")

val2 = input("type the second number\n")
while not(checkNum(val2)):
    if val1 == 'q':
        break
    val1 = input("Uncorrect value. Insert a number of press q to quit\n")

val1 = int(val1)
val2 = int(val2)

print("Greatest common divisor: {}".format(greatestCD(val1,val2)))




