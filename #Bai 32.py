#Bai 32
import math
class Robocon:
    def __init__ (self, tendoi, sodiem, tg, diemtd):
        self.tendoi = tendoi
        self.sodiem = sodiem
        self.tg = tg
        self.diemtd = diemtd
    def dtb(self):
        return (self.sodiem / self.tg)*10
def nhapten():
    while True:
        ten = input('Nhap: ')
        try:
            ten = str(ten)
            if ten.isalnum() == True:
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
def nhapsodiem():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaptgian():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n > 0 and n <= 180:
                break
        except ValueError:
            print('Nhap lai')
    return n

def nhaplist(n):
    list_robocon = []
    print('Nhap diem tuyet doi: ')
    diemtd = nhapsodiem()
    for i in range(n):
        print(f'Nhap thong tin con robocon thu {i+1}: ')
        print('Nhap ten doi: ')
        tendoi = nhapten()
        print('Nhap so diem: ')
        sodiem = nhapsodiem()
        while sodiem > diemtd:
            print('Nhap lai')
            sodiem = nhapsodiem()
        print('Nhap thoi gian: ')
        tg = nhaptgian()
        robocon = Robocon(tendoi, sodiem, tg, diemtd)
        list_robocon.append(robocon)
    return list_robocon
def hienthi(list_robocon, n):
    print('{:<15}{:<15}{:<15}{:<20}{:<15}'.format('Ten doi','So diem','Thoi gian','Diem tuyet doi','Diem trung binh'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<20}{:<15}'.format(list_robocon[i].tendoi,list_robocon[i].sodiem,list_robocon[i].tg,list_robocon[i].diemtd,list_robocon[i].dtb()))
def demdiem(list_robocon, n):
    dem = 0
    listdoi = []
    for i in range(n):
        if list_robocon[i].sodiem == list_robocon[i].diemtd:
            dem += 1
            listdoi.append(list_robocon[i].tendoi)
    print(f'Co {dem} con robocon co so diem bang diem tuyet doi la {listdoi}')
def sapxepds(list_robocon, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if list_robocon[i].dtb() < list_robocon[j].dtb():
                list_robocon[i], list_robocon[j] = list_robocon[j], list_robocon[i]
    
def main():
    print('Nhap so doi: ')
    n = nhapsonguyen()
    list_robocon = nhaplist(n)
    hienthi(list_robocon, n)
    demdiem(list_robocon, n)
    sapxepds(list_robocon, n)
    hienthi(list_robocon, n)
if __name__ == '__main__':
    main()