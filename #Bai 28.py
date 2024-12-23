#Bai 28
import math
class Hs:
    def __init__ (self, ten, msv, dt, dly, dh):
        self.ten = ten
        self.msv = msv
        self.dt = dt
        self.dly = dly
        self.dh = dh
    def dtb(self):
        return (self.dt + self.dly + self.dh)/3
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
            if n > 0 and n < 10:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaplist(n):
    list_hs = []
    for i in range (n):
        print(f'Nhap ten hoc sinh thu {i+1}: ')
        ten = nhapten()
        print('Nhap ma so hoc sinh: ')
        msv = nhapsonguyen()
        print('Nhap diem toan: ')
        dt = nhapsothuc()
        print('Nhap diem ly: ')
        dly = nhapsothuc()
        print('Nhap diem hoa: ')
        dh = nhapsothuc()
        hs = Hs(ten, msv, dt, dly, dh)
        list_hs.append(hs)
    return list_hs
def hienthi(list_hs, n):
    print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten','MSV','Diem toan','Diem ly','Diem hoa','Diem trung binh'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(list_hs[i].ten,list_hs[i].msv,list_hs[i].dt,list_hs[i].dly,list_hs[i].dh,list_hs[i].dtb()))
def tachdanhsach(list_hs, n):
    dssv_tbtren5 = []
    dssv_tbduoi5 = []
    n1 = n2 = 0
    for i in range(n):
        if list_hs[i].dtb() >= 5:
            dssv_tbtren5.append(list_hs[i])
            n1 += 1
        else:
            dssv_tbduoi5.append(list_hs[i])
            n2 += 1
    return dssv_tbtren5, n1, dssv_tbduoi5, n2

def tbmon(list_hs, n):
    tbt = 0
    tbl = 0
    tbh = 0
    for i in range(n):
        tbt += list_hs[i].dt/n
        tbl += list_hs[i].dly/n
        tbh += list_hs[i].dh/n
    print(f'Diem trung binh mon toan: {tbt}')
    print(f'Diem trung binh mon ly: {tbl}')
    print(f'Diem trung binh mon hoa: {tbh}')


def main():
    print('Nhap so hoc sinh: ')
    n = nhapsonguyen()
    list_hs = nhaplist(n)
    hienthi(list_hs, n)
    dssv_tbtren5, n1, dssv_tbduoi5, n2 = tachdanhsach(list_hs, n)
    if len(dssv_tbduoi5) == 0:
        print('Khong co sinh vien co diem trung binh duoi 5')
    else:
        print('Danh sach sinh vien co diem trung binh duoi 5: ')
        hienthi(dssv_tbduoi5, n2)
    if len(dssv_tbtren5) == 0:
        print('Khong co sinh vien co diem trung binh tren 5')
    else:
        print('Danh sach sinh vien co diem trung binh tren 5: ')
        hienthi(dssv_tbtren5, n1)
    tbmon(list_hs, n)
if __name__ == '__main__':
    main()
    