#Bai 15
import math
class Songuyen:
    def __init__(self, a):
        self.a = a
    def ktraam(self):
        return self.a < 0
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
def hienthisohoanthien(list_songuyen, n):
    so_hoanthien = [so.a for so in list_songuyen if so.ktrahoanthien()]
    if so_hoanthien:
        print('Day so hoan thien la: ', so_hoanthien)
    else:
        print('Day khong co so hoan thien nao')
def tichsodoixung(list_songuyen, n):
    t = 1
    for i in range (n):
        if list_songuyen[i].ktradoixung():
            t *= list_songuyen[i].a
    print(f'Tong cac so doi xung la: {t}')
def minsoam(list_songuyen, n):
    soammin = None
    for so in list_songuyen:
        if so.ktraam():
            if soammin is None or so.a < soammin:
                soammin = so.a
    if soammin is not None:
        print(f'So am nho nhat la: {soammin}')
    else:
        print('Khong co so am nao trong danh sach.')
def main():
    print('Nhap so luong so nguyen: ')
    n = nhapsoluongsonguyen()
    list_songuyen = nhaplistsonguyen(n)
    hienthi(list_songuyen, n)
    hienthisohoanthien(list_songuyen, n)
    tichsodoixung(list_songuyen, n)
    minsoam(list_songuyen, n)
if __name__ == "__main__":
    main()