# Analisis Data Peserta Lolos OSN-P 2026 📊

Repository ini berisi skrip ekstraksi dan Exploratory Data Analysis (EDA) terhadap data sebaran peserta lolos Olimpiade Sains Nasional tingkat Provinsi (OSN-P) tahun 2026.

## Latar Belakang
Proyek ini bertujuan untuk memetakan sebaran peserta OSN-P dari berbagai bidang lomba di seluruh Indonesia. Sebagai pihak yang aktif berkontribusi dalam ekosistem olimpiade, seperti pada penyelenggaraan Olimpiade Astara Ganesha, analisis demografi peserta ini sangat penting. Hasil pemetaan ini dapat dimanfaatkan untuk memahami sebaran talenta siswa antar provinsi, mengevaluasi rasio kompetisi sekolah, dan menjadi fondasi riset saat merumuskan tingkat kesulitan soal atau simulasi kompetisi di masa mendatang.

## Teknologi yang Digunakan
Proyek ini dikembangkan menggunakan bahasa pemrograman Python dengan memanfaatkan lingkungan kerja Google Colab. Library utama yang digunakan meliputi:
*   **Pandas:** Untuk manipulasi dan agregasi data tabular.
*   **Matplotlib & Seaborn:** Untuk visualisasi data interaktif dan pembuatan grafik.

## 📂 Struktur Data & Analisis
Tahapan analisis yang terdapat di dalam *notebook* meliputi:
1.  **Data Loading:** Membaca file dataset mentah (`Peserta_Semifinal_OSN_2026.csv`).
2.  **Agregasi Provinsi:** Menghitung total peserta dari masing-masing provinsi untuk melihat peta persaingan wilayah.
3.  **Top Sekolah:** Mengidentifikasi 20 sekolah menengah atas yang menyumbang peserta terbanyak di tingkat provinsi.
4.  **Distribusi Bidang Lomba:** Melakukan tabulasi silang (*cross-tabulation*) menggunakan *heatmap* untuk melihat minat dan dominasi bidang lomba (seperti Astronomi, Fisika, Informatika, dll.) pada 10 provinsi teratas.

## Cara Menjalankan Proyek
1. *Clone repository* ini ke komputer lokal:
   ```bash
   git clone [https://github.com/KursznK/OSN-P-2026.git](https://github.com/KursznK/OSN-P-2026.git)
