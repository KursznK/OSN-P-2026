import re
import pandas as pd
from pypdf import PdfReader

def extract_osn_data(pdf_path, output_csv_path):
    print(f"Membaca file: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""
    
    # Data peserta berada di lampiran, mulai dari halaman ke-4 (indeks 3) hingga selesai
    for page in reader.pages[3:]:
        text += page.extract_text() + " "
    
    # Menghapus karakter baris baru (newline) agar teks menjadi satu baris panjang
    # Hal ini mempermudah pencocokan pola karena beberapa baris tabel terpotong
    flat_text = text.replace('\n', ' ')
    
    # Daftar cabang lomba OSN untuk mendeteksi awal baris
    cabang_list = [
        "ASTRONOMI", "BIOLOGI", "EKONOMI", "FISIKA", "GEOGRAFI", 
        "INFORMATIKA", "KEBUMIAN", "KIMIA", "MATEMATIKA"
    ]
    cabang_pattern = "|".join(cabang_list)
    
    # Membuat pola Regex untuk menangkap data dengan format:
    # 1. Nomor (1-3 digit)
    # 2. Cabang Lomba
    # 3. Nama Siswa (Karakter bebas sebelum NPSN)
    # 4. NPSN (Selalu 8 digit angka)
    # 5. Nama Sekolah (Karakter bebas sebelum Kabupaten/Kota)
    # 6. Kabupaten / Kota / Negara (Ditandai dengan KOTA, KAB, atau nama negara)
    # 7. Provinsi / Luar Negeri (Ditandai dengan PROV atau LUAR NEGERI)
    
    regex_pattern = (
        rf"(\d{{1,3}})\s+({cabang_pattern})\s+(.*?)\s+(\d{{8}})\s+(.*?)\s+"
        rf"((?:KOTA|KAB\.|KAB\s|SINGAPURA|JAPAN|MALAYSIA|THAILAND|ARAB SAUDI).*?)\s+"
        rf"(PROV\..+?|PROV\s.+?|LUAR NEGERI)"
        rf"(?=\s+\d{{1,3}}\s+(?:{cabang_pattern})|\s*$|\s+Halaman)"
    )
    
    pattern = re.compile(regex_pattern, re.IGNORECASE)
    matches = pattern.findall(flat_text)
    
    # Menyusun hasil tangkapan ke dalam struktur DataFrame Pandas
    columns = ["NO", "CABANG", "NAMA", "NPSN", "SEKOLAH", "KABUPATEN / KOTA", "PROVINSI"]
    df = pd.DataFrame(matches, columns=columns)
    
    # Membersihkan spasi ganda atau spasi berlebih pada setiap sel data
    df = df.apply(lambda x: x.str.strip().str.replace(r'\s+', ' ', regex=True))
    
    # Menyimpan data ke format CSV
    df.to_csv(output_csv_path, index=False)
    
    print(f"Berhasil mengekstrak {len(df)} baris data!")
    print(f"File CSV telah disimpan ke: {output_csv_path}")

if __name__ == "__main__":
    # Ganti dengan nama file PDF dan output yang diinginkan
    input_pdf = "Surat Pengumuman Peserta Semifinal OSN Dikmen 2026.pdf"
    output_csv = "Peserta_Semifinal_OSN_2026.csv"
    
    extract_osn_data(input_pdf, output_csv)
