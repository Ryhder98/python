#Bai 63
import math
class Dt:
    def __init__(self,ten,hdh,dg,sl):
        self.ten = ten
        self.hdh = hdh
        self.dg = dg
        self.sl = sl
    def tien(self):
        return self.dg * self.sl
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
def nhapsoluong():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n >= 0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n>=0:
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
    listdt = []
    for i in range(n):
        print('Nhap thong tin dich vu thu ',i+1)
        print('Nhap ten: ')
        ten = nhapten()
        print('Nhap he dieu hanh: ')
        hdh = nhapten()
        print('Nhap don gia: ')
        dg = nhapsothuc()
        print('Nhap so luong: ')
        sl = nhapsoluong()
        dt = Dt(ten,hdh,dg,sl)
        listdt.append(dt)
    return listdt

def hienthi(listdt, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'He dieu hanh', 'Don gia', 'So luong', 'Tien'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listdt[i].ten, listdt[i].hdh, listdt[i].dg, listdt[i].sl, listdt[i].tien()))
def taotuple(listdt, n):
    dshdh = []
    for dt in listdt:
        if dt.hdh == 'Android':
            dshdh.append(dt.ten)
    return tuple(dshdh)
def demxoa(listdt, n):
    dem = 0
    i = 0
    for dt in listdt:
        if dt.sl == 0:
            dem += 1
    while i < len(listdt):
        if listdt[i].sl == 0:
            del listdt[i]
        else:
            i += 1
    n = len(listdt)
    print(f'Co {dem} dien thoai co so luong la 0')
    print('Danh sach sau khi xoa: ')
    hienthi(listdt, n)

def main():
    print('Nhap vao so dien thoai: ')
    n = nhapsonguyen()
    listdt = nhaplist(n)
    hienthi(listdt, n)
    dshdh = taotuple(listdt, n)
    print('Danh sach dien thoai Android: ', dshdh)
    demxoa(listdt, n)

if __name__ == "__main__":
    main()