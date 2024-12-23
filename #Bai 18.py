#Bai 18
import math
import re
class Nhanvien:
    def __init__(self, hoten, sonam, luongcb, hso):
        self.hoten = hoten
        self.sonam = sonam
        self.luongcb = luongcb
        self.hso = hso
    def luong(self):
        return (self.luongcb * self.hso) + self.sonam * (self.luongcb/10)
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
        paterm = r'^[a-zA-Z\s]+$'
        n = input('Nhap: ')
        if re.match(paterm, n):
            break
        else:
            print('Nhap lai')
    return n
def nhaplist(n):
    list_nv = []
    for i in range(n):
        print(f'Nhap thong tin nhan vien thu {i+1}: ')
        print('Nhap ho va ten: ')
        hoten = nhapten()
        print('Nhap so nam cong tac: ')
        sonam = nhapsonguyen()
        print('Nhap luong co ban: ')
        luongcb = nhapsothuc()
        print('Nhap he so luong: ')
        hso = nhapsothuc()
        nhanvien = Nhanvien(hoten, sonam, luongcb, hso)
        list_nv.append(nhanvien)
    return list_nv
def hienthi(list_nv, n):
    print('{:<20}{:<20}{:<15}{:<15}{:<15}'.format('Ho ten','So nam cong tac','Luong co ban','He so luong','Luong'))
    for i in range(n):
        print('{:<20}{:<20}{:<15}{:<15}{:<15}'.format(list_nv[i].hoten,list_nv[i].sonam,list_nv[i].luongcb,list_nv[i].hso,list_nv[i].luong()))
def maxnam(list_nv, n):
    nammax = list_nv[0].sonam
    for i in range(1,n):
        if list_nv[i].sonam > nammax:
            nammax = list_nv[i].sonam
    for i in range(n):
        if list_nv[i].sonam == nammax:
            print(f'Nhan vien co nam cong tac lon nhat la: {list_nv[i].hoten}')
def tongluong(list_nv, n):
    tong = 0
    for i in range(n):
        tong += list_nv[i].luong()
    print(f'Tong luong cua cac nhan vien la: {tong}')
def main():
    print('Nhap so luong nhan vien: ')
    n = nhapsonguyen()
    list_nv = nhaplist(n)
    hienthi(list_nv, n)
    maxnam(list_nv, n)
    tongluong(list_nv, n)
if __name__ == "__main__":
    main()