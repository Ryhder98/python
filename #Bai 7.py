#Bai 7
import math
class Tgd:
    def __init__(self, a):
        self.a = a
    def duongcao(self):
        return math.sqrt(self.a**2 - (0.5*self.a)**2)
    def tinhcvi(self):
        return self.a*3
    def tinhdt(self):
        return (self.a**2*math.sqrt(3))/4
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
def nhaptgd(n):
    list_tgd = []
    for i in range (n):
        print(f'Nhap chieu dai canh cua tam giac deu thu {i+1}: ')
        a = nhapsothuc()
        tgd = Tgd(a)
        list_tgd.append(tgd)
    return list_tgd
def hienthi(list_tgd, n):
    for i in range (n):
        print(f'Tam giac vuong thu ',(i+1),' co canh la: ',(list_tgd[i].a),' va duong cao la: ', list_tgd[i].duongcao())
def tongdt(list_tgd, n):
    t = 0
    for i in range (n):
        t = t + list_tgd[i].tinhdt()
    print(f'Tong dien tich ',n, 'tam giac deu la: ', t)
def maxcvi(list_tgd, n):
    cvimax = list_tgd[0].tinhcvi()
    for i in range (1,n):
        if list_tgd[i].tinhcvi() > cvimax:
            cvimax = list_tgd[i].tinhcvi()
    for i in range (n):
        if list_tgd[i].tinhcvi() == cvimax:
            print(f'Hinh tam giac vuong thu ',(i+1), 'co chu vi lon nhat la: ', list_tgd[i].tinhcvi())
def main():
    print('Nhap so hinh tam giac deu: ')
    n = nhapsonguyen()
    list_tgd = nhaptgd(n)
    hienthi(list_tgd, n)
    tongdt(list_tgd, n)
    maxcvi(list_tgd, n)
if __name__ == "__main__":
    main()