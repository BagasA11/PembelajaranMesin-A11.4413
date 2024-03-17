import datetime
import string
import random

templ = {
    "judul":"",
    "isi":"",
    "author":"",
    "created_at":datetime.datetime.now()
}

# create null dictionary from template
post = dict.fromkeys(templ.keys())

list = {}

while True:
    # generate random key
    ID = "".join(random.choice(string.ascii_uppercase) for i in range(7))
    
    judul = input("input judul\t: ")
    isi = input("input isi\t: ")
    author = input("input author\t: ")
    created_at = datetime.datetime.now()

    # insert input data to post dictionaries
    # {judul, isi, autor, created_at}
    post["judul"] = judul
    post["isi"] = isi
    post["author"] = author
    post["created_at"] = created_at
    
    # add post data as list item
    # {id:{}}
    list[ID] = post.copy()
    
    # loop exit
    exit = int(input("exit?\t press (1) to exit:"))
    if exit == 1 :
        break

print("\n\n")

print(f"{"="*70}")
# print out list 
print(f"id \t judul{'\t'*2} isi{"\t"*4} author{"\t"*2} timestamp", "\n")
# {xxx:{}}

# {xx1:{}, x1x:{}}

for k in list:
    prtout = ""
    prtout = k
    v = list[k]
    for k2 in v:
        prtout = prtout + f" {v[k2]}\t"
    
    print(prtout)
    print("\n")
    