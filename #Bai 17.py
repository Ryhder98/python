#Bai 17
import math
class ptrbac_2:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def giai(self):
        if self.a==0:
            if self.b==0:
                if self.c==0:
                    return "Vo so nghiem"
                else:
                    return "Vo nghiem"
            else:
                x=-self.c/self.b
                return x
        else:
            delta=self.b**2-4*self.a*self.c
            if delta<0:
                return "Vo nghiem"
            elif delta==0:
                xx=-self.b/(2*self.a)
                return xx
            else:
                x1=(-self.b+math.sqrt(delta))/(2*self.a)
                x2=(-self.b-math.sqrt(delta))/(2*self.a)
                return x1,x2
def nhapsothuc():
    while True:
        n =input('Nhap gia tri: ')
        try:
            n = float(n)
            break
        except ValueError:
            print("Nhap lai so thuc")
    return n
def nhaplistptr():
    list_ptr = []
    for i in range(2):
        print('Nhap a: ')
        a = nhapsothuc()
        print('Nhap b: ')
        b = nhapsothuc()
        print('Nhap c: ')
        c = nhapsothuc()
        ptr = ptrbac_2(a, b, c)
        list_ptr.append(ptr)
    return list_ptr
def nghiem(list_ptr):
    for i in range(2):
        print(f'Phuong trinh thu {i+1} co nghiem la: ', list_ptr[i].giai())
def tuplenghiem(list_ptr):
    list_nghiem = []
    for ptr in list_ptr:
        nghiem = ptr.giai()
        list_nghiem.append(nghiem)
    tuple_ng = tuple(list_nghiem)
    print(f'Tuple chứa các nghiệm của các phương trình: {tuple_ng}')
    return tuple_ng
def maxnghiem(list_ptr):
    list_nghiem1 = []
    for ptr in list_ptr:
        nghiem = ptr.giai()
        list_nghiem1.append(nghiem)
    maxnghiem = list_nghiem1[0]
    for i in range(1, len(list_nghiem1)):
        if list_nghiem1[i] > maxnghiem:
            maxnghiem = list_nghiem1[i]
    print(f'Nghiem lon nhat la: {maxnghiem}')
def main():
    list_ptr = nhaplistptr()
    nghiem(list_ptr)
    tuple_nghiem = tuplenghiem(list_ptr)
    maxnghiem(list_ptr)
if __name__ == '__main__':
    main()