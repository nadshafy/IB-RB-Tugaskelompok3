# Sistem Pakar Diagnostik Kerusakan Mobil

### Tugas 3 – Mata Kuliah Inteligensi Buatan (Artificial Intelligence)

## Deskripsi Singkat

Program ini merupakan implementasi Sistem Pakar berbasis aturan (Rule-Based Expert System) untuk mendiagnosis kemungkinan penyebab kerusakan pada mobil.
Sistem menggunakan dua metode penalaran utama:

* Forward Chaining (Penalaran Maju)
→ Menarik kesimpulan berdasarkan fakta awal yang diketahui.

* Backward Chaining (Penalaran Mundur)
→ Membuktikan suatu hipotesis atau tujuan dengan menelusuri aturan yang relevan secara mundur.

### Knowledge Base (Basis Pengetahuan)

Basis pengetahuan terdiri dari dua komponen utama:

Fakta: kondisi atau data yang diketahui dari situasi sebenarnya.
Contoh fakta awal:

``` "Mesin Mati Total", "Suara Klik saat Start", "Tidak Ada Karat pada Terminal" ```


Aturan (Rules): logika yang digunakan sistem dalam bentuk JIKA–MAKA (IF–THEN).
```
ID	Aturan Produksi (IF–THEN)	Prioritas
R1	JIKA Mesin Mati Total → MAKA Cek Kelistrikan	Rendah
R2	JIKA Mesin Berputar Lambat → MAKA Aki Lemah	Sedang
R3	JIKA Lampu Redup → MAKA Aki Lemah	Sedang
R4	JIKA Aki Lemah DAN Tidak Ada Karat pada Terminal → MAKA Ganti Aki	Tinggi
R5	JIKA Suara Klik saat Start → MAKA Aki Lemah	Sedang
R6	JIKA Mesin Mati Total DAN Tidak Ada Suara → MAKA Fungsi Kelistrikan Terputus	Tinggi
R7	JIKA Aki Lemah → MAKA Mesin Sulit Start	Rendah
R8	JIKA Cek Kelistrikan → MAKA Isolasi Kelistrikan	Tertinggi
```

Aturan diurutkan berdasarkan prioritas (conflict resolution) dari tertinggi ke terendah:
R8 > R4 > R6 > R5/R2/R3 > R1/R7

## Struktur Program

File utama: sistem_pakar_mobil.py

Program terdiri dari tiga bagian utama:

* Basis Pengetahuan :
Menyimpan daftar aturan dan fakta awal.

* Forward Chaining :
Menjalankan inferensi berdasarkan fakta yang ada hingga tidak ada aturan baru yang dapat diaktifkan.

* Backward Chaining :
Membuktikan suatu tujuan (misalnya “Ganti Aki”) dengan menelusuri aturan yang menghasilkan kesimpulan tersebut.

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal

Cek versi Python di terminal:
```
python3 --version
```

2. Jalankan program di terminal

Masuk ke direktori tempat file berada, lalu jalankan:
```
main.py
```

3. Hasil yang Ditampilkan

Program akan menampilkan dua proses inferensi:

* Forward Chaining: menunjukkan urutan aktivasi aturan berdasarkan prioritas.

* Backward Chaining: menunjukkan langkah-langkah pembuktian untuk mencapai tujuan.

Contoh output:
```
python3 sistem_pakar_mobil
=== SISTEM PAKAR: DIAGNOSA KERUSAKAN MOBIL ===
Fakta awal: {'Mesin Mati Total', 'Suara Klik saat Start', 'Tidak Ada Karat pada Terminal'}

--- Proses Forward Chaining ---
Aktivasi R5: ['Suara Klik saat Start'] → Aki Lemah
Aktivasi R4: ['Aki Lemah', 'Tidak Ada Karat pada Terminal'] → Ganti Aki
Aktivasi R1: ['Mesin Mati Total'] → Cek Kelistrikan
Aktivasi R8: ['Cek Kelistrikan'] → Isolasi Kelistrikan

--- Proses Backward Chaining ---
Membuktikan tujuan: Ganti Aki
✅ Aturan R4 terpenuhi, menambah 'Ganti Aki' ke fakta.

✅ Kesimpulan: 'Ganti Aki' TERBUKTI berdasarkan fakta dan aturan yang ada.
```

### Penjelasan Singkat
* Forward Chaining

Metode ini memulai penalaran dari fakta yang diketahui menuju kesimpulan baru.
Sistem secara iteratif mencari aturan yang premisnya sesuai dengan fakta, menambahkan hasilnya ke basis fakta, dan melanjutkan hingga tidak ada aturan baru yang dapat diaktifkan.

* Backward Chaining

Metode ini bekerja dengan tujuan tertentu (goal), lalu menelusuri aturan-aturan yang dapat membuktikan tujuan tersebut.
Jika semua kondisi dari aturan yang relevan dapat dibuktikan dari fakta yang ada, maka tujuan dianggap terbukti benar.

### Kesimpulan

Sistem pakar ini berhasil:

1. Menarik kesimpulan otomatis bahwa kerusakan disebabkan oleh Aki Lemah, sehingga perlu Ganti Aki.

2. Menunjukkan bahwa metode Forward dan Backward Chaining dapat digunakan secara saling melengkapi untuk pengambilan keputusan berbasis aturan.

#### Pengembang

* Hildyah Maretasya Araffad (123140151)

* Nadya Shafwah Yusuf (123140167)

* Firman H Gultom (123140171)

#### Kelas: RB

#### Mata Kuliah: Inteligensi Buatan

#### Dosen Pengampu: Andika Setiawan S. Kom., M. Cs.
