# **Kunci Soal PTS PPLG**

## **Kunci Jawaban Soal Pilihan Ganda (PG)**

1. **B**. Dasar Python seperti variabel, tipe data, fungsi, loop, dan OOP
2. **B**. Menangani input dari pemain
3. **A**. Python dan Pygame
4. **D**. Memindahkan atau menggambar gambar atau objek ke layar
5. **B**. `pygame.display.set_mode()`
6. **B**. `pygame.draw.circle()`
7. **A**. Jumlah gambar yang ditampilkan dalam satu detik
8. **B**. Memperbarui tampilan layar
9. **B**. Menggunakan `pygame.Rect.colliderect()`
10. **C**. Mengontrol frame rate game
11. **A**. `pygame.Font`
12. **C.** Dengan menggunakan `pygame.event.get()` dan memeriksa `pygame.KEYDOWN`
13. **A**. Menambahkan kecepatan objek pada sumbu X
14. **B**. Untuk mengatur kecepatan animasi dan gerakan objek
15. **B**. `pygame.mixer.music.load()`
16. **E**. Menggunakan `pickle` atau `json` untuk menyimpan dan memuat data
17. **B**. Snake head
18. **A**. Orientasi pada Objek, prinsip pemrograman yang berfokus pada objek dan class
19. **C**. Objek untuk mengatur posisi dan ukuran objek berbentuk persegi panjang
20. **B**. `pygame.display.flip()`

---

## **Kunci Jawaban Soal AKM**

**1.** Untuk mendeteksi kolisi antara objek dalam Pygame, Anda dapat menggunakan **pygame.Rect** untuk menentukan area objek (seperti persegi panjang) dan kemudian memeriksa apakah dua objek berbenturan dengan menggunakan fungsi `colliderect()`. Dengan `pygame.Rect`, Anda dapat membuat area deteksi untuk setiap objek, dan kemudian menggunakan `if rect1.colliderect(rect2):` untuk mendeteksi kolisi antara dua objek.

**2.** Untuk menangani pergerakan objek yang terbatas dalam area tertentu, Anda perlu memeriksa apakah posisi objek sudah melewati batas dari jendela game. Ini dikenal dengan boundary checking. Untuk setiap pergerakan objek (misalnya, posisi objek yang berubah pada sumbu X atau Y), Anda perlu memeriksa apakah posisi objek berada di dalam batas yang ditentukan (misalnya, di dalam lebar dan tinggi jendela game).

**3.** Dalam game, Anda dapat mengatur **frame rate** menggunakan `pygame.time.Clock()` untuk mengontrol kecepatan animasi dan gerakan objek. **Event loop** menangani input dari pemain dan memperbarui tampilan game. Frame rate dapat diatur dengan `clock.tick(fps)`, di mana `fps` adalah jumlah frame per detik yang Anda inginkan. Hal ini memastikan objek bergerak dengan kecepatan yang konsisten, terlepas dari kecepatan komputer.

**4.** Untuk menambahkan sistem skor dan menampilkan teks, Anda bisa menggunakan objek **pygame.Font** untuk membuat font dan **pygame.render()** untuk menggambar teks di layar. Misalnya, `font = pygame.font.SysFont('Arial', 30)` dan `text = font.render(str(score), True, (255, 255, 255))` untuk menampilkan skor berwarna putih.

**5.** Untuk menangani input dari keyboard dalam Pygame, Anda bisa menggunakan `pygame.key.get_pressed()` untuk memeriksa tombol yang sedang ditekan, dan berdasarkan itu, memperbarui posisi objek (seperti objek pemain) untuk bergerak ke kiri, kanan, atas, atau bawah. Anda bisa menghubungkan input tombol dengan gerakan objek dengan memodifikasi nilai koordinat objek pada sumbu X dan Y sesuai dengan tombol yang ditekan.

---
