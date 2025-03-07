class Mesin():
    _nama = ""
    _kecepatan = 0
    _bahanBakar = ""
    _berat = 0
    _status = False

    def __init__(self, nama, kecepatan, bahanBakar, berat):
        self._nama = nama
        self._kecepatan = kecepatan
        self._bahanBakar = bahanBakar
        self._berat = berat

    def _cekMesin(self):
        if self._status:
            print("Status: Menyala")
        else:
            print("Status: Mati")

    def _nyalakan(self):
        self._status =True
        print("Mesin Dinyalakan")

    def _matikan(self):
        self._status = False
        print("Mesin Dimatikan")

class Mobil(Mesin):
    __brand = ""
    __model = ""
    __warna = ""
    __jumlahPintu = 0

    def __init__(self, Mesin, brand, model, warna, jumlahPintu):
        super().__init__(Mesin._nama, Mesin._kecepatan, Mesin._bahanBakar, Mesin._berat)
        self.__brand = brand
        self.__model = model
        self.__warna = warna
        self.__jumlahPintu = jumlahPintu

    def nyalakanMobil(self):
        if self._status:
            print("Tidak bisa menyalakan! Mobil sudah nyala!")
        else:
            self._nyalakan()

    def getBrand(self):
        return self.__brand

    def getModel(self):
        return self.__model

    def setBrand(self, brand):
        self.__brand = brand

mesin1 = Mesin("V8", 120, "Besin", 28)
mobil1 = Mobil(mesin1, "BMW", "RX-8", "Silver", 2)
mobil1.nyalakanMobil()
print(mobil1.getBrand())
mobil1.setBrand("GTX")
print(mobil1.getBrand())
