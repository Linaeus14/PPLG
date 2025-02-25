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
    brand = ""
    model = ""
    warna = ""
    jumlahPintu = 0

    def __init__(self, Mesin, brand, model, warna, jumlahPintu):
        super().__init__(Mesin._nama, Mesin._kecepatan, Mesin._bahanBakar, Mesin._berat)
        self.brand = brand
        self.model = model
        self.warna = warna
        self.jumlahPintu = jumlahPintu

    def nyalakanMobil(self):
        self._nyalakan()

    def klakson():
        print("Beep Beep")

mesin1 = Mesin("V8", 120, "Besin", 28)
mobil1 = Mobil(mesin1, "BMW", "RX-8", "Silver", 2)
mobil1.nyalakanMobil()
