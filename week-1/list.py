listPow2 = [i**2 for i in range(0, 10)]
listEven = [i for i in range(0, 10) if i%2 == 0]
listRange = list(range(0, 10, 3))




print("list power by 2:\t", listPow2, "\n")
print("list even:\t", listEven, "\n")
print("list range between 0 and 10:\t", listRange, "\n")
print("\n===================\n\n")
data = []
data.insert(0, listPow2)
data.append(listEven)
data.append(listRange)
print("raw data:\t", data,"n")
data.sort()
print("sorted data:\t",data, "\n")
datapop = data.pop(0)
print("\n")
print("pop data:\t", datapop, "\n")
print("data:\t",data, "\n")
