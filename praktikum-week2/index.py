import json


def Average(data = {}, key = ""):
    # key validation
    avg = 0
    for x in data:        
        if not key in data[x]:
            raise Exception(f"{key} is not exist")
        
        avg += data[x][key]/len(data)
    
    return avg

def median(nums = []):
    if not type([x for x in nums]) == int:
        raise Exception(f"not number type")
    
    # v0 + vn / 2
    return (min(nums) + max(nums))/2

def GetMax(data = {}, key = ""):
    # MAXNUM = max([x for x in data[key]])
    numbers = []
    for x in data:
        numbers.append(data[x][key])
    
    return max(numbers)
    
def GetMin(data = {}, key = ""):
    numbers = []
    for x in data:
        numbers.append(data[x][key])
    
    return min(numbers)

def SumProduct(data= {}, key = ""):
    numbers = []
    for x in data:
        numbers.append(data[x][key])
    
    return sum(numbers)

def GetMedian(data= {}, key = ""):
    numbers = []
    for x in data:
        numbers.append(data[x][key])
    return median(numbers)

# path to json file
json_path = 'data.json'
try:
    # read json file
    with open(json_path, 'r') as json_file:
        data = json.load(json_file) # get data from json file -> {key:value}
        
        avg_produk_terjual = Average(data, "produk_terjual")
        avg_penjualan = Average(data, "jumlah_penjualan")
        
        max_produk_terjual = GetMax(data, "produk_terjual")
        max_jumlah_penjualan = GetMax(data, "jumlah_penjualan")
        
        print(f"\nrata2 produk terjual {avg_produk_terjual} ")
        print(f"rata2 penjualan {avg_penjualan} \n")
        print(f"max produk terjual {max_produk_terjual} ")
        print(f"max penjualan {max_jumlah_penjualan} \n")
# Throw exception if fail to open file
except FileNotFoundError:
    print(f"File '{json_path}' not found.")
