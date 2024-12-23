#Bai 47
import math
class Bodem:
    def __init__(self, ten, Kd, loaiFF):
        self.ten = ten
        self.Kd = Kd
        self.loaiFF = loaiFF
    def tinhsoFF(self):
        if self.Kd == 0:
            return 0
        else:
            return math.log2(self.Kd)
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapkd():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            break
        except ValueError:
            print("Nhap lai")
    return n
def nhapten():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isalpha() == True and n.istitle() == True:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhaploai():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isupper() == True:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhaplist(n):
    listBodem = []
    for i in range(n):
        print('Nhap ten bo dem:')
        ten = nhapten()
        print('Nhap Kd:')
        Kd = nhapkd()
        print('Nhap loai FF:')
        loaiFF = nhaploai()
        bodem = Bodem(ten, Kd, loaiFF)
        listBodem.append(bodem)
    return listBodem
def hienthi(listBodem, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten bo dem', 'Kd', 'Loai FF', 'So FF'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listBodem[i].ten, listBodem[i].Kd, listBodem[i].loaiFF, listBodem[i].tinhsoFF()))
def sapxepds(listBodem,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listBodem[j].Kd < listBodem[j+1].Kd:
                listBodem[j], listBodem[j+1] = listBodem[j+1], listBodem[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listBodem, n)
def xoads(listBodem, n):
    i = 0
    while i < len(listBodem):
        if listBodem[i].Kd == 0:
            del listBodem[i]
        else:
            i += 1
    n = len(listBodem)
    return n, listBodem
def main():
    print('Nhap vao so bo dem: ')
    n = nhapsonguyen()
    listBodem = nhaplist(n)
    hienthi(listBodem, n)
    sapxepds(listBodem, n)
    m, listBodem1 = xoads(listBodem, n)
    print('Danh sach sau khi xoa: ')
    hienthi(listBodem1, m)

if __name__ == '__main__':
    main()

