#Bai 40
import math
class Linhkien:
    def __init__(self, ten, gia, trangthai):
        self.ten = ten
        self.gia = gia
        self.trangthai = trangthai
    def dinhgia(self):
        trangthai = {'Hong': 0, 'Cu': 0.5, 'Moi': 1}
        if self.trangthai not in trangthai:
            raise ValueError("Trang thai khong hop le")
        giatri = (self.gia * trangthai[self.trangthai])
        return giatri
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
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isalpha() == True and n.istitle() == True:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaplist(n):
    listlinhkien = []
    for i in range(n):
        print('Nhap ten linh kien: ')
        ten = nhapten()
        print('Nhap gia: ')
        gia = nhapsothuc()
        print('Nhap trang thai: ')
        trangthai = nhapten()
        linhkien = Linhkien(ten, gia, trangthai)
        listlinhkien.append(linhkien)
    return listlinhkien

def hienthi(listlinhkien, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'Gia', 'Trang thai', 'Tong tien'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listlinhkien[i].ten, listlinhkien[i].gia, listlinhkien[i].trangthai, listlinhkien[i].dinhgia()))
def demhong(listlinhkien, n):
    dem = 0
    lkhong = []
    for lk in listlinhkien:
        if lk.trangthai == 'Hong':
            dem += 1
            lkhong.append(lk)
    if dem == 0:
        print('Khong co linh kien hong')
    else:
        return dem, lkhong
def linhkienmoi(listlinhkien, n):
    lkmoi = []
    demm = 0
    for lk in listlinhkien:
        if lk.trangthai == 'Moi':
            lkmoi.append(lk.ten)
            demm += 1
    tuplelkmoi = tuple(lkmoi)
    if demm == 0:
        print('Khong co linh kien nao moi')
    else:
        print('Linh kien moi: ', tuplelkmoi)
def main():
    print('Nhap so linh kien: ')
    n = nhapsonguyen()
    listlinhkien = nhaplist(n)
    hienthi(listlinhkien, n)
    dem, lkhong = demhong(listlinhkien, n)
    print('So linh kien hong: ', dem)
    print('Danh sach linh kien hong: ')
    hienthi(lkhong, dem)
    print('Tuple linh kien moi:')
    linhkienmoi(listlinhkien, n)


if __name__ == '__main__':
    main()