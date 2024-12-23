#Bai 42
import math
class Thothucong:
    def __init__(self, ten, sothamdet, dongia):
        self.ten = ten
        self.sothamdet = sothamdet
        self.dongia = dongia
    def tiencong(self):
        return self.sothamdet * self.dongia
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n >0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n >0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhapten():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isalpha() == True and n.istitle() == True:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaplist(n):
    listthothucong = []
    for i in range(n):
        print('Nhap ten tho thu cong: ')
        ten = nhapten()
        print('Nhap so tham de: ')
        sothamdet = nhapsonguyen()
        print('Nhap don gia: ')
        dongia = nhapsothuc()
        thothucong = Thothucong(ten, sothamdet, dongia)
        listthothucong.append(thothucong)
    return listthothucong

def hienthi(listthothucong, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'So tham det', 'Don gia', 'Tien cong'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listthothucong[i].ten, listthothucong[i].sothamdet, listthothucong[i].dongia, listthothucong[i].tiencong()))
def demds(listthothucong, n):
    dem = 0
    dsthunhapcao = []
    thunhapmax = listthothucong[0].tiencong()
    for i in range(1, n):
        if listthothucong[i].tiencong() > thunhapmax:
            thunhapmax = listthothucong[i].tiencong()
    for i in range(n):
        if listthothucong[i].tiencong() == thunhapmax:
            dsthunhapcao.append(listthothucong[i])
            dem += 1
    return dem, dsthunhapcao
def taotuple(listthothucong, n):
    dstiencongthap = ()
    tiencongmin = listthothucong[0].dongia
    for i in range(1, n):
        if listthothucong[i].dongia < tiencongmin:
                tiencongmin = listthothucong[i].dongia
    for thothucong in listthothucong:
        if thothucong.dongia == tiencongmin:
            dstiencongthap+=(thothucong.ten, thothucong.dongia)
    print('Tuple tho thu cong co tien cong thap nhat: ', dstiencongthap)
def main():
    print('Nhap so tho thu cong: ')
    n = nhapsonguyen()
    listthothucong = nhaplist(n)
    hienthi(listthothucong, n)
    dem, dsthunhapcao = demds(listthothucong, n)
    print('So tho thu cong co tien cong cao nhat: ', dem)
    print('Danh sach tho thu cong co tien cong cao nhat: ')
    hienthi(dsthunhapcao, dem)
    taotuple(listthothucong, n)
if __name__ == '__main__':
    main()

