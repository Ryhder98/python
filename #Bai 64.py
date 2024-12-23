#Bai 64
import math
class DeMUX:
    def __init__(self, ten, sobitdauvao, sobitdaura):
        self.ten = ten
        self.sobitdauvao = sobitdauvao
        self.sobitdaura = sobitdaura
    def soduongdk(self):
        return math.log2(self.sobitdaura/self.sobitdauvao)
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapsobitdauvao():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n == 1 :
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapsobitdaura():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if math.log2(n) == int(math.log2(n)):
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
    listDeMUX = []
    for i in range(n):
        print('Nhap ten mach DeMUX:')
        ten = nhapten()
        print('Nhap so bit dau vao:')
        sobitdauvao = nhapsobitdauvao()
        print('Nhap so bit dau ra:')
        sobitdaura = nhapsobitdaura()
        mux = DeMUX(ten, sobitdauvao, sobitdaura)
        listDeMUX.append(mux)
    return listDeMUX

def hienthi(listDeMUX, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten DeMUX', 'So bit dau vao', 'So bit dau ra', 'So duong dk'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listDeMUX[i].ten, listDeMUX[i].sobitdauvao, listDeMUX[i].sobitdaura, listDeMUX[i].soduongdk()))
    
def sapxepds(listDeMUX, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listDeMUX[j].sobitdaura < listDeMUX[j+1].sobitdaura:
                listDeMUX[j], listDeMUX[j+1] = listDeMUX[j+1], listDeMUX[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listDeMUX, n)

def maxdgdk(listDeMUX, n):
    dsmaxdgdk = []
    dgdkmax = listDeMUX[0].soduongdk()
    for i in range(1, n):
        if listDeMUX[i].soduongdk() > dgdkmax:
            dgdkmax = listDeMUX[i].soduongdk()
    for i in range(n):
        if listDeMUX[i].soduongdk() == dgdkmax:
            dsmaxdgdk.append(listDeMUX[i].ten)
    tupledgdk = tuple(dsmaxdgdk)
    print(f'Tuple mach DeMUX co duong dk lon nhat la: {tupledgdk} voi {dgdkmax} duong dieu khien')
def main():
    print('Nhap so mach demux: ')
    n = nhapsonguyen()
    listDeMUX = nhaplist(n)
    hienthi(listDeMUX, n)
    sapxepds(listDeMUX, n)
    maxdgdk(listDeMUX, n)
if __name__ == '__main__':
    main()
    