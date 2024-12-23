#Bai 60
import math
class Hoaqua:
    def __init__(self,loai,gia,soluong,chatluong):
        self.loai = loai
        self.gia = gia
        self.soluong = soluong
        self.chatluong = chatluong
    def sotien(self):
        if self.chatluong == 1:
            return round(self.gia*self.soluong,3)
        elif self.chatluong == 2:
            return round(self.gia*self.soluong*0.8,3)
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
def nhapchatluong():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n == 1 or n == 2:
                break
        except ValueError:
            print("Nhap lai")
    return n

def nhaplist(n):
    listhq = []
    for i in range(n):
        print('Nhap thong tin hoa qua thu ',i+1)
        print('Nhap loai: ')
        loai = nhaploai()
        print('Nhap gia: ')
        gia = nhapsothuc()
        print('Nhap so luong: ')
        soluong = nhapsonguyen()
        print('Nhap chat luong: ')
        chatluong = nhapchatluong()
        hq = Hoaqua(loai,gia,soluong,chatluong)
        listhq.append(hq)
    return listhq

def hienthi(listhq, n):
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Loai', 'Gia', 'So luong', 'Chat luong','Tien'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(listhq[i].loai, listhq[i].gia, listhq[i].soluong, listhq[i].chatluong, listhq[i].sotien()))
def taodict(listhq, n):
    dicthq = {}
    for i in range(n):
        dicthq[listhq[i].loai] = listhq[i].sotien()
    return dicthq
def sapxepds(listhq, n):
    for i in range(n-1):
        for j in range(i+1,n):
            if listhq[i].soluong < listhq[j].soluong:
                listhq[i], listhq[j] = listhq[j], listhq[i]
    print('Danh sach sau khi sap xep: ')
    hienthi(listhq, n)
def main():
    print('Nhap vao so hoa qua trong ds n: ')
    n = nhapsonguyen()
    listhq = nhaplist(n)
    hienthi(listhq, n)
    dicthq = taodict(listhq, n)
    print('Dict hoa qua: ')
    print(dicthq)
    sapxepds(listhq, n)

if __name__ == '__main__':
    main()