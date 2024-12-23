#Bai 56
import math
class Phong:
    def __init__(self,cd, cr, h):
        self.cd = cd
        self.cr = cr
        self.h = h
    def csdh(self):
        return self.cd*self.cr*self.h*200
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n>0:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n>0:
                break
        except ValueError:
            print("Nhap lai")
    return n

def nhaplist(n):
    listphong = []
    for i in range(n):
        print('Nhap thong tin phong thu',i+1)
        print('Nhap chieu dai: ')
        cd = nhapsothuc()
        print('Nhap chieu rong: ')
        cr = nhapsothuc()
        print('Nhap chieu cao: ')
        h = nhapsothuc()
        phong = Phong(cd,cr,h)
        listphong.append(phong)
    return listphong

def hienthi(listphong, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Chieu dai', 'Chieu rong', 'Chieu cao','CSDH'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listphong[i].cd, listphong[i].cr, listphong[i].h, listphong[i].csdh(), listphong[i].csdh()))

def taodict(listphong, n):
    dictphong = {}
    for i in range(n):
        v = listphong[i].cd*listphong[i].cr*listphong[i].h
        dictphong[v] = listphong[i].csdh()
    return dictphong
def demds(listphong, n):
    dem = 0
    for i in range(n):
        if listphong[i].csdh() > 9000:
            dem += 1
    print(f'So phong co CSDH > 9000 la: {dem}')

def main():
    print('Nhap so phong: ')
    n = nhapsonguyen()
    listphong = nhaplist(n)
    hienthi(listphong, n)
    dictphong = taodict(listphong, n)
    print(f'Dictionary phong: {dictphong}')
    demds(listphong, n)

if __name__ == '__main__':
    main()
