#Bai 43
import math
class Tgv:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def canhhuyen(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2), 2)
    def tinhgoc(self):
        g1 = round(math.degrees(math.atan(self.a/self.b)),2)
        g2 = round(math.degrees(math.atan(self.b/self.a)),2)
        g3 = 90
        return g1, g2, g3
    def dt(self):
        return self.a * self.b
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n >0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n >0:
                break
        except ValueError:
            print('Nhap lai')
    return n

def nhaplist(n):
    listtgv = []
    for i in range(n):
        print('Nhap canh a: ')
        a = nhapsothuc()
        print('Nhap canh b: ')
        b = nhapsothuc()
        tgv = Tgv(a, b)
        listtgv.append(tgv)
    return listtgv
def hienthi(listtgv, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('A', 'B', 'Canh huyen', 'Goc 1', 'Goc 2', 'Goc 3', 'Dien tich'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listtgv[i].a, listtgv[i].b, listtgv[i].canhhuyen(), listtgv[i].tinhgoc()[0], listtgv[i].tinhgoc()[1], listtgv[i].tinhgoc()[2], listtgv[i].dt()))
def sxds(listtgv, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listtgv[j].dt() < listtgv[j+1].dt():
                listtgv[j], listtgv[j+1] = listtgv[j+1], listtgv[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listtgv, n)
def tupledt(listtgv, n):
    maxdt = listtgv[0].dt()
    dsdtmax = []
    for i in range(1, n):
        if listtgv[i].dt() > maxdt:
            maxdt = listtgv[i].dt()
    for i in range(n):
        if listtgv[i].dt() == maxdt:
            dsdtmax.append(listtgv[i].dt())
    tupletgv = tuple(dsdtmax)
    print('Tuple tgv co dien tich lon nhat: ', tupletgv)
def main():
    print('Nhap so tgv: ')
    n = nhapsonguyen()
    listtgv = nhaplist(n)
    hienthi(listtgv, n)
    sxds(listtgv, n)
    tupledt(listtgv, n)
if __name__ == '__main__':
    main()