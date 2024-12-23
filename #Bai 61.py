#Bai 61
import math
class Tauca:
    def __init__(self,ten,tieuthu,dg,tienca,k):
        self.ten = ten
        self.tieuthu = tieuthu
        self.dg = dg
        self.tienca = tienca
        self.k = k
    def lai(self):
        chiphi = self.tieuthu * self.dg
        if self.tienca/chiphi >= 5:
            return 'Co lai'
        else:
            return 'Khong lai'
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
            if n>0:
                break
        except ValueError:
            print("Nhap lai")
    return n

def nhapten():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isalpha() == True and n.istitle() == True:
                break
        except ValueError:
            print("Nhap lai")
    return n

def nhaplist(n):
    listtauca = []
    k = 5
    for i in range(n):
        print('Nhap thong tin tau ca thu ',i+1)
        print('Nhap ten: ')
        ten = nhapten()
        print('Nhap so lit dau tieu thu: ')
        tieuthu = nhapsothuc()
        print('Nhap don gia: ')
        dg = nhapsothuc()
        print('Nhap tien ca: ')
        tienca = nhapsothuc()
        tau = Tauca(ten,tieuthu,dg,tienca,k)
        listtauca.append(tau)
    return listtauca

def hienthi(listtauca, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten', 'Tieu thu', 'Don gia', 'Tien ca','Ty le k', 'Kha nang lai'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listtauca[i].ten, listtauca[i].tieuthu, listtauca[i].dg, listtauca[i].tienca, listtauca[i].k, listtauca[i].lai()))

def taotuple(listtauca, n):
    dslai = []
    for tau in listtauca:
        if tau.lai() == 'Co lai':
            dslai.append(tau.ten)
    return tuple(dslai)
def sapxepds(listtauca, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listtauca[j].tienca < listtauca[j+1].tienca:
                listtauca[i], listtauca[j] = listtauca[j], listtauca[i]
    print('Danh sach sau khi sap xep: ')
    hienthi(listtauca, n)
def main():
    print('Nhap vao so tau ca trong ds n: ')
    n = nhapsonguyen()
    listtauca = nhaplist(n)
    hienthi(listtauca, n)
    dscolai = taotuple(listtauca, n)
    print('Tuple tau co lai: ', dscolai)
    sapxepds(listtauca, n)

if __name__ == "__main__":
    main()