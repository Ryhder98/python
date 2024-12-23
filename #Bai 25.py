#Bai 25
import math
class Dientro:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def giatri(self):
        mau_vong1 = {'Den': 0, 'Nau': 1, 'Do': 2, 'Cam': 3, 'Vang': 4, 'Luc': 5, 'Lam': 6, 'Tim': 7, 'Xam': 8, 'Trang': 9}
        mau_vong2 = {'Den': 0, 'Nau': 1, 'Do': 2, 'Cam': 3, 'Vang': 4, 'Luc': 5, 'Lam': 6, 'Tim': 7, 'Xam': 8, 'Trang': 9}
        mau_vong3 = {'Den': 10**0, 'Nau': 10**1, 'Do': 10**2, 'Cam': 10**3, 'Vang': 10**4, 'Luc': 10**5, 'Lam': 10**6, 'Tim': 10**7, 'Xam': 10**8, 'Trang': 10**9}
        if self.v1 not in mau_vong1 or self.v2 not in mau_vong2 or self.v3 not in mau_vong2:
            raise ValueError("Mau khong hop le")
        gia_tri = (mau_vong1[self.v1] * 10 + mau_vong2[self.v2]) * mau_vong3[self.v3]
        return gia_tri
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
def nhaplist(n):
    listdtro = []
    for i in range(n):
        while True:
            try:
                v1 = input(f"Nhap mau vong 1 cho dien tro thu {i + 1}: ")
                v2 = input(f"Nhap mau vong 2 cho dien tro thu {i + 1}: ")
                v3 = input(f"Nhap mau vong 3 cho dien tro thu {i + 1}: ")
                dtro = Dientro(v1, v2, v3)
                listdtro.append(dtro)
                break
            except ValueError:
                print("Mau khong hop le. Vui long nhap lai.")
    return listdtro
def inlist(listdtro):
    print('Danh sach dien tro vua nhap: ')
    for i, dtro in enumerate(listdtro, start=1):
        print(f"Dien tro thu {i}: {dtro.v1}, {dtro.v2}, {dtro.v3}")
def taotuple(listdtro):
    return tuple(dtro.giatri() for dtro in listdtro)
def mindtro(listdtro):
    min_dtro = None
    min_gia_tri = float('inf')
    for dtro in listdtro:
        gia_tri = dtro.giatri()
        if gia_tri < min_gia_tri:
            min_gia_tri = gia_tri
            min_dtro = dtro
    return min_dtro
def main():
    print('Nhap so dien tro: ')
    n = nhapsonguyen()
    listdtro = nhaplist(n)
    inlist(listdtro)
    tuplegiatri = taotuple(listdtro)
    print('Tuple dien tro: ')
    print(tuplegiatri)
    dtro_min = mindtro(listdtro)
    print('Dien tro co tro khang nho nhat: ', dtro_min.giatri())
    print(f'vong mau 1: {dtro_min.v1}, vong mau 2: {dtro_min.v2}, vong mau 3: {dtro_min.v3}')
if __name__ == '__main__':
    main()




        