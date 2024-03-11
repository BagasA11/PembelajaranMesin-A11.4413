def sort_harga(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            # Bandingkan masing-masing elemen
            if arr[j][3] > arr[j + 1][3]:
                # Jika elemen pertama lebih besar, tukar posisinya
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_ID(buku, index):
    
    if index > len(buku):
        return
    
    item = []
    for i in range(len(buku)):
        if buku[i][0] == index:
            item = buku[i]
            break
        i+=1
    
    return item

def Get_ByJudul(buku, judul = str()):
    return [b for b in buku if b[1] == judul]

buku = []
again = str("y")
urut = str()
i = 0
while again == "y":
    judul = input("masukkan judul buku\t: ")
    penerbit = input("masukkan penerbit buku\t: ")
    harga = int(input("input harga (rp)\t: "))
    cart = [i+1, judul, penerbit, harga]
    buku.append(cart)

    for id in range(len(buku)):
        print("id: ", buku[id][0], "\tjudul: ", buku[id][1], "\tpenerbit: ", buku[id][2], "\tharga: ", buku[id][3])
        print("\n\n")
    again = input("ulangi? (y or t):\t")
    i+=1
# mencari judul buku
urut = input("urutkan harga? (y/t)")
if urut == "y":
    print("mengurutkan harga "+"..."*3)
    buku = sort_harga(buku)

    for id in range(len(buku)):
        print("id: ", buku[id][0], "\tjudul: ", buku[id][1], "\tpenerbit: ", buku[id][2], "\tharga: ", buku[id][3])
        print("\n")

print("\n\n==== \t Mencari Nomor Buku \t ===\n")

cariID = int(input("masukkan nomor buku\t:"))

item = find_ID(buku, cariID)

if item == None:
    print("data tidak ditemukan\n")
else: 
    print("data ditemukan\t: ", item)

print("\n\n==== \t Mencari Judul Buku \t ===\n")
data_judul = Get_ByJudul(buku, input("masukkan judul\t: "))
print("data yang didapat\t: ", data_judul)