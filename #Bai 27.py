#Bai 27
import math
class Hs:
    def __init__(self, ten, msv, dt, dv, da):
        self.ten = ten
        self.msv = msv
        self.dt = dt
        self.dv = dv
        self.da = da
    def tongdiem(self):
        return self.dt + self.dv + self.da
def nhapten():
    while True:
        ten = input('Nhap: ')
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
            if n > 0 and n < 10:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaplist(n):
    list_hs = []
    for i in range(n):
        print(f'Nhap ten hoc sinh thu {i+1}: ')
        ten = nhapten()
        print('Nhap ma so hoc sinh: ')
        msv = nhapsonguyen()
        print('Nhap diem toan: ')
        dt = nhapsothuc()
        print('Nhap diem van: ')
        dv = nhapsothuc()
        print('Nhap diem an: ')
        da = nhapsothuc()
        hs = Hs(ten, msv, dt, dv, da)
        list_hs.append(hs)
    return list_hs

def hienthi(list_hs, n):
    print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten','MSV','Diem toan','Diem van','Diem an','Tong diem'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(list_hs[i].ten,list_hs[i].msv,list_hs[i].dt,list_hs[i].dv,list_hs[i].da,list_hs[i].tongdiem()))
def sapxep(list_hs, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if list_hs[i].tongdiem() < list_hs[j].tongdiem():
                list_hs[i], list_hs[j] = list_hs[j], list_hs[i]
def demsv(list_hs, n):
    dem = 0
    for i in range(n):
        if list_hs[i].tongdiem() >= 15:
            dem += 1
    return dem

def main():
    print('Nhap so luong hoc sinh: ')
    n = nhapsonguyen()
    list_hs = nhaplist(n)
    hienthi(list_hs, n)
    sapxep(list_hs, n)
    print('Danh sach hoc sinh sau khi sap xep: ')
    hienthi(list_hs, n)
    print(f'So hoc sinh co tong diem >= 15: {demsv(list_hs, n)}')

if __name__ == "__main__":
    main()
    