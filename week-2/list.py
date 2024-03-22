
def isi(arr = []):
    return [x for x in range(10)]

list = []
list = isi(list)


for i in range(len(list)):
    if  list[i] % 2 == 0:
        print(f"num of {list[i]} is even")
    elif  list[i] % 2 != 0:
        print(f"num of {list[i]} is odd")
    else:
        print(f"{list[i]} is not number type")