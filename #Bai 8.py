#Bai 8
import math
class Hhcn:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def dtxq(self):
        return (self.a + self.b)*2*self.h
    def thetich(self):
        return self.a * self.b * self.h
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
def nhaphhcn(n):
    list_hhcn = []
    for i in range(n):
        print(f'Nhap chieu dai hinh hop chu nhat thu {i+1}: ')
        a = nhapsothuc()
        print(f'Nhap chieu rong hinh hop chu nhat thu {i+1}: ')
        b = nhapsothuc()
        print(f'Nhap chieu cao hinh hop chu nhat thu {i+1}: ')
        h = nhapsothuc()
        hhcn = Hhcn(a, b, h)
        list_hhcn.append(hhcn)
    return list_hhcn
def hienthi(list_hhcn, n):
    for i in range (n):
        print(f'Hinh hop chu nhat thu ',(i+1),' co chieu dai la: ',(list_hhcn[i].a),' chieu rong la: ', list_hhcn[i].b,' va chieu cao la: ', list_hhcn[i].h, ' co dien tich xung quanh la: ', list_hhcn[i].dtxq())
def tongthetich(list_hhcn, n):
    t = 0
    for i in range(n):
        t = t + list_hhcn[i].thetich()
    print(f'Tong the tich ',n, 'hinh hop chu nhat la: ', t)
def maxthetich(list_hhcn, n):
    thetichmax = list_hhcn[0].thetich()
    for i in range (1,n):
        if list_hhcn[i].thetich() > thetichmax:
            thetichmax = list_hhcn[i].thetich()
    for i in range (n):
        if list_hhcn[i].thetich() == thetichmax:
            print(f'Hinh hop chu nhat thu ',(i+1), 'co the tich lon nhat la: ', list_hhcn[i].thetich())
def main():
    print('Nhap so hinh hop chu nhat: ')
    n = nhapsonguyen()
    list_hhcn = nhaphhcn(n)
    hienthi(list_hhcn, n)
    tongthetich(list_hhcn, n)
    maxthetich(list_hhcn, n)
if __name__ == "__main__":
    main()