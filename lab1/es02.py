ind = 0
num =[]
while ind < 1000:
    # num.append(ind)
    num = num + [ind]
    ind += 1
# print(num)
value = input("insert an integer between 0 and 1000 or press Q to quit \n")
print(all([char.isdigit() for char in value]))

# while not all([val.isdigit() for char in value])d :
#     if value == 'q':
#         break
#     else:
#         # print(typ3e(int(value)))
#         value = input("Value inserted is incorrect. try again or quit \n")
# digits = list(value)
# digits = [int(x) for x in digits]
# # print(sum(diùgits))
# # print(sum(int(digits)))
# print("Inserted number " + value +"\ndigits: {}".format(digits) + "\nsum: {}".format(sum(digits)))
