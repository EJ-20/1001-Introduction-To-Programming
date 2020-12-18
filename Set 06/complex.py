class Complex:
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b 

    def __add__(self, c):
        x = (self.__a + c[0])
        y = (self.__b + c[2])
        return str(x) + "+" + str(y) + "i"

    def __sub__(self, c):
        x = (self.__a - c[0])
        y = (self.__b - c[3])
        if y < 0:
            return str(x) + str(y) + "i"
        else:
            return str(x) + "-" + str(y) + "i"

    def __mul__(self, c, d):
        x = self.__a * c[0]
        y = (self.__b * d[3]) + "i"
        return Complex(x,y)

    def __str__(self):
        return str(self.__a) + "+" + str(self.__b) + "i"
    
    def __getitem__(self, index):
        if index == 0:
            return self.__a
        else:
            return self.__b

def main():
    comp1 = Complex(1,2)
    comp2 = Complex(3,4)
    print(comp1)
    print(comp2)
    print(comp1 - comp2)
    print(comp1 + comp2)

main()
    
    
        
