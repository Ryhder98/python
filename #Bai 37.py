#Bai 37
import math
class Maybom:
    def __init__(self, loai, cs, tg):
        self.loai = loai
        self.cs = cs
        self.tg = tg
    def nltieuthu(self):
        return self.cs * self.tg
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
            if n > 0:
                break
        except ValueError:
            print('Nhap lai')
    return n
def nhaploai():
    while True:
        loai = input('Nhap: ')
        try:
            loai = str(loai)
            if loai.isalpha() == True and loai.istitle() == True:
                break
        except ValueError:
            print('Nhap lai')
    return loai

def nhaplist(n):
    listmaybom = []
    for i in range(n):
        print('Nhap loai may bom: ')
        loai = nhaploai()
        print('Nhap cong suat may bom: ')
        cs = nhapsothuc()
        print('Nhap thoi gian: ')
        tg = nhapsothuc()
        maybom = Maybom(loai, cs, tg)
        listmaybom.append(maybom)
    return listmaybom
def hienthi(listmaybom, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Loai', 'Cong suat', 'Thoi gian', 'Tieu thu'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listmaybom[i].loai, listmaybom[i].cs, listmaybom[i].tg, listmaybom[i].nltieuthu()))
def sapxepds(listmaybom, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listmaybom[j].nltieuthu() < listmaybom[j+1].nltieuthu():
                listmaybom[j], listmaybom[j+1] = listmaybom[j+1], listmaybom[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listmaybom, n)

def tongnl(listmaybom, n):
    t = 0
    for i in range(n):
        t += listmaybom[i].nltieuthu()
    print('Tong nang luong tieu thu: ', t)

def main():
    print('Nhap so may bom: ')
    n = nhapsonguyen()
    listmaybom = nhaplist(n)
    hienthi(listmaybom, n)
    sapxepds(listmaybom, n)
    tongnl(listmaybom, n)

if __name__ == '__main__':
    main()