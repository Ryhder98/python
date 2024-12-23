#Bai 48
import math
class Mt:
    def __init__ (self, CPU, RAM, ROM):
        self.CPU = CPU
        self.RAM = RAM
        self.ROM = ROM
    def TongRAMvaROM(self):
        return self.RAM + self.ROM
def nhapCPU():
    while True:
        n = input('Nhap: ')
        try:
            n = str(n)
            if n.isalnum() == True:
                break
        except ValueError:
            print("Nhap lai")
    return n
def nhapRAMvaROM():
    while True:
        n = input('Nhap: ')
        try:
            n = int(n)
            break
        except ValueError:
            print("Nhap lai")
    return n
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
def nhaplist(n):
    listmt = []
    for i in range(n):
        print('Nhap CPU:')
        CPU = nhapCPU()
        print('Nhap RAM:')
        RAM = nhapRAMvaROM()
        print('Nhap ROM:')
        ROM = nhapRAMvaROM()
        mt = Mt(CPU, RAM, ROM)
        listmt.append(mt)
    return listmt
def hienthi(listmt, n):
    print('{:<15}{:<15}{:<15}{:<15}'.format('CPU', 'RAM', 'ROM', 'Tong RAM va ROM'))
    for i in range(n):
        print('{:<15}{:<15}{:<15}{:<15}'.format(listmt[i].CPU, listmt[i].RAM, listmt[i].ROM, listmt[i].TongRAMvaROM()))
def tachds(listmt, n):
    m1 = m2 = 0
    listmt1 = []
    listmt2 = []
    for i in range(n):
        if listmt[i].CPU == 'Intel':
            listmt1.append(listmt[i])
            m1 += 1
        else:
            m2 += 1
            listmt2.append(listmt[i])
    return m1, m2, listmt1, listmt2
def minRam(listmt, n):
    dsRAMmin = []
    dem = 0
    Rammin = listmt[0].RAM
    for i in range(1, n):
        if listmt[i].RAM < Rammin:
            Rammin = listmt[i].RAM
    for i in range(n):
        if listmt[i].RAM == Rammin:
            dem += 1
            dsRAMmin.append(listmt[i])
    return dem, dsRAMmin

def main():
    print('Nhap vao so may tinh: ')
    n = nhapsonguyen()
    listmt = nhaplist(n)
    hienthi(listmt, n)
    m1, m2, listmt1, listmt2 = tachds(listmt, n)
    if m1 == 0:
        print('Khong co may tinh co CPU la Intel')
    else:
        print('May tinh co CPU la Intel co ten sau: ')
        hienthi(listmt1, m1)
    if m2 == 0:
        print('Khong co may tinh co CPU khac Intel')
    else:
        print('May tinh co CPU khac Intel co ten sau: ')
        hienthi(listmt2, m2)
    dem, dsRAMmin = minRam(listmt, n)
    print('Danh sach may tinh co RAM nho nhat la: ')
    hienthi(dsRAMmin, dem)

if __name__ == '__main__':
    main()


