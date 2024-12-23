#Bai 57
import math
class Loaptrung:
    def __init__(self,k,t,x,y):
        self.k = k
        self.t = t
        self.x = x
        self.y = y
    def sotien(self):
        trungno = self.k * (self.t/100) * self.x
        trunghong = self.k * (1-(self.t/100)) * self.y
        return trungno + trunghong
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
    listloaptrung = []
    for i in range(n):
        print('Nhap thong tin lo ap trung thu ',i+1)
        print('Nhap kha nang ap: ')
        k = nhapsothuc()
        print('Nhap hieu suat no: ')
        t = nhapsothuc()
        print('Nhap gia trung no: ')
        x = nhapsothuc()
        print('Nhap gia trung hong: ')
        y = nhapsothuc()
        loaptrung = Loaptrung(k,t,x,y)
        listloaptrung.append(loaptrung)
    return listloaptrung

def hienthi(listloaptrung, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Kha nang ap', 'Hieu suat no', 'Gia trung no', 'Gia trung hong', 'So tien'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listloaptrung[i].k, listloaptrung[i].t, listloaptrung[i].x, listloaptrung[i].y, listloaptrung[i].sotien()))

def taotuple(listloaptrung, n):
    listsotien = []
    for i in range(n):
        listsotien.append(listloaptrung[i].sotien())
    return tuple(listsotien)
def sapxepds(listloaptrung, n):
    for i in range(n-1):
        for j in range(i+1,n):
            if listloaptrung[j].sotien() < listloaptrung[j+1].sotien():
                listloaptrung[i], listloaptrung[j] = listloaptrung[j], listloaptrung[i]
    print('Danh sach sau khi sap xep: ')
    hienthi(listloaptrung, n)

def main():
    print('Nhap so lo ap trung: ')
    n = nhapsonguyen()
    listloaptrung = nhaplist(n)
    hienthi(listloaptrung, n)
    listsotien = taotuple(listloaptrung, n)
    print('Tuple so tien: ')
    print(listsotien)
    sapxepds(listloaptrung, n)

if __name__ == '__main__':
    main()


