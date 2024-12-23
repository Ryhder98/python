#Bai 35
import math
class Ptrb2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
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