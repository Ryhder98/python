#Bai 1:
import math
class Tugiac:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def tinhcvi(self):
        return self.a+self.b+self.c+self.d
    def canhmax(self):
        return max(self.a,self.b,self.c,self.d)
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
def nhaptugiac(n):
    list_tugiac = []
    for i in range(n):
        print(f'Nhap canh thu nhat cua hinh tu giac thu {i+1}')
        a = nhapsothuc()
        print(f'Nhap canh thu hai cua hinh tu giac thu {i+1}')
        b = nhapsothuc()
        print(f'Nhap canh thu ba cua hinh tu giac thu {i+1}')
        c = nhapsothuc()
        print(f'Nhap canh thu tu cua hinh tu giac thu {i+1}')
        d = nhapsothuc()           
        tg = Tugiac(a,b,c,d)
        list_tugiac.append(tg)
    return list_tugiac
def hienthi(list_tugiac, n):
    for i in range(n):
        print(f'Hinh tu giac thu',(i+1),'co 4 canh la: ',(list_tugiac[i].a,list_tugiac[i].b,list_tugiac[i].c,list_tugiac[i].d),'co chu vi la: ',list_tugiac[i].tinhcvi(),'va co canh max la: ',list_tugiac[i].canhmax())
def cvimin(list_tugiac, n):
    mincv = list_tugiac[0].tinhcvi()
    for i in range(1, n):
        if list_tugiac[i].tinhcvi() < mincv:
            mincv = list_tugiac[i].tinhcvi()
    for i in range(n):
        if list_tugiac[i].tinhcvi() == mincv:
            print(f'Hinh tu giac thu',(i+1),'co chu vi nho nhat la: ',(list_tugiac[i].tinhcvi()))
def main():
    print('Nhap so hinh tu giac: ')
    n = nhapsonguyen()
    list_tugiac = nhaptugiac(n)
    hienthi(list_tugiac, n)
    cvimin(list_tugiac,n)
if __name__ == "__main__":
    main()