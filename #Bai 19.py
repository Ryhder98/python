#Bai 19
import math
class Hinhtron():
    def __init__(self,a):
        self.a = a
    def chuvi(self):
        return round(2*math.pi*self.a, 3)
    def dientich(self):
        return round(math.pi*self.a**2, 3)
def nhapsonguyen():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            if n > 0:
                break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhapsothuc():
    while True:
        n = input('Nhap gia tri: ')
        try:
            n = float(n)
            break
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
    return n
def nhaplisttron(n):
    list_tron = []
    for i in range(n):
        print(f'Nhap ban kinh thu {i+1}: ')
        a = nhapsothuc()
        hinhtron = Hinhtron(a)
        list_tron.append(hinhtron)
    return list_tron
def hienthi(list_tron, n):
    print('{:<15}{:<15}{:<15}'.format('Ban kinh','Chu vi','Dien tich'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}'.format(list_tron[i].a, list_tron[i].chuvi(), list_tron[i].dientich()))
def tongdientich(list_tron, n):
    t = 0
    for i in range(n):
        t += list_tron[i].dientich()
    print(f'Tong dien tich la: {t}')
def mintron(list_tron, n):
    min = list_tron[0].a
    for i in range(1,n):
        if list_tron[i].a < min:
            min = list_tron[i].a
    for i in range (n):
        if list_tron[i].a == min:
            print(f'Hinh tron thu {i+1} co ban kinh nho nhat la: {list_tron[i].a}')
def main():
    print('Nhap so luong hinh tron: ')
    n = nhapsonguyen()
    list_tron = nhaplisttron(n)
    hienthi(list_tron, n)
    tongdientich(list_tron, n)
    mintron(list_tron, n)
if __name__ == '__main__':
    main()
    