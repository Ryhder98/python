#Bai 62
import math
class Sv:
    def __init__(self,ten,dtl,tinno):
        self.ten = ten
        self.dtl = dtl
        self.tinno = tinno
    def tinhtrang(self):
        if self.dtl <= 0.8 or self.tinno > 20:
            return 'Duoi hoc'
        elif 0.8 <= self.dtl <= 1.0 and self.tinno <= 20:
            return 'Canh bao'
        else:
            return 'Tiep tuc'
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n>=0 and n <= 4:
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
    listsv = []
    for i in range(n):
        print('Nhap thong tin sinh vien thu ',i+1)
        print('Nhap ten: ')
        ten = nhapten()
        print('Nhap diem tich luy: ')
        dtl = nhapsothuc()
        print('Nhap tin no: ')
        tinno = nhapsonguyen()
        sv = Sv(ten,dtl,tinno)
        listsv.append(sv)
    return listsv

def hienthi(listsv, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'Diem tich luy', 'Tin no','Tinh trang'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listsv[i].ten, listsv[i].dtl, listsv[i].tinno, listsv[i].tinhtrang()))

def taodict(listsv, n):
    dictsv = {}
    for i in range(n):
        if listsv[i].tinhtrang() == 'Duoi hoc' or listsv[i].tinhtrang() == 'Canh bao':
            dictsv[listsv[i].ten] = listsv[i].tinhtrang()
    return dictsv

def sapxepds(listsv, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listsv[j].dtl < listsv[j+1].dtl:
                listsv[i], listsv[j] = listsv[j], listsv[i]
    print('Danh sach sau khi sap xep: ')
    hienthi(listsv, n)
def main():
    print('Nhap vao so sinh vien trong ds n: ')
    n = nhapsonguyen()
    listsv = nhaplist(n)
    hienthi(listsv, n)
    dictsv = taodict(listsv, n)
    print('Dict sinh vien duoi hoc hoac canh bao: ', dictsv)
    sapxepds(listsv, n)

if __name__ == '__main__':
    main()