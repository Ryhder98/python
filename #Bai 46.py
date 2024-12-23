#Bai 46
import math
class MUX:
    def __init__(self, ten, sobitdauvao, sobitdaura):
        self.ten = ten
        self.sobitdauvao = sobitdauvao
        self.sobitdaura = sobitdaura
    def soduongdk(self):
        return math.log2(self.sobitdauvao/self.sobitdaura)
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
def nhapsobitdaura():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n == 1 :
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapsobitdauvao():
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
    listMUX = []
    for i in range(n):
        print('Nhap ten mach MUX:')
        ten = nhapten()
        print('Nhap so bit dau vao:')
        sobitdauvao = nhapsobitdauvao()
        print('Nhap so bit dau ra:')
        sobitdaura = nhapsobitdaura()
        mux = MUX(ten, sobitdauvao, sobitdaura)
        listMUX.append(mux)
    return listMUX

def hienthi(listMUX, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ten MUX', 'So bit dau vao', 'So bit dau ra', 'So duong dk'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listMUX[i].ten, listMUX[i].sobitdauvao, listMUX[i].sobitdaura, listMUX[i].soduongdk()))
    
def sapxepds(listMUX, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if listMUX[j].sobitdauvao < listMUX[j+1].sobitdauvao:
                listMUX[j], listMUX[j+1] = listMUX[j+1], listMUX[j]
    print('Danh sach sau khi sap xep: ')
    hienthi(listMUX, n)

def maxdgdk(listMUX, n):
    dgdkmax = listMUX[0].soduongdk()
    for i in range(1, n):
        if listMUX[i].soduongdk() > dgdkmax:
            dgdkmax = listMUX[i].soduongdk()
    for i in range(n):
        if listMUX[i].soduongdk() == dgdkmax:
            print(f'Mach MUX co duong dk lon nhat la: {listMUX[i].ten} voi {dgdkmax}')
def main():
    print('Nhap so mach mux: ')
    n = nhapsonguyen()
    listMUX = nhaplist(n)
    hienthi(listMUX, n)
    sapxepds(listMUX, n)
    maxdgdk(listMUX, n)
if __name__ == '__main__':
    main()
    