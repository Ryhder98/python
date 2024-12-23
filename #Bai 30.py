#Bai 30
import math
class Ong:
    def __init__ (self, loai, vt, tg):
        self.loai = loai
        self.vt = vt
        self.tg = tg
    def qd(self):
        return self.vt * self.tg
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
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n

def nhaplist(n):
    list_ong = []
    for i in range(n):
        print(f'Nhap thong tin con ong thu {i+1}: ')
        print('Nhap loai: ')
        loai = nhapten()
        print('Nhap van toc: ')
        vt = nhapsothuc()
        print('Nhap thoi gian: ')
        tg = nhapsothuc()
        ong = Ong(loai, vt, tg)
        list_ong.append(ong)
    return list_ong
def hienthi(list_ong, n):
    print('{:<20}{:<15}{:<15}{:<15}'.format('Ten','Loai','Van toc','Thoi gian'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}'.format(list_ong[i].loai,list_ong[i].vt,list_ong[i].tg,list_ong[i].qd()))
def fastest(list_ong, n):
    maxspeed = list_ong[0].vt
    for i in range(1, n):
        if list_ong[i].vt > maxspeed:
            maxspeed = list_ong[i].vt
    for i in range(n):
        if list_ong[i].vt == maxspeed:
            print(f'Con ong: {list_ong[i].loai} co van toc lon nhat la: {list_ong[i].vt}')
def demong(list_ong, n):
    dem = 0
    dai = list_ong[0].qd()
    for i in range(1,n):
        if list_ong[i].qd() > dai:
            dai = list_ong[i].qd()
    for i in range(n):
        if list_ong[i].qd() == dai:
            dem += 1
    print(f'Co {dem} con ong co quang duong dai nhat la: {dai}')
def main():
    print('Nhap so loai ong: ')
    n = nhapsonguyen()
    list_ong = nhaplist(n)
    hienthi(list_ong, n)
    fastest(list_ong, n)
    demong(list_ong, n)

if __name__ == '__main__':
    main()
