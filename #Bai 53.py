#Bai 53
import math
class Hinhtru:
    def __init__(self,ten,r,h):
        self.ten = ten
        self.r = r
        self.h = h
    def dtxq(self):
        return round(2*math.pi*self.r*(self.r+self.h), 3)
    def thetich(self):
        return round(math.pi*self.r*self.r*self.h, 3)
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
def nhapten():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.istitle() == True and n.isalpha() == True:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhaplist(n):
    listhtru = []
    for i in range(n):
        print('Nhap thong tin hinh tru thu',i+1)
        print('Nhap ten: ')
        ten = nhapten()
        print('Nhap ban kinh: ')
        r = nhapsothuc()
        print('Nhap chieu cao: ')
        h = nhapsothuc()
        htru = Hinhtru(ten,r,h)
        listhtru.append(htru)
    return listhtru
def hienthi(listhtru, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'Ban kinh', 'Chieu cao','DTXQ','The tich'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listhtru[i].ten, listhtru[i].r, listhtru[i].h, listhtru[i].dtxq(), listhtru[i].thetich()))

def maxminhtru(listhtru, n):
    maxhtru = listhtru[0].thetich()
    minhtru = listhtru[0].thetich()
    for i in range(1, n):
        if listhtru[i].thetich() > maxhtru:
            maxhtru = listhtru[i].thetich()
        if listhtru[i].thetich() < minhtru:
            minhtru = listhtru[i].thetich()
    for i in range(n):
        if listhtru[i].thetich() == maxhtru:
            print(f'Hinh tru co the tich lon nhat la: {listhtru[i].ten} voi the tich la: {maxhtru}')
        if listhtru[i].thetich() == minhtru:
            print(f'Hinh tru co the tich nho nhat la: {listhtru[i].ten} voi the tich la {minhtru}')

def tongdtxq(listhtru, n):
    tongdtxq = 0
    for i in range(n):
        tongdtxq += listhtru[i].dtxq()
    print(f'Tong dien tich xung quanh la: {tongdtxq}')
def main():
    print('Nhap so hinh tru: ')
    n = nhapsonguyen()
    listhtru = nhaplist(n)
    hienthi(listhtru, n)
    maxminhtru(listhtru, n)
    tongdtxq(listhtru, n)

if __name__ == '__main__':
    main()
