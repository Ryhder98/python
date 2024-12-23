#Bai 14
import math
class Songuyen:
    def __init__(self, a):
        self.a = a
    def ktraduong(self):
        return self.a > 0
    def ktradoixung(self):
        return str(self.a) == str(self.a)[::-1]
    def ktrahoanthien(self):
        tonguocso = 0
        for i in range(1, self.a):
            if self.a % i == 0:
                tonguocso += i
        return tonguocso == self.a
def nhapgiatrisonguyen():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhapsoluongsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhaplistsonguyen(n):
    list_songuyen = []
    for i in range(n):
        print(f'Nhap so nguyen thu {i+1}: ')
        a = nhapgiatrisonguyen()
        songuyeni = Songuyen(a)
        list_songuyen.append(songuyeni)
    return list_songuyen
def hienthi(list_songuyen, n):
    print('Day so nguyen vua nhap la: ', [so.a for so in list_songuyen])
def hienthisoduong(list_songuyen, n):
    so_duong = [so.a for so in list_songuyen if so.ktraduong()]
    if so_duong:
        print('Day so duong la: ', so_duong)
    else:
        print('Day khong co so duong nao')
def tongsohoanthien(list_songuyen, n):
    t = 0
    for i in range (n):
        if list_songuyen[i].ktrahoanthien():
            t += list_songuyen[i].a
    print(f'Tong cac so hoan thien la: {t}')
def maxdoixung(list_songuyen, n):
    doixungmax = None
    for so in list_songuyen:
        if so.ktradoixung():
            if doixungmax is None or so.a > doixungmax:
                doixungmax = so.a
    if doixungmax is not None:
        print(f'So doi xung lon nhat la: {doixungmax}')
    else:
        print('Khong co so doi xung nao trong danh sach.')
def main():
    print('Nhap so luong so nguyen: ')
    n = nhapsoluongsonguyen()
    list_songuyen = nhaplistsonguyen(n)
    hienthi(list_songuyen, n)
    hienthisoduong(list_songuyen, n)
    tongsohoanthien(list_songuyen, n)
    maxdoixung(list_songuyen, n)
if __name__ == "__main__":
    main()