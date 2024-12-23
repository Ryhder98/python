#Bai 5
import math
class Htg:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def tinhcvi(self):
        return self.a + self.b + self.c
    def tinhdt(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
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
def nhaptg(n):
    list_tg = []
    for i in range (n):
        print(f'Nhap vao canh thu nhat cua tam giac thu {i+1}: ')
        a = nhapsothuc()
        print(f'Nhap vao canh thu hai cua tam giac thu {i+1}: ')
        b = nhapsothuc()
        print(f'Nhap vao canh thu ba cua tam giac thu {i+1}: ')
        c = nhapsothuc()
        htg = Htg(a, b ,c)
        list_tg.append(htg)
    return list_tg
def hienthi(list_tg, n):
    for i in range (n):
        print(f'Hinh tam giac thu ',(i+1),' co 3 canh lan luot la: ',(list_tg[i].a, list_tg[i].c, list_tg[i].b),' va co chu vi la: ', list_tg[i].tinhcvi())
def tongdt(list_tg, n):
    t = 0
    for i in range (n):
        t = t + list_tg[i].tinhdt()
    print(f'Tong dien tich ',n,' tam gia la: ',t)
def mindt(list_tg, n):
    dtmin = list_tg[0].tinhdt()
    for i in range (1, n):
        if list_tg[i].tinhdt() < dtmin:
            dtmin = list_tg[i].tinhdt()
    for i in range (n):
        if list_tg[i].tinhdt() == dtmin:
            print(f'Hinh tam giac thu ', (i+1),' co dien tich nho nhat la: ', list_tg[i].tinhdt())
def main():
    print('Nhap so hinh tam giac: ')
    n = nhapsonguyen()
    list_tg = nhaptg(n)
    hienthi(list_tg, n)
    tongdt(list_tg, n)
    mindt(list_tg, n)
if __name__ == "__main__":
    main()