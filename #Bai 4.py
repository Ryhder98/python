#Bai 4
import math
class Htv:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def canhcheo(self):
        return math.sqrt(self.b**2 + (self.c - self.a)**2)
    def tinhcvi(self):
        return self.a + self.b + self.c + math.sqrt(self.b**2 + (self.c - self.a)**2)
    def tinhdt(self):
        return 0.5*self.b*(self.a + self.c)
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
def nhaphtv(n):
    list_htv = []
    for i in range (n):
        print(f'Nhap vao day nho cua hinh thang vuong thu {i+1}')
        a = nhapsothuc()
        print(f'Nhap vao canh ben vuong goc voi hai day cua hinh thang vuong thu {i+1}')
        b = nhapsothuc()
        print(f'Nhap vao day lon cua hinh thang vuong thu {i+1}')
        c = nhapsothuc()
        htv = Htv(a, b, c)
        list_htv.append(htv)
    return list_htv
def hienthi(list_htv, n):
    for i in range (n):
        print(f'Hinh thang vuong thu ',(i+1),' co day nho, day lon va canh ben vuong goc la: ',(list_htv[i].a, list_htv[i].c, list_htv[i].b),' va co chu vi la: ', list_htv[i].tinhcvi())
def tongdt(list_htv, n):
    t = 0
    for i in range(n):
        t = t + list_htv[i].tinhdt()
    print(f'Tong dien tich cua ',n,' hinh thang vuong la: ', t)
def maxdt(list_htv, n):
    dtmax = list_htv[0].tinhdt()
    for i in range (1,n):
        if list_htv[i].tinhdt() > dtmax:
            dtmax = list_htv[i].tinhdt()
    for i in range (n):
        if list_htv[i].tinhdt() == dtmax:
            print(f'Hinh thang vuong thu',(i+1),' co dien tich lon nhat la: ',list_htv[i].tinhdt())
def main():
    print('Nhap vao so hinh thang vuong: ')
    n = nhapsonguyen()
    list_htv = nhaphtv(n)
    hienthi(list_htv, n)
    tongdt(list_htv, n)
    maxdt(list_htv, n)
if __name__ == "__main__":
    main()