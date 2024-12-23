#Bai 3
import math
class Hv:
    def __init__(self, a):
        self.a = a
    def tinhcvi(self):
        return self.a*4
    def tinhdt(self):
        return self.a**2
    def duongcheo(self):
        return math.sqrt(self.a**2 + self.a**2)
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
def nhaphv(n):
    list_hv = []
    for i in range (n):
        print(f'Nhap canh cua hinh vuong thu {i+1}')
        a = nhapsothuc()
        hv = Hv(a)
        list_hv.append(hv)
    return list_hv
def hienthi(list_hv, n):
    for i in range (n):
        print(f'Hinh vuong thu ',(i+1),' co canh la: ',(list_hv[i].a), 'va co chu vi la ',(list_hv[i].tinhcvi()))
def tongdt(list_hv, n):
    t = 0
    for i in range (n):
        t = t + list_hv[i].tinhdt()
    print(f'Tong dien tich cac hinh vuong la: ', t)
def maxduongcheo(list_hv, n):
    dgcheomax = list_hv[0].duongcheo()
    for i in range (1, n):
        if list_hv[i].duongcheo() > dgcheomax:
            dgcheomax = list_hv[i].duongcheo()
    for i in range (n):
        if list_hv[i].duongcheo() == dgcheomax:
            print(f'Hinh vuong thu ',(i+1),' co do dai duong cheo lon nhat la: ', list_hv[i].duongcheo())
def main():
    print('Nhap so hinh vuong: ')
    n = nhapsonguyen()
    list_hv = nhaphv(n)
    hienthi(list_hv, n)
    tongdt(list_hv, n)
    maxduongcheo(list_hv, n)
if __name__ == "__main__":
    main()