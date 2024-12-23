#Bai 54
import math
class Hhcn:
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
    def dttp(self):
        return (self.a + self.b)*2*self.h + (self.a*self.b*2)
    def thetich(self):
        return self.a*self.b*self.h
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n>0:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n>0:
                break
        except ValueError:
            print("Nhap lai")
    return n

def nhaplist(n):
    listhhcn = []
    for i in range(n):
        print('Nhap thong tin hinh chu nhat thu',i+1)
        print('Nhap chieu dai: ')
        a = nhapsothuc()
        print('Nhap chieu rong: ')
        b = nhapsothuc()
        print('Nhap chieu cao: ')
        h = nhapsothuc()
        hhcn = Hhcn(a,b,h)
        listhhcn.append(hhcn)
    return listhhcn

def hienthi(listhhcn, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Chieu dai', 'Chieu rong', 'Chieu cao','DTTP','The tich'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listhhcn[i].a, listhhcn[i].b, listhhcn[i].h, listhhcn[i].dttp(), listhhcn[i].thetich()))

def taotuple(listhhcn,n):
    listthetich = []
    for i in range(n):
        if listhhcn[i].thetich() > 50:
            listthetich.append(listhhcn[i])
    return tuple(listthetich)
def sapxepds(listhhcn,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listhhcn[j].thetich() < listhhcn[j+1].thetich():
                listhhcn[j], listhhcn[j+1] = listhhcn[j+1], listhhcn[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listhhcn, n)
def main():
    print('Nhap so hinh chu nhat: ')
    n = nhapsonguyen()
    listhhcn = nhaplist(n)
    hienthi(listhhcn, n)
    listthetich = taotuple(listhhcn, n)
    print('Hinh chu nhat co the tich > 50 la: ')
    hienthi(listthetich, len(listthetich))
    sapxepds(listhhcn, n)

if __name__ == '__main__':
    main()
