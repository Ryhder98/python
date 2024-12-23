#Bai 26
import math
class Sinhvien:
    def __init__(self, ten, msv, diemtt, diemda):
        self.ten = ten
        self.msv = msv
        self.diemtt = diemtt
        self.diemda = diemda
    def diemtb(self):
        return (7*self.diemtt + 8*self.diemda)/15
def nhapten():
    while True:
        ten = input('Nhap ten: ')
        try:
            ten = str(ten)
            if ten.istitle() == True and ten.isalpha() == True:
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

def nhaplist_sv(n):
    list_sv = []
    for i in range(n):
        print(f'Nhap ten sinh vien thu {i+1}: ')
        ten = nhapten()
        print('Nhap ma so sinh vien: ')
        msv = nhapsonguyen()
        print('Nhap diem thuyet trinh: ')
        diemtt = nhapsothuc()
        print('Nhap diem do an: ')
        diemda = nhapsothuc()
        sinhvien = Sinhvien(ten, msv, diemtt, diemda)
        list_sv.append(sinhvien)
    return list_sv
def hienthi(list_sv, n):
    print('{:<20}{:<15}{:<15}{:<15}{:<15}'.format('Ten','MSV','Diem thuc tap','Diem do an','Diem trung binh'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}{:<15}'.format(list_sv[i].ten,list_sv[i].msv,list_sv[i].diemtt,list_sv[i].diemda,list_sv[i].diemtb()))
def sapxep(list_sv, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if list_sv[i].diemtb() < list_sv[j].diemtb():
                list_sv[i], list_sv[j] = list_sv[j], list_sv[i]
def xoasv(list_sv, n):
    i = 0
    while i < len(list_sv):
        if list_sv[i].diemtb() < 4:
            del list_sv[i]
        else:
            i += 1
    n = len(list_sv)
    return n, list_sv
def main():
    print('Nhap so luong sinh vien: ')
    n = nhapsonguyen()
    list_sv = nhaplist_sv(n)
    hienthi(list_sv, n)
    sapxep(list_sv, n)
    m, sv1 = xoasv(list_sv, n)
    print('Danh sach sinh vien sau khi xoa: ')
    hienthi(sv1, m)            
if __name__ == "__main__":
    main()
