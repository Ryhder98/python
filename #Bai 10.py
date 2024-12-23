#Bai 10
class Thisinh:
    def __init__(self, ten, namsinh, toan, van, ngoaingu):
        self.ten = ten
        self.namsinh = namsinh
        self.toan = toan
        self.van = van
        self.ngoaingu = ngoaingu
    def tuoi(self):
        return 2024 - self.namsinh
    def tongdiem(self):
        return self.toan + self.van + self.ngoaingu
def nhapsonguyen():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            if n>0:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n>=0 and n<=10:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhapten():
    while True:
        n = input('Thong tin can nhap : ')
        try:
            n = str(n)
            if n.istitle()==True:
                break
        except ValueError:
            print('Nhap sai')
    return n
def nhapthisinh(n):
    list_thisinh = []
    for i in range(n):
        print(f'Nhap ten cua thi sinh : ')
        ten = nhapten()
        print(f'Nhap nam sinh cua thi sinh : ')
        namsinh = nhapsonguyen()
        print(f'Nhap diem toan cua thi sinh : ')
        toan = nhapsothuc()
        print(f'Nhap diem van cua thi sinh : ')
        van = nhapsothuc()
        print(f'Nhap diem ngoai ngu cua thi sinh : ')
        ngoaingu = nhapsothuc()
        thisinh = Thisinh(ten, namsinh, toan, van, ngoaingu)
        list_thisinh.append(thisinh)
    return list_thisinh

def hienthi(list_thisinh, n):
    print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<12}{:<12}'.format('Ho va ten','Nam sinh','Toan','Van','Ngoai ngu','Tuoi','Tong diem'))
    for i in range(n):
        print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<12}{:<12}'.format(list_thisinh[i].ten,list_thisinh[i].namsinh,list_thisinh[i].toan,list_thisinh[i].van,list_thisinh[i].ngoaingu,list_thisinh[i].tuoi(),list_thisinh[i].tongdiem()))
def mintuoi(list_thisinh, n):
    tuoimin = list_thisinh[0].tuoi()
    for i in range(1,n):
        if list_thisinh[i].tuoi() < tuoimin:
            tuoimin = list_thisinh[i].tuoi()
    for i in range(n):
        if list_thisinh[i].tuoi() == tuoimin:
            print(f'Thi sinh co tuoi nho nhat la: {list_thisinh[i].ten} voi tuoi la: {list_thisinh[i].tuoi()} ')
def maxtoan(list_thisinh, n):
    toanmax = list_thisinh[0].toan
    for i in range(1,n):
        if list_thisinh[i].toan > toanmax:
            toanmax = list_thisinh[i].toan
    for i in range(n):
        if list_thisinh[i].toan == toanmax:
            print(f'Thi sinh co diem toan lon nhat la: {list_thisinh[i].ten} voi diem toan la: {list_thisinh[i].toan} ')

def main():
    print('Nhap so thi sinh: ')
    n = nhapsonguyen()
    list_thisinh = nhapthisinh(n)
    hienthi(list_thisinh, n)
    mintuoi(list_thisinh, n)
    maxtoan(list_thisinh, n)
if __name__ == '__main__':
    main()