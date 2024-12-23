#Bai 44
import math
class Kh:
    def __init__(self, ten, tiengui, lai, tg):
        self.ten = ten
        self.tiengui = tiengui
        self.lai = lai
        self.tg = tg
    def sotienrutduoc(self):
        return round(self.tiengui * (1 + self.lai * self.tg / 100), 2)
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n > 0:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapten():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isalpha() == True and n.istitle() == True:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhaplist(n):
    listkh = []
    for i in range(n):
        print('Nhap ten khach hang:')
        ten = nhapten()
        print('Nhap so tien gui:')
        tiengui = nhapsothuc()
        print('Nhap lai:')
        lai = nhapsothuc()
        print('Nhap thoi gian:')
        tg = nhapsothuc()
        kh = Kh(ten, tiengui, lai, tg)
        listkh.append(kh)
    return listkh

def hienthi(listkh, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten KH', 'Tien gui', 'Lai', 'Thoi gian', 'So tien rut duoc'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listkh[i].ten, listkh[i].tiengui, listkh[i].lai, listkh[i].tg, listkh[i].sotienrutduoc()))
def tongtiengoc(listkh, n):
    t = 0
    for i in range(n):
        t += listkh[i].tiengui
    print(f'Tong tien goc: {t}')
def taodict(listkh, n):
    dictkh = {}
    for i in range(n):
        dictkh[listkh[i].ten] = listkh[i].sotienrutduoc()
    return dictkh
def main():
    print('Nhap so luong khach hang:')
    n = nhapsonguyen()
    listkh = nhaplist(n)
    hienthi(listkh, n)
    tongtiengoc(listkh, n)
    dictkh = taodict(listkh, n)
    print('Dictionary KH: ',dictkh)

if __name__ == '__main__':
    main()