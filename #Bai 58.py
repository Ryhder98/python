#Bai 58
import math
class Beca:
    def __init__(self,loai,x,y,von):
        self.loai = loai
        self.x = x
        self.y = y
        self.von = von
    def tiencong(self):
        return self.x*self.y - self.von
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n>0:
                break
        except ValueError:
            print("Nhap lai")
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
def nhaploai():
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
    listbeca = []
    for i in range(n):
        print('Nhap thong tin be ca thu ',i+1)
        print('Nhap loai: ')
        loai = nhaploai()
        print('Nhap don gia: ')
        x = nhapsothuc()
        print('Nhap san luong thu duoc: ')
        y = nhapsothuc()
        print('Nhap von: ')
        von = nhapsothuc()
        beca = Beca(loai,x,y,von)
        listbeca.append(beca)
    return listbeca

def hienthi(listbeca, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Loai', 'Don gia', 'San luong', 'Von', 'Tien cong'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listbeca[i].loai, listbeca[i].x, listbeca[i].y, listbeca[i].von, listbeca[i].tiencong()))
def taodict(listbeca, n):
    dictbeca = {}
    for i in range(n):
        dictbeca[listbeca[i].loai] = listbeca[i].tiencong()
    return dictbeca
def tongtien(listbeca, n):
    t = 0
    for i in range(n):
        t += listbeca[i].tiencong()
    return t

def main():
    print('Nhap so be ca: ')
    n = nhapsonguyen()
    listbeca = nhaplist(n)
    hienthi(listbeca, n)
    dictbeca = taodict(listbeca, n)
    print(f'Dictionary be ca: {dictbeca}')
    print(f'Tong tien cong: {tongtien(listbeca, n)}')
    
if __name__ == '__main__':
    main()