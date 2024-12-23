#Bai 45
import math
class Vatnuoi:
    def __init__(self, ten, sl, luongthucan, songaynuoi, dongiathucan):
        self.ten = ten
        self.sl = sl
        self.luongthucan = luongthucan
        self.songaynuoi = songaynuoi
        self.dongiathucan = dongiathucan
    def chiphithucan(self):
        return round(self.luongthucan * self.dongiathucan * self.songaynuoi, 2)
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
            if n > 0:
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
    listvn = []
    print('Nhap don gia thuc an:')
    dongiathucan = nhapsothuc()
    for i in range(n):
        print('Nhap ten vat nuoi:')
        ten = nhapten()
        print('Nhap so luong:')
        sl = nhapsothuc()
        print('Nhap luong thuc an:')
        luongthucan = nhapsothuc()
        print('Nhap so ngay nuoi:')
        songaynuoi = nhapsothuc()
        vn = Vatnuoi(ten, sl, luongthucan, songaynuoi, dongiathucan)
        listvn.append(vn)
    return listvn

def hienthi(listvn, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten VN', 'So luong', 'Luong thuc an', 'So ngay nuoi', 'Don gia thuc an', 'Chi phi thuc an'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listvn[i].ten, listvn[i].sl, listvn[i].luongthucan, listvn[i].songaynuoi, listvn[i].dongiathucan, listvn[i].chiphithucan()))

def tongchiphi(listvn, n):
    t = 0
    for i in range(n):
        t += listvn[i].chiphithucan()
    print(f'Tong chi phi thuc an: {t}')
def demtuple(listvn, n):
    dem = 0
    dsvn = []
    minchiphi = listvn[0].chiphithucan()
    for i in range(1, n):
        if listvn[i].chiphithucan() < minchiphi:
            minchiphi = listvn[i].chiphithucan()
    for i in range(n):
        if listvn[i].chiphithucan() == minchiphi:
            dem += 1
            dsvn.append((listvn[i].ten, listvn[i].chiphithucan()))
    return dsvn, dem

def main():
    print('Nhap so luong vat nuoi:')
    n = nhapsonguyen()
    listvn = nhaplist(n)
    hienthi(listvn, n)
    tongchiphi(listvn, n)
    dsvn, dem = demtuple(listvn, n)
    print(f'So vat nuoi co chi phi thuc an nho nhat la: {dem}')
    print(f'Vat nuoi co chi phi thuc an nho nhat la: {dsvn}')

if __name__ == '__main__':
    main()