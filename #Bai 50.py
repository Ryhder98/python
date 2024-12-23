#Bai 50
import math
class MachRC:
    def __init__(self, ten, R, C):
        self.ten = ten
        self.R = R
        self.C = C
    def tinhF(self):
        return round(1/(2*math.pi*math.sqrt(self.R*self.C)),4)
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
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
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

def nhaplist(n):
    listmachRC = []
    for i in range(n):
        print('Nhap ten:')
        ten = nhapten()
        print('Nhap R:')
        R = nhapsothuc()
        print('Nhap C:')
        C = nhapsothuc()
        machRC = MachRC(ten, R, C)
        listmachRC.append(machRC)
    return listmachRC

def hienthi(listmachRC, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'R', 'C', 'Tan so'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listmachRC[i].ten, listmachRC[i].R, listmachRC[i].C, listmachRC[i].tinhF()))

def sapxepds(listmachRC, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listmachRC[j].R < listmachRC[j+1].R:
                listmachRC[j], listmachRC[j+1] = listmachRC[j+1], listmachRC[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listmachRC, n)

def maxF(listmachRC, n):
    Fmax = listmachRC[0].tinhF()
    for i in range(1, n):
        if listmachRC[i].tinhF() > Fmax:
            Fmax = listmachRC[i].tinhF()
    for i in range(n):
        if listmachRC[i].tinhF() == Fmax:
            print(f'Mach RC co dai thong lon nhat la: {listmachRC[i].ten} voi tan so lon nhat la: {Fmax}')

def main():
    print('Nhap vao so mach RC: ')
    n = nhapsonguyen()
    listmachRC = nhaplist(n)
    hienthi(listmachRC, n)
    sapxepds(listmachRC, n)
    maxF(listmachRC, n)

if __name__ == '__main__':
    main()