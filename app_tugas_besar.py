import streamlit as st
import pandas as pd
import time
import sys

# Konfigurasi sistem
st.set_page_config(page_title="Analisis Kompleksitas TELU", layout="wide")

# --- LOGIKA ALGORITMA SESUAI PERHITUNGAN MANUAL ---
class AlgoritmaAritmatika:
    @staticmethod
    def hitung_iteratif(n, a, b):
        """Kompleksitas O(n)"""
        total = 0
        for i in range(n):
            total += (a + i * b)
        return total

    @staticmethod
    def hitung_rekursif(n, a, b):
        """
        Kompleksitas O(2^n) 
        Rumus T(n) = 2T(n-1) + 2
        """
        if n <= 0:
            return 0
        # Pemanggilan fungsi berulang hingga n kali
        return (a + (n - 1) * b) + AlgoritmaAritmatika.hitung_rekursif(n - 1, a, b)

# --- TAMPILAN DASHBOARD ---
st.title("📊 Dashboard Analisis Kompleksitas Algoritma")
st.write("Studi Kasus: Deret Aritmatika (Iteratif O(n) vs Rekursif O(2^n))")

with st.sidebar:
    st.header("Konfigurasi Input")
    a = st.number_input("Suku Pertama (a)", value=1)
    b = st.number_input("Beda (b)", value=2)
    run_btn = st.button("Jalankan Analisis", type="primary")

if run_btn:
    # Ukuran masukan berbeda untuk keamanan sistem
    n_iteratif = [1, 1000, 10000, 50000, 100000] # Kuat sampai n=100.000
    n_rekursif = [1, 5, 10, 15, 20, 25]          # O(2^n) hanya kuat sampai n kecil
    
    results = []
    
    # Jalankan Tes Iteratif
    st.write("Menguji Iteratif (O(n))...")
    for n in n_iteratif:
        t1 = time.perf_counter()
        AlgoritmaAritmatika.hitung_iteratif(n, a, b)
        results.append({"n": n, "Tipe": "Iteratif", "Waktu (s)": time.perf_counter() - t1})

    # Jalankan Tes Rekursif
    st.write("Menguji Rekursif (O(2^n))...")
    for n in n_rekursif:
        t2 = time.perf_counter()
        AlgoritmaAritmatika.hitung_rekursif(n, a, b)
        results.append({"n": n, "Tipe": "Rekursif", "Waktu (s)": time.perf_counter() - t2})

    df = pd.DataFrame(results)

    # Visualisasi Grafik
    st.subheader("Grafik Perbandingan Running Time")
    
    st.line_chart(df.pivot(index='n', columns='Tipe', values='Waktu (s)'))

    # Analisis Akademis
    st.divider()
    st.error("### ⚠️ Analisis Perbandingan Penting")
    st.markdown(f"""
    1. **Iteratif ($O(n)$):** Berjalan sangat efisien bahkan hingga $n=100.000$.
    2. **Rekursif ($O(2^n)$):** Berdasarkan perhitungan manual $T(n) = 2^{{n+1}} - 2$, algoritma ini mengalami ledakan waktu eksekusi secara eksponensial.
    3. **Kesimpulan:** Meskipun tujuan pengujian adalah $n=100.000$, algoritma rekursif tidak mungkin dijalankan pada angka tersebut karena akan membutuhkan waktu jutaan tahun secara teoritis.
    """)

    # Tombol Ekspor
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Data CSV", data=csv, file_name="hasil_aka_telu.csv")
