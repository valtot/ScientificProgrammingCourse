def strcmpi(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 != l2:
        return False
    else:
        ord1 = [ord(char) for char in str1]
        ord2 = [ord(char) for char in str2]
        i = 0
        boolList  =[]
        while i < l1:
            boolList.append(ord1[i] == ord2[i])
            i+=1
        return all(boolList)

color = input("insert one color\n")
clr = ["red", "green", "blue", "purple", "yellow"]


boolList2 = []
for col in clr:
     boolList2.append(strcmpi(color, col))

if any(boolList2):
    print("right color selected\n")
else:
    print("wrong color selected\n")
       

