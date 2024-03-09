# program untuk menghitung tahun
# menggunakan library 'datetime'

# gmail = "bagasmipa3@gmail.com"

import datetime as dt

print("masukkan tanggal lahir anda:\n")
tgl = input("tanggal:\t")
bln = input("bulan:\t")
thn = input("tahun:\t")

born = dt.datetime(int(thn), int(bln), int(tgl))
today = dt.datetime.now()

delta = today - born
if delta.days/365 < 17:
    print("hanya untuk 17+")
else:
    print("welcome")