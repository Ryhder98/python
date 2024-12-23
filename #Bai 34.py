#Bai 34
import math
class Nv:
    def __init__ (self, ten, luongcb, sonam, hso):
        self.ten = ten
        self.luongcb = luongcb
        self.sonam = sonam
        self.hso = hso
    def luong(self):
        return (self.luongcb*self.hso) + self.sonam*(self.luongcb/10)
def nhapten():
    while True:
        ten = input('Nhap ten: ')
        try:
            ten = str(ten)
            if ten.istitle() == True and ten.isalpha() == True:
                break
        except ValueError:
            print('Nhap lai')
    return ten
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
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n

def nhaplist(n):
    list_nv = []
    for i in range(n):
        print(f'Nhap thong tin nhan vien thu {i+1}: ')
        print('Nhap ten: ')
        ten = nhapten()
        print('Nhap luong co ban: ')
        luongcb = nhapsothuc()
        print('Nhap so nam: ')
        sonam = nhapsonguyen()
        print('Nhap he so: ')
        hso = nhapsothuc()
        nv = Nv(ten, luongcb, sonam, hso)
        list_nv.append(nv)
    return list_nv
def hienthi(list_nv, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten','Luong cb', 'So nam', 'He so', 'Luong'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(list_nv[i].ten, list_nv[i].luongcb, list_nv[i].sonam, list_nv[i].hso, list_nv[i].luong()))
def sapxepds(list_nv, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if list_nv[i].luong() < list_nv[j].luong():
                list_nv[i], list_nv[j] = list_nv[j], list_nv[i]
    print('Danh sach nhan vien sau khi sap xep la: ')
    hienthi(list_nv, n)
def nvvehuu(list_nv, n):
    vehuu = []
    n1 = 0
    for i in range(n):
        if list_nv[i].sonam >= 25:
            vehuu.append(list_nv[i])
            n1+=1
    return vehuu, n1
def main():
    print('Nhap so nhan vien: ')
    n = nhapsonguyen()
    list_nv = nhaplist(n)
    hienthi(list_nv, n)
    sapxepds(list_nv, n)
    vehuu, n1 = nvvehuu(list_nv, n)
    if len(vehuu) == 0:
        print('Khong co nhan vien ve huu')
    else:
        print('Danh sach nhan vien ve huu la: ')
        hienthi(vehuu, n1)
if __name__ == '__main__':
    main()
