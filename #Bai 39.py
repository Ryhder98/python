#Bai 39
import math
class Hanghoa:
    def __init__(self, ten, gia, sl):
        self.ten = ten
        self.gia = gia
        self.sl = sl
    def tongtien(self):
        return self.gia * self.sl
def nhapten():
    while True:
        ten = input('Nhap: ')
        try:
            ten = str(ten)
            if ten.isalpha() == True and ten.istitle() == True:
                break
        except ValueError:
            print('Nhap lai')
    return ten
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n

def nhaplist(n):
    listhh = []
    for i in range(n):
        print('Nhap ten hang hoa: ')
        ten = nhapten()
        print('Nhap gia: ')
        gia = nhapsothuc()
        print('Nhap so luong: ')
        sl = nhapsonguyen()
        hh = Hanghoa(ten, gia, sl)
        listhh.append(hh)
    return listhh

def hienthi(listhh, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'Gia', 'So luong', 'Tong tien'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listhh[i].ten, listhh[i].gia, listhh[i].sl, listhh[i].tongtien()))
def sapxepds(listhh, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if listhh[i].tongtien() > listhh[j].tongtien():
                listhh[i], listhh[j] = listhh[j], listhh[i]
    return listhh
def dicthanghoa(listhh,n):
    dict = {}
    for hh in listhh:
        dict[hh.ten] = hh.tongtien()
    print(f'Dictionary của hàng hóa là: {dict}')

def main():
    print('Nhap so hang hoa: ')
    n = nhapsonguyen()
    listhh = nhaplist(n)
    hienthi(listhh, n)
    listhh = sapxepds(listhh, n)
    print('Danh sach sau khi sap xep:')
    hienthi(listhh, n)
    dicthanghoa(listhh, n)

if __name__ == '__main__':
    main()