#Bai 13
import math
class Songuyen:
    def __init__(self, a):
        self.a = a
    def ktraamduong(self):
        if self.a > 0:
            return True
        if self.a < 0:
            return False
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
def hienthisoam(list_songuyen, n):
    so_am = []
    dem = 0
    for i in range (n):
        if list_songuyen[i].ktraamduong() == False:
            so_am.append(list_songuyen[i].a)
            dem += 1
        if dem == 0:
            print('Khong co so am nao trong danh sach.') 
            break
    print('Day so am la: ',so_am)
def tongsodoixung(list_songuyen, n):
    t = 0
    for i in range (n):
        if list_songuyen[i].ktradoixung():
            t += list_songuyen[i].a
    print(f'Tong cac so doi xung la: {t}')
def minhoanthien(list_songuyen, n):
    hoanthienmin = None
    for i in range (n):
        if list_songuyen[i].ktrahoanthien():
            if hoanthienmin is None or list_songuyen[i].a < hoanthienmin:
                hoanthienmin = list_songuyen[i].a
    if hoanthienmin is not None:
        print(f'So hoan thien nho nhat la: {hoanthienmin}')
    else:
        print('Khong co so hoan thien nao trong danh sach.')
def main():
    print('Nhap so luong so nguyen: ')
    n = nhapsoluongsonguyen()
    list_songuyen = nhaplistsonguyen(n)
    hienthi(list_songuyen, n)
    hienthisoam(list_songuyen, n)
    tongsodoixung(list_songuyen, n)
    minhoanthien(list_songuyen, n)
if __name__ == "__main__":
    main()