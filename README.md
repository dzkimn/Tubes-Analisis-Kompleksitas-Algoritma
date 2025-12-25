# Analisis Kompleksitas Algoritma: Deret Aritmatika 📊

Tugas Besar Mata Kuliah Analisis Kompleksitas Algoritma - Semester Ganjil 2025/2026.

## 📝 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dan membandingkan efisiensi dua algoritma dalam menghitung **Deret Aritmatika**. Kami membandingkan pendekatan **Iteratif** yang efisien dengan pendekatan **Rekursif** yang didesain mengikuti model pertumbuhan tertentu sesuai arahan akademis

## 🧮 Analisis Teoritis
Berdasarkan perhitungan manual yang telah dilakukan:

1. **Algoritma Iteratif**:
   - **Kompleksitas Waktu**: $O(n)$ (Linear).
   - **Analisis**: Menggunakan satu perulangan `for` tunggal yang berjalan sebanyak $n$ kali.

2. **Algoritma Rekursif**:
   - **Rumus Rekurens**: $T(n) = 2T(n-1) + 2$.
   - **Kompleksitas Waktu**: $O(2^n)$ (Eksponensial).
   - **Analisis**: Menggunakan solusi persamaan karakteristik, didapatkan hasil $T(n) = 2^{n+1} - 2$, yang menunjukkan pertumbuhan waktu yang sangat cepat (ledakan eksponensial).

## 📈 Hasil Pengujian (Empiris)
Aplikasi ini melakukan pengujian *running time* dengan ukuran masukan hingga **n = 100.000**:
- **Iteratif**: Berjalan sangat stabil (sekitar 0.007 detik) bahkan untuk input maksimal.
- **Rekursif**: Mengalami lonjakan waktu yang ekstrem pada $n < 30$ karena sifat eksponensialnya.



## 🚀 Cara Menjalankan
1. Pastikan Python sudah terinstall.
2. Install library yang dibutuhkan:
   ```bash
   pip install streamlit pandas matplotlib
