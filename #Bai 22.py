#Bai 22
import math
class Songuyen:
    def __init__(self,a):
        self.a = a
    def ktrachanle(self):
        if self.a % 2 == 0:
            return True
        else:
            return False
    def chinhphuong(self):
        return self.a ** 2
    def sodao(self):
        return int(str(self.a)[::-1])
def nhapgtrisonguyen():
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
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhaplist(n):
    list_songuyen = []
    for i in range(n):
        print(f'Nhap so thu {i+1}: ')
        a = nhapgtrisonguyen()
        songuyen = Songuyen(a)
        list_songuyen.append(songuyen)
    return list_songuyen
def insodao(list_songuyen, n):
    lsodao = []
    for so in list_songuyen:
        if so.sodao():
            lsodao.append(so.sodao())
    print(f'Cac so dao nguoc la: {lsodao}')
def tongle(list_songuyen, n):
    t = 0
    dem = 0
    for so in list_songuyen:
        if so.ktrachanle() == False:
            t += so.a
            dem += 1
    if dem == 0:
        print('Khong co so le nao.')
    else:
        print(f'Tong cac so le la: {t}')
def maxcp(list_songuyen, n):
    maxcp = 0
    for so in list_songuyen:
        if so.chinhphuong() > maxcp:
            maxcp = so.chinhphuong()
    print(f'So chinh phuong lon nhat la: {maxcp}')
def main():
    print('Nhap so luong so nguyen: ')
    n = nhapsoluongsonguyen()
    list_songuyen = nhaplist(n)
    insodao(list_songuyen, n)
    tongle(list_songuyen, n)
    maxcp(list_songuyen, n)
if __name__ == '__main__':
    main()