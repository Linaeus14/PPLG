# **Soal PTS PPLG**

## **Soal Pilihan Ganda (PG)**

### 1. Apa yang harus dikuasai terlebih dahulu sebelum mulai belajar Pygame?

A. Pygame library
B. Dasar Python seperti variabel, tipe data, fungsi, loop, dan OOP
C. Membuat jendela game
D. Membuat animasi objek
E. Membuat sistem skor

### 2. Fungsi yang paling utama dari event loop (pengecekan event) dalam Pygame adalah untuk?

A. Menjalankan animasi
B. Menangani input dari pemain
C. Menggambar objek
D. Memperbarui skor
E. Semua jawaban benar

### 3. Untuk memulai dengan Pygame, apa yang perlu diinstal terlebih dahulu?

A. Python dan Pygame
B. Pygame dan Unity
C. Python dan NumPy
D. Hanya Python
E. Hanya Pygame

### 4. Apa yang dimaksud dengan "Blit" dalam Pygame?

A. Fungsi untuk menggambar teks di layar
B. Menambahkan objek ke dalam layar
C. Menyimpan status game
D. Memindahkan atau menggambar gambar atau objek ke layar
E. Mengatur kecepatan animasi

### 5. Untuk membuat jendela game dalam Pygame, fungsi mana yang digunakan?

A. pygame.draw.rect()
B. pygame.display.set_mode()
C. pygame.image.load()
D. pygame.init()
E. pygame.time.delay()

### 6. Fungsi mana yang digunakan untuk menggambar lingkaran di layar pada Pygame?

A. pygame.draw.line()
B. pygame.draw.circle()
C. pygame.draw.rect()
D. pygame.display.update()
E. pygame.draw.polygon()

### 7. Apa yang dimaksud dengan "frame rate" dalam pengembangan game menggunakan Pygame?

A. Jumlah gambar yang ditampilkan dalam satu detik
B. Kecepatan gerakan objek
C. Jumlah teks yang ditampilkan
D. Durasi waktu sebuah objek bergerak
E. Kecepatan suara dalam game

### 8. Apa tujuan dari fungsi `pygame.display.flip()`?

A. Menggambar objek di layar
B. Memperbarui tampilan layar dengan mengganti buffer layar
C. Menangani input dari pemain
D. Mengatur kecepatan frame rate
E. Menyimpan status game

### 9. Dalam Pygame, bagaimana cara mendeteksi kolisi antara dua objek?

A. Menggunakan fungsi `pygame.collide()`
B. Menggunakan `pygame.Rect.colliderect()`
C. Menggunakan `pygame.event.get()`
D. Menggunakan `pygame.draw.collide()`
E. Menggunakan `pygame.update()`

### 10. Apa fungsi dari `pygame.time.Clock()`?

A. Mengatur ukuran jendela game
B. Menambahkan musik ke dalam game
C. Mengontrol frame rate game
D. Menyimpan status game
E. Mengatur warna latar belakang

### 11. Untuk menampilkan teks di layar pada Pygame, kita harus menggunakan objek apa?

A. `pygame.Font`
B. `pygame.Image`
C. `pygame.Sound`
D. `pygame.Text`
E. `pygame.Surface`

### 12. Bagaimana cara untuk mendapatkan input dari pemain menggunakan keyboard dalam Pygame dengan **`pygame.KEYDOWN`**?

A. Dengan menggunakan `pygame.key.get_pressed()`
B. Dengan menggunakan `pygame.mouse.get_pos()`
C. Dengan menggunakan `pygame.event.get()` dan memeriksa `pygame.KEYDOWN`
D. Dengan menggunakan `pygame.key.event()`
E. Dengan menggunakan `pygame.key.is_pressed()`

### 13. Bagaimana cara agar objek dalam Pygame bergerak ke kanan dalam game?

A. Menambahkan kecepatan objek pada sumbu X
B. Mengubah warna objek
C. Mengatur posisi objek menggunakan `pygame.display.update()`
D. Menambahkan waktu delay
E. Menggunakan `pygame.key.get_pressed()`

### 14. Apa tujuan utama dari manajemen waktu (frame rate) dalam game Pygame?

A. Untuk menentukan warna objek
B. Untuk mengatur kecepatan animasi dan gerakan objek
C. Untuk menentukan ukuran jendela game
D. Untuk mengontrol input pemain
E. Untuk mengubah suara dalam game

### 15. Untuk menambahkan suara atau musik dalam game Pygame, apa yang harus digunakan?

A. `pygame.image.load()`
B. `pygame.mixer.music.load()`
C. `pygame.display.flip()`
D. `pygame.time.delay()`
E. `pygame.font.Font()`

### 16. Bagaimana cara untuk menambahkan fitur simpan dan muat game dalam Pygame?

A. Menggunakan file teks untuk menyimpan status
B. Menggunakan modul `pygame.save()`
C. Menggunakan modul `pygame.mixer`
D. Menggunakan `pygame.event.save()`
E. Menggunakan `json` untuk menyimpan dan memuat data

### 17. Pada saat membuat game Snake, objek apa yang harus terus bergerak?

A. Makanan
B. Snake head
C. Latar belakang
D. Skor
E. Sistem suara

### 18. Apa yang dimaksud dengan **"OOP"** dalam konteks pengembangan game menggunakan Python?

A. Orientasi pada Objek, prinsip pemrograman yang berfokus pada objek dan class
B. Penggunaan objek dalam game
C. Pengaturan posisi objek dalam game
D. Sistem kontrol untuk objek
E. Tidak ada yang benar

### 19. Apa yang dimaksud dengan **"pygame.Rect"**?

A. Modul untuk mengatur waktu
B. Objek untuk menggambar garis
C. Objek untuk mengatur posisi dan ukuran objek berbentuk persegi panjang
D. Fungsi untuk menggambar lingkaran
E. Fungsi untuk menangani input mouse

### 20. Bagaimana cara memperbarui tampilan layar setelah menggambar objek baru di Pygame?

A. `pygame.draw.update()`
B. `pygame.display.flip()`
C. `pygame.update()`
D. `pygame.draw.rect()`
E. `pygame.display.clear()`

---

## **Soal AKM**

### 1. (Bergambar) Berikut adalah gambar dari sebuah permainan "Snake" yang memiliki objek bergerak. Jelaskan bagaimana Anda dapat menggunakan Pygame untuk mendeteksi kolisi antara objek tersebut dengan menggunakan **pygame.Rect**

### 2. Dalam pengembangan game menggunakan Pygame, sering kali objek bergerak dalam ruang dua dimensi. Jelaskan bagaimana Anda bisa menangani pergerakan objek yang terbatas dalam area tertentu (misalnya, objek yang tidak boleh keluar dari jendela game) dengan memanfaatkan konsep boundary checking atau pengecekan kordinat

### 3. Dalam game Snake, dengan objek ular yang bergerak di layar. Jelaskan bagaimana Anda dapat menggunakan **frame rate** dan **event pada game loop** untuk mengontrol kecepatan objek bergerak dan interaksi pemain

### 4. (Bergambar) Pada gambar berikut terdapat tampilan antarmuka game yang menampilkan skor. Bagaimana Anda dapat menambahkan sistem skor dan menampilkan teks di layar dengan menggunakan Pygame?

### 5. Dalam game sederhana Snake, pemain dapat menggunakan tombol keyboard untuk menggerakkan objek. Berdasarkan pernyataan ini, jelaskan bagaimana Anda dapat menangani input dari keyboard dalam Pygame untuk menggerakkan objek tersebut

---
