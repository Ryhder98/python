#Bai 33
import math
class Trau:
    def __init__ (self, ms, ns, tg):
        self.ms = ms
        self.ns = ns
        self.tg = tg
    def sometv(self):
        return self.ns * self.tg
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
def nhaplist(n):
    list_trau = []
    for i in range(n):
        print(f'Nhap thong tin con trau thu {i+1}: ')
        print('Nhap ma so: ')
        ms = nhapsonguyen()
        print('Nhap nang suat: ')
        ns = nhapsothuc()
        print('Nhap thoi gian: ')
        tg = nhapsothuc()
        trau = Trau(ms, ns, tg)
        list_trau.append(trau)
    return list_trau

def hienthi(list_trau, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('Ma so', 'Nang suat', 'Thoi gian', 'So met vuong'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(list_trau[i].ms, list_trau[i].ns, list_trau[i].tg, list_trau[i].sometv()))
def maxsk(list_trau, n):
    skmax = list_trau[0].tg
    for i in range(1, n):
        if list_trau[i].tg > skmax:
            skmax = list_trau[i].tg
    for i in range (n):
        if list_trau[i].tg == skmax:
            print(f'Con trau thu {i+1} co suc khoe deo dai nhat la: {list_trau[i].tg}')
def tongdt(list_trau, n):
    t = 0
    for i in range(n):
        t += list_trau[i].sometv()
    print(f'Tong so met vuong cua {n} con trau la {t}')
def main():
    print('Nhap so trau: ')
    n = nhapsonguyen()
    list_trau = nhaplist(n)
    hienthi(list_trau, n)
    maxsk(list_trau, n)
    tongdt(list_trau, n)
if __name__ == '__main__':
    main()