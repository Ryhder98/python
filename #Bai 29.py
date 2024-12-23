#Bai 29
import math
class Ts:
    def __init__ (self, ten, sbd, dt, dly, dh):
        self.ten = ten
        self.sbd = sbd
        self.dt = dt
        self.dly = dly
        self.dh = dh
    def tongdiem(self):
        return self.dt + self.dly + self.dh
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
            if n > 0 and n < 10:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaplist(n):
    list_ts = []
    for i in range(n):
        print(f'Nhap ten thi sinh thu {i+1}: ')
        ten = nhapten()
        print('Nhap so bao dan: ')
        sbd = nhapsonguyen()
        print('Nhap diem toan: ')
        dt = nhapsothuc()
        print('Nhap diem ly: ')
        dly = nhapsothuc()
        print('Nhap diem hoa: ')
        dh = nhapsothuc()
        ts = Ts(ten, sbd, dt, dly, dh)
        list_ts.append(ts)
    return list_ts
def hienthi(list_ts, n):
    print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten','So bao dan','Diem toan','Diem ly','Diem hoa','Tong diem'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(list_ts[i].ten,list_ts[i].sbd,list_ts[i].dt,list_ts[i].dly,list_ts[i].dh,list_ts[i].tongdiem()))
def maxdtoan(list_ts, n):
    dtoanmax = list_ts[0].dt
    for i in range(1, n):
        if list_ts[i].dt > dtoanmax:
            dtoanmax = list_ts[i].dt
    for i in range(n):
        if list_ts[i].dt == dtoanmax:
            print(f'Thi sinh co diem toan cao nhat la: {list_ts[i].ten} voi diem toan: {list_ts[i].dt}')
def sapxepdstang(list_ts, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if list_ts[i].tongdiem() > list_ts[j].tongdiem():
                list_ts[i], list_ts[j] = list_ts[j], list_ts[i]
    print('Danh sach sinh vien sau khi sap xep: ')
    hienthi(list_ts, n)
def main():
    print('Nhap vao so sv trong ds n: ')
    n = nhapsonguyen()
    list_ts = nhaplist(n)
    hienthi(list_ts, n)
    maxdtoan(list_ts, n)
    sapxepdstang(list_ts, n)
if __name__ == '__main__':
    main()
