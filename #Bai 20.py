#Bai 20
import math
class Songuyen():
    def __init__(self,a):
        self.a = a
    def ktramduong(self):
        if self.a > 0:
            return True
        else:
            return False
    def ktrahoanthien(self):
        tonguocso = 0
        for i in range(1,self.a):
            if self.a % i == 0:
                tonguocso += i
        return tonguocso == self.a
    def ktrachinhphuong(self):
        return math.sqrt(self.a) == int(math.sqrt(self.a))
def nhapsonguyen(n):
    songuyen = []
    for i in range (n):
        print(f'Nhap so nguyen thu {i+1}: ')
        a = int(input())
        songuyeni = Songuyen(a)
        songuyen.append(songuyeni)
    return songuyen
def insohoanthien(songuyen, n):
    sohoanthien = []
    demh = 0
    for so in songuyen:
        if so.ktrahoanthien():
            sohoanthien.append(so.a)
            demh += 1
    if demh == 0:
        print('Khong co so hoan thien nao trong danh sach.')
    else:
        print('Cac so hoan thien trong day la: ', sohoanthien)
def tichchinhphuong(songuyen, n):
    t = 1
    demc = 0
    for so in songuyen:
        if so.ktrachinhphuong():
            t *= so.a
            demc += 1
    if demc == 0:
        print('Khong co so chinh phuong nao trong danh sach.')
    else:
        print(f'Tich cac so chinh phuong la: {t}')
def main():
    print('Nhap so luong so nguyen: ')
    n = int(input())
    songuyen = nhapsonguyen(n)
    insohoanthien(songuyen, n)
    tichchinhphuong(songuyen, n)
if __name__ == "__main__":
    main()
    