ind = 1000
num =[]
while ind < 2001:
    # num.append(ind)
    num = num + [ind]
    ind += 1

# num = [x for x in [1000:2000]]

a = list(filter(lambda x: (x%6 == 0)&(x%9 !=0), num))
print(a)