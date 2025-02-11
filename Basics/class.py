class Mesin():
    nama = ""
    kecepatan = 0
    bahan_bakar = ""

    def __init__(self, nama, kecepatan, bahan_bakar):
        self.nama = nama
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar

    def nyalakan(self):
        print("Mesin dinyalakan")

    def cekBahanBakar(self):
        return self.bahan_bakar

mesin1 = Mesin("V12", 300, "Bensin")
bahanBakar = mesin1.cekBahanBakar()
print(bahanBakar)
mesin1.nyalakan()