import json
import matplotlib.pyplot as plt
import numpy as np

def Average(data = {}, key = ""):
    # key validation
    avg = 0
    for x in data:        
        if not key in data[x]:
            raise Exception(f"{key} is not exist")
        
        avg += data[x][key]/len(data)
    
    return avg

def median(nums = []):
    for x in nums:
        if not (type(x) == int or type(x) == float):
            raise Exception(f"{x} is not number type")
            
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

def getKey(data = {}):
    keys = []
    for x in data:
        keys.append(x)
        
    return keys

def getListByKey(data = {}, key = ""):
    
    list = []
    for k in data:
        if not key in data[k]:
            raise Exception(f"key {key} not exist")
        
        list.append(data[k][key])
    return list

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
        
        min_produk_terjual = GetMin(data, "produk_terjual")
        min_jumlah_penjualan = GetMin(data, "jumlah_penjualan")
        
        mid_produk_terjual = GetMedian(data, "produk_terjual")
        mid_jumlah_penjualan = GetMedian(data, "jumlah_penjualan")
        
        print(f"\nrata2 produk terjual\t: {avg_produk_terjual} ")
        print(f"rata2 penjualan\t: {avg_penjualan} \n")
        
        print(f"max produk terjual\t: {max_produk_terjual} ")
        print(f"max penjualan\t: {max_jumlah_penjualan} ")
        
        print(f"min produk terjual\t: {min_produk_terjual} ")
        print(f"min penjualan\t: {min_jumlah_penjualan} ")
        
        print(f"median produk terjual\t: {mid_produk_terjual} ")
        print(f"median penjualan\t: {mid_jumlah_penjualan} \n")
        print('\n')
        
        xpoint = np.array(getKey(data)) 
        
        ypoint_produkTerjual = np.array(getListByKey(data, "produk_terjual"))
        print(ypoint_produkTerjual)
        ypoint_totalPenjualan = np.array(getListByKey(data, "jumlah_penjualan"))
        print(ypoint_totalPenjualan)
        
        # produk terjual
        # merah
        plt.plot(xpoint, ypoint_produkTerjual, c = 'red')
        # total penjualan
        # hijau
        plt.plot(xpoint, ypoint_totalPenjualan, c = 'green')
        
        # set axis
        plt.axis([0, 7, 0, max_jumlah_penjualan])
        plt.show()
        
# Throw exception if fail to open file
except FileNotFoundError:
    print(f"File '{json_path}' not found.")
