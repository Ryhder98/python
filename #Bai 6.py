#Bai 6
import math
class Tgv:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def canhhuyen(self):
        return math.sqrt(self.a**2 + self.b**2)
    def tinhcvi(self):
        return self.a + self.b + math.sqrt(self.a**2 + self.b**2)
    def tinhdt(self):
        return 0.5*self.a*self.b
def nhapsonguyen():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            if n>0:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n>0:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhaptgv(n):
    list_tgv = []
    for i in range (n):
        print(f'Nhap chieu dai canh goc vuong thu nhat cua tam giac thu {i+1}: ')
        a = nhapsothuc()
        print(f'Nhap chieu dai canh goc vuong thu hai cua tam giac thu {i+1}: ')
        b = nhapsothuc()
        tgv = Tgv(a,b)
        list_tgv.append(tgv)
    return list_tgv
def hienthi(list_tgv, n):
    for i in range (n):
        print(f'Tam giac vuong thu ',(i+1),' co 2 canh goc vuong lan luot la: ',(list_tgv[i].a, list_tgv[i].b),' va canh huyen la: ', list_tgv[i].canhhuyen())
def tongdt(list_tgv, n):
    t = 0
    for i in range (n):
        t = t + list_tgv[i].tinhdt()
    print(f'Tong dien tich ',n, 'tam giac vuong la: ', t)
def maxcvi(list_tgv, n):
    cvimax = list_tgv[0].tinhcvi()
    for i in range (1,n):
        if list_tgv[i].tinhcvi() > cvimax:
            cvimax = list_tgv[i].tinhcvi()
    for i in range (n):
        if list_tgv[i].tinhcvi() == cvimax:
            print(f'Hinh tam giac vuong thu ',(i+1), 'co chu vi lon nhat la: ', list_tgv[i].tinhcvi())
def main():
    print('Nhap vao so hinh tam giac vuong: ')
    n = nhapsonguyen()
    list_tgv = nhaptgv(n)
    hienthi(list_tgv, n)
    tongdt(list_tgv, n)
    maxcvi(list_tgv, n)
if __name__ == "__main__":
    main()