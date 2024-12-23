#Bai 52
import math
import re
class Sinhvien:
    def __init__(self, ten, diembaocao, diempc, diempm, thuyettrinh):
        self.ten = ten
        self.diembaocao = diembaocao
        self.diempc = diempc
        self.diempm = diempm
        self.thuyettrinh = thuyettrinh
    def tongdiem(self):
        return self.diembaocao + self.diempc + self.diempm + self.thuyettrinh
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
def nhapdiembaocao_thuyettrinh():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n >= 0 and n <= 2:
                return n
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
def nhapdiemphancung_phanmem():
    while True:
        n = input('Nhap: ')
        try:
            n = float(n)
            if n >= 0 and n <= 3:
                return n
        except ValueError:
            print('Nhap sai, vui lòng nhập lại.')
def nhapten():
    while True:
        parterm = r'^[a-zA-Z\s]+$'
        ten = input('Nhap ten: ')
        if re.match(parterm, ten):
            break
        else:
            print('Nhap sai, vui lòng nhập lại.')
    return ten
def nhaplist_sv(n):
    list_sv = []
    for i in range(n):
        print(f'Nhap ten sinh vien thu {i+1}: ')
        ten = nhapten()
        print('Nhap diem bao cao: ')
        diembaocao = nhapdiembaocao_thuyettrinh()
        print('Nhap diem thiet ke phan cung: ')
        diempc = nhapdiemphancung_phanmem()
        print('Nhap diem thiet ke phan mem: ')
        diempm = nhapdiemphancung_phanmem()
        print('Nhap diem thuyet trinh: ')
        thuyettrinh = nhapdiembaocao_thuyettrinh()
        sinhvien = Sinhvien(ten, diembaocao, diempc, diempm, thuyettrinh)
        list_sv.append(sinhvien)
    return list_sv
def hienthi(list_sv, n):
    print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('Ten','Diem bao cao', 'Diem tkpc', 'Diem tkpm', 'Thuyet trinh','Tong diem'))
    for i in range(n):
        print('{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(list_sv[i].ten, list_sv[i].diembaocao, list_sv[i].diempc, list_sv[i].diempm, list_sv[i].thuyettrinh, list_sv[i].tongdiem()))
def sapxep(list_sv, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if list_sv[i].tongdiem() < list_sv[j].tongdiem():
                list_sv[i], list_sv[j] = list_sv[j], list_sv[i]
    return list_sv
def tachdanhsachsv(list_sv, n):
    sv_thietke_phancung = []
    sv_thietke_phanmem = []
    sv_codiembangnhau = []
    n1 = n2 = n3 = 0
    for sv1 in list_sv:
        if sv1.diempc > sv1.diempm:
            sv_thietke_phancung.append(sv1)
            n1+=1
        elif sv1.diempc < sv1.diempm:
            sv_thietke_phanmem.append(sv1)
            n2+=1
        else:
            sv_codiembangnhau.append(sv1)
            n3+=1
    return sv_thietke_phancung, n1, sv_thietke_phanmem, n2, sv_codiembangnhau, n3
def main():
    print('Nhap so luong sinh vien: ')
    n = nhapsonguyen()
    list_sv = nhaplist_sv(n)
    hienthi(list_sv, n)
    sapxep(list_sv, n)
    print('Danh sach sinh vien sau khi sap xep: ')
    hienthi(list_sv, n)
    sv_thietke_phancung, n1, sv_thietke_phanmem, n2, sv_codiembangnhau, n3 = tachdanhsachsv(list_sv, n)
    if len(sv_thietke_phancung) != 0: 
        print('Danh sach sinh vien thiet ke phan cung tot hon phan mem: ')
        hienthi(sv_thietke_phancung, n1)
    if len(sv_thietke_phanmem) != 0:
        print('Danh sach sinh vien thiet ke phan mem tot hon phan cung: ')
        hienthi(sv_thietke_phanmem, n2) 
    if len(sv_codiembangnhau) == n:
        print('Khong co sinh vien co diem phan cung lon hon phan mem va nguoc lai') 
if __name__ == '__main__':
    main()