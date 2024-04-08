
# import uuid
import os
from pathlib import Path
# from os import path

dir = str("./file/")
# filename = str.format("{}.txt", uuid.uuid1())
# dirfile = dir + filename


def writefile():
    print(3*"=", " daftar file ", 3*"=")
    
    listdir = os.listdir(dir)
    
    for i in range(len(listdir)):
        print(f"{i+1}. {listdir[i]}")
    print(f"{len(listdir) + 1}. buat file baru")
    
    pil = int( input("pilih angka dari daftar file: "))
    if pil <= len(listdir) and pil > 0 :
        print(f"membuka file ke-{pil}: {listdir[pil-1]}")
        file_local = listdir[pil - 1]
        with open(dir+file_local, "w") as f:
            content = input("tulis text baru:\n")
            f.write(content)
    
    else:
        # file name
        name = input("tulis nama file baru:\t")
        while (os.path.exists(dir+name)):
            print("file is already exist")
            name = input("tulis nama file baru:\t")
        
        with open(dir+name, "w") as f:
            content = input("input text:\n")
            f.write(content)
    # print(os.path.exists(dir+listdir[0]))

def readFile():
    print(3*"=", " daftar file ", 3*"=")    
    listdir = os.listdir(dir)
    
    for i in range(len(listdir)):
        print(f"{i+1}. {listdir[i]}")
    pil = int(input(f"pilih angka 1 - {len(listdir)}:\t"))
    
    if pil >0 and pil <= len(listdir):
        print(f"membuka file ke-{pil}:\t {listdir[pil-1]}")
        with open(dir+listdir[pil-1], "r") as f:
            print(f.read())

    else:
        readFile()

def removeFile():
    print(3*"=", " daftar file ", 3*"=")    
    listdir = os.listdir(dir)
    
    for i in range(len(listdir)):
        print(f"{i+1}. {listdir[i]}")
        
    pil = int(input(f"pilih file 1 - {len(listdir)} yang ingin di hapus: "))
    while (not os.path.exists(dir+listdir[pil - 1])):
        print(f"file {listdir[pil - 1]} is not exist")
        pil = int(input(f"pilih file 1 - {len(listdir)} yang ingin di hapus: "))
    
    print(f"menghapus file {listdir[pil - 1]}")
    os.remove(dir+listdir[pil - 1])

def exit():
    print("bye")
    return