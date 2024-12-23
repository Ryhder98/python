#Bai 49
import math
class MachLC:
    def __init__(self, ten, L, C):
        self.ten = ten
        self.L = L
        self.C = C
    def tinhF(self):
        return 1/(2*math.pi*math.sqrt(self.L*self.C))
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
    listmachLC = []
    for i in range(n):
        print('Nhap ten:')
        ten = nhapten()
        print('Nhap L:')
        L = nhapsothuc()
        print('Nhap C:')
        C = nhapsothuc()
        machLC = MachLC(ten, L, C)
        listmachLC.append(machLC)
    return listmachLC
def hienthi(listmachLC, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'L', 'C', 'Tan so'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listmachLC[i].ten, listmachLC[i].L, listmachLC[i].C, listmachLC[i].tinhF()))
def sapxepds(listmachLC, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listmachLC[j].tinhF() < listmachLC[j+1].tinhF():
                listmachLC[j], listmachLC[j+1] = listmachLC[j+1], listmachLC[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listmachLC, n)
def maxF(listmachLC, n):
    Fmax = listmachLC[0].tinhF()
    for i in range(1, n):
        if listmachLC[i].tinhF() > Fmax:
            Fmax = listmachLC[i].tinhF()
    for i in range(n):
        if listmachLC[i].tinhF() == Fmax:
            print(f'Mach LC co tan so lon nhat la: {listmachLC[i].ten} voi tan so lon nhat la: {Fmax}')
def main():
    print('Nhap vao so mach LC: ')
    n = nhapsonguyen()
    listmachLC = nhaplist(n)
    hienthi(listmachLC, n)
    sapxepds(listmachLC, n)
    maxF(listmachLC, n)

if __name__ == '__main__':
    main()