#Bai 12
import math
class Songuyen:
    def __init__(self, a):
        self.a = a

    def ktrale(self):
        return self.a % 2 != 0

    def ktranguyento(self):
        if self.a < 2:
            return False
        for i in range(2, int(self.a**0.5) + 1):
            if self.a % i == 0:
                return False
        return True

    def ktrachinhphuong(self):
        return self.a ** 0.5 == int(self.a ** 0.5)

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

def hienthi(list_songuyen):
    print('Day so nguyen vua nhap la: ', [so.a for so in list_songuyen])

def daysole(list_songuyen):
    so_le = [so.a for so in list_songuyen if so.ktrale()]
    if so_le:
        print('Day so le la: ', so_le)
    else:
        print('Day khong co so le nao')

def tichchinhphuong(list_songuyen):
    t = 1
    for so in list_songuyen:
        if so.ktrachinhphuong():
            t *= so.a
    print(f'Tich cac so chinh phuong la: {t}')

def maxnguyento(list_songuyen):
    nguyento_max = None
    for so in list_songuyen:
        if so.ktranguyento():
            if nguyento_max is None or so.a > nguyento_max:
                nguyento_max = so.a
    if nguyento_max is not None:
        print(f'So nguyen to lon nhat la: {nguyento_max}')
    else:
        print('Khong co so nguyen to nao trong danh sach.')

def main():
    print('Nhap so luong so nguyen: ')
    n = nhapsoluongsonguyen()
    list_songuyen = nhaplistsonguyen(n)
    hienthi(list_songuyen)
    daysole(list_songuyen)
    tichchinhphuong(list_songuyen)
    maxnguyento(list_songuyen)

if __name__ == '__main__':
    main()
