#Bai 36
import math
class Dtro:
    def __init__(self, v1, v2 ,v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def giatri(self):
        v1 = {'Den': 0, 'Nau': 1, 'Do': 2, 'Cam': 3, 'Vang': 4, 'Luc': 5, 'Lam': 6, 'Tim': 7, 'Xam': 8, 'Trang': 9}
        v2 = {'Den': 0, 'Nau': 1, 'Do': 2, 'Cam': 3, 'Vang': 4, 'Luc': 5, 'Lam': 6, 'Tim': 7, 'Xam': 8, 'Trang': 9}
        v3 = {'Den': 1, 'Nau': 10, 'Do': 10**2, 'Cam': 10**3, 'Vang': 10**4, 'Luc': 10**5, 'Lam': 10**6, 'Tim': 10**7, 'Xam': 10**8, 'Trang': 10**9}
        if self.v1 not in v1 or self.v2 not in v2 or self.v3 not in v3:
            raise ValueError("Mau khong hop le")
        gia_tri = (v1[self.v1] * 10 + v2[self.v2]) * v3[self.v3]
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
def nhapmau():
    while True:
        mau = input('Nhap mau: ')
        if mau not in ['Den', 'Nau', 'Do', 'Cam', 'Vang', 'Luc', 'Lam', 'Tim', 'Xam', 'Trang']:
            print('Mau khong hop le. Vui long nhap lai.')
        else:
            break
    return mau
def nhaplist(n):
    listdtro = []
    for i in range(n):
        print('Nhap vong mau thu 1: ')
        v1 = nhapmau()
        print('Nhap vong mau thu 2: ')
        v2 = nhapmau()
        print('Nhap vong mau thu 3: ')
        v3 = nhapmau()
        dtro = Dtro(v1, v2, v3)
        listdtro.append(dtro)
    return listdtro
def hienthi(listdtro, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Vong mau 1', 'Vong mau 2', 'Vong mau 3', 'Gia tri'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listdtro[i].v1, listdtro[i].v2, listdtro[i].v3, listdtro[i].giatri()))
def sxepds(listdtro, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if listdtro[i].giatri() > listdtro[j].giatri():
                listdtro[i], listdtro[j] = listdtro[j], listdtro[i]
    print('Danh sach sau khi sap xep: ')
    hienthi(listdtro, n)
def demgtri(listdtro, n):
    dem = 0
    for i in range(n):
        if listdtro[i].giatri() < 1000:
            dem += 1
    return dem
def main():
    print('Nhap so dien tro: ')
    n = nhapsonguyen()
    listdtro = nhaplist(n)
    hienthi(listdtro, n)
    listdtro = sxepds(listdtro, n)
    hienthi(listdtro, n)
    print('So dien tro co gia tri < 1000: ', demgtri(listdtro, n))
if __name__ == '__main__':
    main()