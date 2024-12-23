#Bai 16
import math
class Sothuc:
    def __init__(self, a):
        self.a = a
    def ktrasoamduong(self):
        if self.a > 0:
            return True
        if self.a < 0:
            return False
    def demchusosaudauphay(self):
        return len(str(self.a).split('.')[1])
def nhapsothuc():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = float(n)
            break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n

def nhaptuplesothuc(n):
    list_sothuc = []
    for i in range(n):
        print(f'Nhap so thuc thu {i+1}: ')
        a = nhapsothuc()
        sothuc = Sothuc(a)
        list_sothuc.append(sothuc)
    tuple_sothuc = tuple(list_sothuc)
    return tuple_sothuc

def hienthicacsoduong(list_sothuc, n):
    so_duong = []
    demd = 0
    for so in list_sothuc:
        if so.ktrasoamduong() == True:
            demd += 1
    if demd == 0:
        print('Day khong co so duong nao')
    if demd > 0:
        for so in list_sothuc:
            if so.ktrasoamduong() == True:
                so_duong.append(so.a)
        print('Day so duong la: ',so_duong)
def tichcacsoam(list_sothuc,n):
    t = 1
    dem = 0
    for so in list_sothuc:
        if so.ktrasoamduong() == False:
            dem += 1
            t *= so.a
    if dem == 0:
        print('Day khong co so am nao')
    else:
        print(f'Tich cac so am la: {t}')
def maxsosaudauphay(list_sothuc):
    sothucmax = list_sothuc[0]
    maxchusosothuc = sothucmax.demchusosaudauphay()
    listt = [sothucmax.a]
    for so in list_sothuc[1:]:
        sochuso = so.demchusosaudauphay()
        if sochuso > maxchusosothuc:
            sothucmax = so
            maxchusosothuc = sochuso
            listt = [sothucmax.a]
        if sochuso == maxchusosothuc:
            listt.append(so.a)
    print(f'Số có chữ số sau dấu phẩy max là: {listt} với số chữ số sau dấu phẩy là: {maxchusosothuc}')

def main():
    print('Nhap so luong so thuc: ')
    n = nhapsonguyen()
    list_sothuc = nhaptuplesothuc(n)
    hienthicacsoduong(list_sothuc, n)
    tichcacsoam(list_sothuc, n)
    maxsosaudauphay(list_sothuc)
if __name__ == '__main__':
    main()