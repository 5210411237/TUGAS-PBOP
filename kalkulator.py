class Kalkulator:
    def __init__(self,a,b):
        self.var1 = a
        self.var2 = b
        print("A = {}".format(a),",","B = {}".format(b))
    
    def tambah(self):
        print("A + B = {}".format(self.var1 + self.var2))

    def kurang(self):
        print("A - B = {}".format(self.var1 - self.var2))

    def kali(self):
        print("A x B = {}".format(self.var1 * self.var2))

    def bagi(self):
        if self.var2 == 0:
            print("Pembagian dengan nol")

        else:
            print("A / B = {}".format(self.var1/self.var2))

objek1 = Kalkulator(1,2)
objek1.tambah()
objek1.kurang()
objek1.kali()

objek2 = Kalkulator(2,0)
objek2.bagi()