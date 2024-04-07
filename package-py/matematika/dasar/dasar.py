def total(*args):
    total = 0
    for i in range(args):
        total += i
    return total

def tambah(a, b):
    return a + b

def kurang(a, b):
    return tambah(a, (b * -1))

def kali(*args):
    kali = 1
    for i in args:
        kali *= i
    return kali

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

