#Bai 38
import math
class Congnhan:
    def __init__(self, ten, cs, tg, tcong):
        self.ten = ten
        self.cs = cs
        self.tg = tg
        self.tcong = tcong
    def luong(self):
        return self.cs * self.tg * self.tcong
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
def nhaplist(n):
    listcn = []
    for i in range(n):
        print('Nhap ten cong nhan: ')
        ten = nhapten()
        print('Nhap cong suat: ')
        cs = nhapsothuc()
        print('Nhap thoi gian: ')
        tg = nhapsothuc()
        print('Nhap tong cong: ')
        tcong = nhapsothuc()
        cn = Congnhan(ten, cs, tg, tcong)
        listcn.append(cn)
    return listcn

def hienthi(listcn, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'Cong suat', 'Thoi gian', 'Tien cong', 'Luong'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listcn[i].ten, listcn[i].cs, listcn[i].tg, listcn[i].tcong, listcn[i].luong()))
def maxcong(listcn, n):
    congmax = listcn[0].tcong
    for i in range(1, n):
        if listcn[i].tcong > congmax:
            congmax = listcn[i].tcong
    for i in range(n):
        if listcn[i].tcong == congmax:
            print('Cong nhan co tong cong lon nhat la: ', listcn[i].ten, "voi tien cong la: ", listcn[i].tcong)
def tongluong(listcn, n):
    t = 0
    for i in range(n):
        t += listcn[i].luong()
    print('Tong luong: ', t)

def main():
    print('Nhap so cong nhan: ')
    n = nhapsonguyen()
    listcn = nhaplist(n)
    hienthi(listcn, n)
    maxcong(listcn, n)
    tongluong(listcn, n)

if __name__ == '__main__':
    main()