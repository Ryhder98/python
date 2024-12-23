#Bai 21
import math
class Luythua:
    def __init__(self,a):
        self.a = a
    def binhphuong(self):
        return self.a ** 2
    def lapphuong(self):
        return self.a ** 3
    def giaithua(self):
        g = 1
        for i in range(1, self.a + 1):
            g *= i
        return g
def nhapsonguyen():
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
    list_luythua = []
    for i in range(n):
        print(f'Nhap so thu {i+1}: ')
        a = nhapsonguyen()
        luythua = Luythua(a)
        list_luythua.append(luythua)
    return list_luythua
def hienthi(list_luythua, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('So thuc','Binh phuong','Lap phuong','Giai thua'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(list_luythua[i].a, list_luythua[i].binhphuong(), list_luythua[i].lapphuong(), list_luythua[i].giaithua()))
def dictluythua(list_luythua, n):
    dict_luythua = {}
    for i in range(n):
        dict_luythua[list_luythua[i].a] = list_luythua[i].binhphuong() 
    return dict_luythua
def tonglapphuong(list_luythua, n):
    t = 0
    for i in range(n):
        t += list_luythua[i].lapphuong()
    return t
def main():
    print('Nhap so luong so thuc: ')
    n = nhapsonguyen()
    list_luythua = nhaplist(n)
    hienthi(list_luythua, n)
    print('Dictionary luy thua: ')
    dict_luythua = dictluythua(list_luythua, n)
    print(dict_luythua)
    print(f'Tong cac so lap phuong la: {tonglapphuong(list_luythua, n)}')
if __name__ == "__main__":
    main()
