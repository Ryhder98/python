#Bai 51
import math
class Ga:
    def __init__(self, loai, tuoi, gioitinh, sl):
        self.loai = loai
        self.tuoi = tuoi
        self.gioitinh = gioitinh
        self.sl = sl
        self.trunggaRi = 0
        self.trunggaLai = 0
        self.trunggaKhac = 0
    def sotrung(self):
        if self.loai == 'Ri' and self.tuoi > 45 and self.gioitinh == 'Mai':
            self.trunggaRi += 1
        elif self.loai == 'Lai' and self.tuoi > 30 and self.gioitinh == 'Mai':
            self.trunggaLai += 2
        elif self.tuoi > 35 and self.gioitinh == 'Mai':
            self.trunggaRi += 0
            self.trunggaLai += 0
            self.trunggaKhac += 1
        return self.trunggaRi, self.trunggaLai, self.trunggaKhac
def nhapsonguyen():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            if n>0:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhapten():
    while True:
        n = input('Thong tin can nhap : ')
        try:
            n = str(n)
            if n.istitle()==True and n.isalpha() == True:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhaplist(n):
    listga =[]
    for i in range(n):
        print('Nhap loai ga : ')
        loai = nhapten()
        print('Nhap tuoi : ')
        tuoi = nhapsonguyen()
        print('Nhap gioi tinh : ')
        gioitinh = nhapten()
        print('Nhap so luong : ')
        sl = nhapsonguyen()
        ga = Ga(loai,tuoi,gioitinh,sl)
        listga.append(ga)
    return listga

def hienthi(listga,n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Loai','Tuoi','Gioi tinh','So luong','So trung Ri', 'So trung Lai', 'So trung Khac'))
    for i in range(n):
        trunggaRi, trunggaLai, trunggaKhac = listga[i].sotrung()
        print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listga[i].loai,listga[i].tuoi,listga[i].gioitinh,listga[i].sl,trunggaRi, trunggaLai, trunggaKhac))
def tongsotrung(listga, n):
    tong = 0
    
    for i in range(n):
        trunggaRi, trunggaLai, trunggaKhac = listga[i].sotrung()
        tong += trunggaLai + trunggaRi + trunggaKhac
    return tong

def dem(listga, n):
    dem = 0
    demtrung = 0
    for i in range(n):
        if listga[i].loai == 'Ri' and listga[i].gioitinh == 'Trong':
            dem += listga[i].sl
    for i in range(n):
        trunggaRi, trunggaLai, trunggaKhac = listga[i].sotrung()
        if listga[i].loai == 'Ri' and listga[i].gioitinh == 'Mai':
            demtrung += trunggaRi
    print(f'So con ga trong ri la: {dem} va co {demtrung} trung ga ri')
    
def main():
    print('Nhap vao so ga: ')
    n = nhapsonguyen()
    listga = nhaplist(n)
    hienthi(listga,n)
    tong = tongsotrung(listga,n)
    print(f'Tong so trung la: {tong}')
    dem(listga,n)

if __name__ == '__main__':
    main()