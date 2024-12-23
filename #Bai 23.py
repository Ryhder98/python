#Bai 23
import math
class Songuyen:
    def __init__(self, a):
        self.a = a
    def ktrachanle(self):
        if self.a % 2 == 0:
            return True
        if self.a % 2 != 0:
            return False
    def ktrachinhphuong(self):
        return math.sqrt(self.a) == int(math.sqrt(self.a))
    def sodao(self):
        return int(str(self.a)[::-1])
def nhapgiatriso():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhapsoluongso():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhaplist(n):
    list_songuyen = []
    for i in range(n):
        print(f'Nhap so thu {i+1}: ')
        a = nhapgiatriso()
        songuyen = Songuyen(a)
        list_songuyen.append(songuyen)
    return list_songuyen

def dictsodao(list_songuyen, n):
    dict_sodao = {}
    for so in list_songuyen:
        if so.sodao():
            dict_sodao[so.a] = so.sodao()
    return dict_sodao
def tongsodao(list_songuyen):
    t = 0
    for so in list_songuyen:
        if so.sodao():
            t += so.sodao()
    print(f'Tong cac so dao nguoc la: {t}')
def mincp(list_songuyen):
    demc = 0
    for so in list_songuyen:
        if so.ktrachinhphuong() == True:
            demc += 1
            cpmin = so.a
    if demc == 0:
        print('Khong co so chinh phuong nao.')
    if demc != 0:
        for so in list_songuyen:
            if so.ktrachinhphuong() == True:
                if so.a < cpmin:
                    cpmin = so.a
        print(f'So chinh phuong nho nhat la: {cpmin}')

def main():
    print('Nhap so luong so nguyen: ')
    n = nhapsoluongso()
    list_songuyen = nhaplist(n)
    dict_sodao = dictsodao(list_songuyen, n)
    print(dict_sodao)
    tongsodao(list_songuyen)
    mincp(list_songuyen)

if __name__ == '__main__':
    main()

