#Bai 41
import math
class Mon:
    def __init__(self,ten,sotin,heso,dongia):
        self.ten=ten
        self.sotin=sotin
        self.heso=heso
        self.dongia=dongia
    def hocphi(self):
        return self.sotin*self.heso*self.dongia
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
    listmon = []
    print('Nhap don gia: ')
    dongia = nhapsothuc()
    for i in range(n):
        print('Nhap ten mon: ')
        ten = nhapten()
        print('Nhap so tin: ')
        sotin = nhapsonguyen()
        print('Nhap he so: ')
        heso = nhapsothuc()
        mon = Mon(ten, sotin, heso, dongia)
        listmon.append(mon)
    return listmon

def hienthi(listmon, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'So tin', 'He so', 'Don gia', 'Hoc phi'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listmon[i].ten, listmon[i].sotin, listmon[i].heso, listmon[i].dongia, listmon[i].hocphi()))
def tonghocphi(listmon, n):
    t = 0
    for i in range(n):
        t += listmon[i].hocphi()
    return t
def taodict(listmon, n):
    dictmon = {}
    for i in range(n):
        dictmon[listmon[i].ten] = listmon[i].hocphi()
    return dictmon
def main():
    print('Nhap so mon: ')
    n = nhapsonguyen()
    listmon = nhaplist(n)
    hienthi(listmon, n)
    print('Tong hoc phi: ', tonghocphi(listmon, n))
    dictmon = taodict(listmon, n)
    print('Danh sach mon: ', dictmon)

if __name__ == '__main__':
    main()