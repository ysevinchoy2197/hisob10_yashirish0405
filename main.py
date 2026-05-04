#7-misol
class Dokon:
    def __init__(self, nomi, kassa):
        self.nomi = nomi
        self.kassa = kassa
        self.__kassa = 0

    def sotuv(self, summa):
        self.__kassa += summa

    def harajat(self, summa):
        self.__kassa -= summa

    def info(self):
        print(f"nomi: {self.nomi}")
        print(f"kassa: {self.__kassa}")

d1 = Dokon("Supermarket", "12 000 000")
d1.info()
