import os


os.system("cls")

buku_template = {
    "id":0,
    "judul":"",
    "thn_terbit":0000
}

buku = {}
list_buku = []

buku = dict.fromkeys(buku_template.keys())
# return all keys = buku.keys()
# return all values = buku.values()
# for book in buku.values():
#     print(book)
print(buku.values())
print(f"{'masukkan data':^8}\t:\n")

y = int(1)
while y == 1:

    id_buku = int(input("masukkan id buku (1/999)\t: "))
    Judul = input("masukkan judul buku\t: ")
    tahun_terbit = int(input("masukkan tahun terbit buku (yyyy)\t: "))

    buku.update({"id":id_buku})
    buku.update({"judul":Judul})
    buku.update({"thn_terbit":tahun_terbit})
    print(buku, "\n")
    # insert buku item to list_buku
    list_buku.insert(len(list_buku), buku.copy())
    
    print(f"list_buku = {list_buku}")
    y = int(input("ulangi? (0/1)\t: "))

# [{}]
print(f"list_buku = {list_buku}")
print(f"{'id':<2} {'judul':<10} {'tahun_terbit':<40}", "\n")
for item in list_buku:
    print(item["id"], "\n")
# print(f"{buku.get("id"):^2} {buku.get("judul"):^10} {buku.get("thn_terbit"):^40}", "\n")




