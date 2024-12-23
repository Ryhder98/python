#Bai 31
import math
class Kien:
    def __init__ (self, loai, ns, tg):
        self.loai = loai
        self.ns = ns
        self.tg = tg
    def sogram(self):
        return self.ns * self.tg

def nhaploai():
    while True:
        loai = input('Nhap: ')
        try:
            loai = str(loai)
            if loai.istitle() == True and loai.isalpha() == True:
                break
        except ValueError:
            print('Nhap lai')
    return loai
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
    list_kien = []
    for i in range(n):
        print('Nhap loai kien: ')
        loai = nhaploai()
        print('Nhap nang suat tha moi: ')
        ns = nhapsothuc()
        print('Nhap thoi gian: ')
        tg = nhapsothuc()
        kien = Kien(loai, ns, tg)
        list_kien.append(kien)
    return list_kien
def hienthi(list_kien, n):
    print('{:<20}{:<15}{:<15}{:<15}'.format('Loai','Nang suat','Thoi gian','So gram'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}'.format(list_kien[i].loai,list_kien[i].ns,list_kien[i].tg,list_kien[i].sogram()))
def minns(list_kien, n):
    nsmin = list_kien[0].ns
    for i in range(1, n):
        if list_kien[i].ns < nsmin:
            nsmin = list_kien[i].ns
    for i in range(n):
        if list_kien[i].ns == nsmin:
            print(f'Kien: {list_kien[i].loai} co nang suat tha moi nho nhat la: {list_kien[i].ns}')
def tonggram(list_kien, n):
    tong = 0
    for i in range(n):
        tong += list_kien[i].sogram()
    print(f'Tong so gram la: {tong}')
def main():
    print('Nhap so loai kien: ')
    n = nhapsonguyen()
    list_kien = nhaplist(n)
    hienthi(list_kien, n)
    minns(list_kien, n)
    tonggram(list_kien, n)

if __name__ == '__main__':
    main()