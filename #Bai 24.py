#Bai 24
import math
class Giaithua:
    def __init__ (self, a ):
        self.a = a
    def tinhgiaithua(self):
        g = 1
        for i in range(1, self.a + 1):
            g *= i
        return g
    def tong(self):
        t = 0
        for i in range(1, self.a + 1):
            t += i
        return t
def nhapgiatriso():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n 
def nhapsoluong():
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
    list_giaithua = []
    for i in range(n):
        print(f'Nhap so thu {i+1}: ')
        a = nhapgiatriso()
        giaithua = Giaithua(a)
        list_giaithua.append(giaithua)
    return list_giaithua
def hienthi(list_giaithua, n):
    print('{:<15}{:<15}{:<15}'.format('So thuc','Tong','Giai thua'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}'.format(list_giaithua[i].a, list_giaithua[i].tong(), list_giaithua[i].tinhgiaithua()))
def dictgiaithua(list_giaithua, n):
    dict_giaithua = {}
    for so in list_giaithua:
        dict_giaithua[so.a] = so.tinhgiaithua()
    return dict_giaithua
def taotuple(list_giaithua, n):
    listg = []
    for so in list_giaithua:
        listg.append(so.tinhgiaithua())
    tuplegiaithua = tuple(listg)
    return tuplegiaithua
def main():
    print('Nhap so luong so thuc: ')
    n = nhapsoluong()
    list_giaithua = nhaplist(n)
    hienthi(list_giaithua, n)
    print('Dictionary giai thua: ')
    dict_giaithua = dictgiaithua(list_giaithua, n)
    print(dict_giaithua)
    print('Tuple giai thua: ')
    tupleg = taotuple(list_giaithua, n)
    print(tupleg)
if __name__ == '__main__':
    main()
