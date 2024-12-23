#Bai 2
import math
class Hcn:
    def __init__(self,cd,cr):
        self.cd = cd
        self.cr = cr
    def tinhcvi(self):
        return (self.cd+self.cr)*2
    def tinhdt(self):
        return self.cd*self.cr
    def duongcheo(self):
        return math.sqrt(self.cd**2 + self.cr**2)
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
def nhaphcn(n):
    list_hcn = []
    for i in range(n):
        print(f'Nhap chieu dai cua hinh chu nhat thu {i+1}')
        cd = nhapsothuc()
        print(f'Nhap chieu rong cua hinh chu nhat thu {i+1}')
        cr = nhapsothuc()
        hcn = Hcn(cd,cr)
        list_hcn.append(hcn)
    return list_hcn
def hienthi(list_hcn, n):
    for i in range(n):
        print(f'Hinh chu nhat thu',(i+1),'co chieu dai va chieu rong la: ',(list_hcn[i].cd,list_hcn[i].cr),'va chu vi hinh chu nhat la: ',(list_hcn[i].tinhcvi()))
def tongdt(list_hcn, n):
        t = 0
        for i in range(n):
            t = t + list_hcn[i].tinhdt()
        print(f'tong dien tich cac hcn: ',t)
def duongcheomax(list_hcn, n):
        dgcheomax = list_hcn[0].duongcheo()
        for i in range (1,n):
            if list_hcn[i].duongcheo() > dgcheomax:
                dgcheomax = list_hcn[i].duongcheo()
        for i in range (n):
            if list_hcn[i].duongcheo() == dgcheomax:
                print(f'Hinh chu nhat thu ',(i+1),' co do dai duong cheo lon nhat la: ', list_hcn[i].duongcheo())

def main():
    print('Nhap so  hinh chu nhat: ')
    n = nhapsonguyen()
    list_hcn = nhaphcn(n)
    hienthi(list_hcn, n)
    tongdt(list_hcn, n)
    duongcheomax(list_hcn, n)
if __name__ == "__main__":
    main()