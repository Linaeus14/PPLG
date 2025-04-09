import pygame, os, json

pygame.init()
lebar_layar = 800
tinggi_layar = 600
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Practice 3")

putih = (255, 255, 255)
hitam = (0, 0, 0)

lokasi_foto1 = "Practice/assets/image.jpg"
lokasi_foto2 = "Practice/assets/image2.jpg"
lokasi_file = "Practice/assets/save.json"

if os.path.exists(lokasi_foto1) and os.path.exists(lokasi_foto2):
    foto1 = pygame.image.load(lokasi_foto1)
    foto2 = pygame.image.load(lokasi_foto2)
    foto1 = pygame.transform.scale(foto1, (800, 600))
    foto2 = pygame.transform.scale(foto2, (800, 600))
else:
    print("File tidak ditemukan")
    pygame.quit()
    exit()

# Prosedur untuk menyimpan nomor ke file
def simpan(index):
    with open(lokasi_file, "w") as penyimpanan:
        json.dump({"index": index}, penyimpanan)

# Fungsi untuk memuat nomor dari file
def muat():
    if os.path.exists(lokasi_file):
        with open(lokasi_file, "r") as penyimpanan:
            nilai = json.load(penyimpanan)
            return nilai.get("index", 0)
    return 0

index = muat()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simpan(index)
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                index = (index + 1) % 2
    if index == 0:
        layar.blit(foto1, (0, 0))
    else:
        layar.blit(foto2, (0, 0))
    pygame.display.flip()
