import pygame
import random
from pygame.locals import K_w, K_a, K_s, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.locals import K_BACKSPACE, KEYDOWN, QUIT

# Pendefinisian objek game kotak dengan membuat class dengan nama Square
class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Square, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect(topleft=(x, y))

# Pendefinisian objek game kotak dengan membuat class dengan nama Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Surface dengan argumen tambahan SRCALPHA menghasilkan surface dengan transparani rgb
        self.surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.surf.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surf, (225, 100, 200), pygame.Rect(5, 5, 20, 20))
        self.rect = self.surf.get_rect()

        # Menetukan posisi tengah layar
        # Ukurannya 800x600, jadi tengahnya (400, 300)
        self.rect.center = (400, 300)

    def moveRight(self):
        self.rect.x += 9

    def moveLeft(self):
        self.rect.x -= 9

    def moveDown(self):
        self.rect.y += 9

    def moveUp(self):
        self.rect.y -= 9

# Class untuk membuat garis border
class Line(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super(Line, self).__init__()
        # Memastikan garis selalu memiliki ketebalan
        if x1 == x2:  # Vertical
            self.surf = pygame.Surface((1, abs(y2 - y1)))
        elif y1 == y2:  # Horizontal
            self.surf = pygame.Surface((abs(x2 - x1), 1))
        else:
            self.surf = pygame.Surface((abs(x2 - x1), abs(y2 - y1)))
        self.surf.fill((255, 255, 255))  # Garis berwarna putih
        self.rect = self.surf.get_rect(topleft=(x1, y1))

    def update(self):
        # Garis tetap di tempat yang sama, jadi tidak perlu pergerakan
        pass

# Class untuk membuat lingkaran
class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Circle, self).__init__()
        self.surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, (120,0,10), (10, 10), 10)
        self.rect = self.surf.get_rect(topleft=(x, y))

# Fungsi untuk memeriksa input dan kolisi
def handle_input_and_collision(player, borders, squares, circle, keys):
    if keys[K_RIGHT] or keys[K_d]:
        player.moveRight()
        if pygame.sprite.spritecollide(player, borders, False) or pygame.sprite.spritecollide(player, squares, False):
            player.moveLeft()
    if keys[K_LEFT] or keys[K_a]:
        player.moveLeft()
        if pygame.sprite.spritecollide(player, borders, False) or pygame.sprite.spritecollide(player, squares, False):
            player.moveRight()
    if keys[K_DOWN] or keys[K_s]:
        player.moveDown()
        if pygame.sprite.spritecollide(player, borders, False) or pygame.sprite.spritecollide(player, squares, False):
            player.moveUp()
    if keys[K_UP] or keys[K_w]:
        player.moveUp()
        if pygame.sprite.spritecollide(player, borders, False) or pygame.sprite.spritecollide(player, squares, False):
            player.moveDown()

    # Deteksi tabrakan dengan lingkaran
    if pygame.sprite.collide_rect(player, circle):
        return True
    return False

# Fungsi untuk membuat lingkaran di posisi acak
def create_random_circle(squares, borders, player):
    while True:
        x = random.randint(0, 770)
        y = random.randint(0, 570)
        circle = Circle(x, y)
        if not pygame.sprite.spritecollide(circle, squares, False) and not pygame.sprite.spritecollide(circle, borders, False) and not pygame.sprite.collide_rect(circle, player):
            return circle

# inisialisasi pygame
pygame.init()

# Menentukan judul layar/window/game
pygame.display.set_caption("Game Kotak")

# Menentukan dimensi layar
screen = pygame.display.set_mode((800, 600))

# Mendeklarasi tick/frame dari game
frame = pygame.time.Clock()

# Menginisialisasi objek player
player = Player()

# Menginstansiasi objek kotak
square1 = Square(40, 40)
square2 = Square(40, 520)
square3 = Square(720, 40)
square4 = Square(720, 520)

# Membuat objek-objek garis batas
top_border = Line(1, 1, 799, 1)    # Garis atas
bottom_border = Line(1, 599, 799, 599)  # Garis bawah
left_border = Line(1, 1, 1, 599)  # Garis kiri
right_border = Line(799, 1, 799, 599)  # Garis kanan

# Pembuatan grup sprite dan menambahkan objek-objek ke dalamnya
# Memudahkan pengaturan kolisi objek dengan objek-objek lain
squares = pygame.sprite.Group()
squares.add(square1, square2, square3, square4)

# Membuat grup untuk garis border
borders = pygame.sprite.Group()
borders.add(top_border, bottom_border, left_border, right_border)

# Membuat lingkaran di posisi acak
circle = create_random_circle(squares, borders, player)

# Variabel untuk menjaga loop game tetap berjalan
gameOn = True

# Variabel untuk menyimpan skor
score = 0
font = pygame.font.Font(None, 36)

# Loop game utama
while gameOn:
    # loop melalui antrean event
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False

        # Cek key tipe tekan sekali (bukan tahan)
        if event.type == KEYDOWN and event.key == K_BACKSPACE:
            gameOn = False

    # Definisi keadaan tombol keyboard apakah ditekan atau tidak setiap frame
    keys = pygame.key.get_pressed()

    # Tangani input dan kolisi
    if handle_input_and_collision(player, borders, squares, circle, keys):
        score += 1
        circle = create_random_circle(squares, borders, player)

    # Bersihkan layar menjadi hitam sebelum menggambar objek-objek ulang
    screen.fill((0, 0, 0))

    # Menggunakan blit untuk menggambar objek-objek di layar
    screen.blit(player.surf, player.rect.topleft) # Player
    for square in squares: # Loop untuk group objek
        screen.blit(square.surf, square.rect.topleft)

    # Menggambar border (garis batas) di sekeliling layar
    for border in borders:
        screen.blit(border.surf, border.rect.topleft)

    # Menggambar lingkaran
    screen.blit(circle.surf, circle.rect.topleft)

    # Menggambar skor
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Memperbarui tampilan dengan flip
    pygame.display.flip()

    # Penentuan frame per detik
    frame.tick(60)

# Menutup pygame setelah keluar dari loop
pygame.quit()
