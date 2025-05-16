# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah lembaga pendidikan tinggi yang berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah meluluskan banyak mahasiswa dengan prestasi gemilang. Namun demikian, masih terdapat sejumlah mahasiswa yang tidak berhasil menyelesaikan studi mereka atau mengalami dropout. Untuk itu, diperlukan sebuah analisis terhadap faktor-faktor yang berkontribusi terhadap tingginya angka dropout, agar Jaya Jaya Institut dapat segera memberikan pendampingan khusus kepada mahasiswa yang berisiko.

## Permasalahan Bisnis

Jaya Jaya Institut saat ini dihadapkan pada tantangan besar terkait tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Fenomena ini tidak hanya berdampak pada reputasi dan stabilitas keuangan institusi, tetapi juga membawa konsekuensi negatif bagi para mahasiswa yang gagal menyelesaikan pendidikan mereka.

Dropout yang tinggi berpotensi menurunkan tingkat kepercayaan calon mahasiswa beserta orang tua terhadap mutu pendidikan yang ditawarkan. Beberapa isu bisnis utama yang muncul akibat kondisi ini meliputi:

* **Citra Institusi**: Tingkat dropout yang signifikan berisiko menodai reputasi Jaya Jaya Institut sebagai lembaga pendidikan yang kredibel dan berkualitas.
* **Penurunan Pendapatan**: Setiap mahasiswa yang keluar sebelum lulus menyebabkan hilangnya potensi pemasukan dari biaya kuliah dan pendukung lainnya.
* **Dampak terhadap Akreditasi**: Persentase kelulusan yang rendah dapat memengaruhi penilaian akreditasi institusi secara keseluruhan.
* **Ketidakpuasan Para Pemangku Kepentingan**: Kepercayaan mahasiswa, orang tua, dan masyarakat luas bisa menurun apabila institusi dianggap kurang efektif dalam membimbing mahasiswa hingga lulus.

# Cakupan Proyek

* Melakukan pengumpulan serta pengolahan data mahasiswa.
* Menganalisis data untuk mengidentifikasi apa saja hal yang menyebabkan dropout mahasiswa.
* Mengembangkan model prediksi menggunakan 3 algoritma yang ada untuk memprediksi.
* Mendesain dashboard untuk memvisualisasikan prediksi.
* Menyusun **action recommendation** berdasarkan temuan yang diperoleh.

# Persiapan

Berikut adalah tahapan untuk menyiapkannya:

**Sumber data**: [Student Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Di sini, untuk melakukan proses, saya sepenuhnya menggunakan Google Colab. Baru kemudian pada bagian visualisasi menggunakan Metabase dengan Docker. Tapi jika ingin menjalankan proyek secara lokal, dapat dilakukan dengan cara berikut:

1. Buka terminal di VS Code.
2. Jalankan perintah berikut:

   ```bash
   conda create --name submissionds python==3.9.21
   ```
3. Jalankan perintah kedua untuk mengaktifkan virtual environment:

   ```bash
   conda activate submissionds
   ```
4. Lanjut ke tahap untuk melihat model prediksi menggunakan Streamlit.

# Business Dashboard

Dashboard bisnis ini dirancang untuk memprediksi kemungkinan seorang mahasiswa mengalami dropout di Jaya Jaya Institut. Prediksi dilakukan menggunakan model machine learning yang telah dilatih sebelumnya dan diintegrasikan ke dalam dashboard untuk memberikan hasil secara real-time berdasarkan data yang dimasukkan.

Dashboard menyediakan berbagai kolom input yang merepresentasikan faktor-faktor yang dapat memengaruhi keputusan mahasiswa untuk berhenti studi, seperti jalur pendaftaran, mata kuliah yang diambil, latar belakang pendidikan, pekerjaan orang tua, serta aspek akademik lainnya.

Hasil prediksi ditampilkan secara langsung menggunakan model yang sudah disimpan, sehingga pengguna dapat memperoleh wawasan cepat mengenai risiko dropout setiap mahasiswa.

Dengan adanya dashboard ini, diharapkan pihak Jaya Jaya Institut dapat segera mengidentifikasi mahasiswa yang berisiko dan menerapkan langkah-langkah pencegahan lebih awal guna menekan angka dropout dan meningkatkan keberhasilan studi mahasiswa.

# Menjalankan Sistem Machine Learning

Aplikasi prediksi keberhasilan mahasiswa menggunakan machine learning yang diimplementasikan dengan Streamlit.

Aplikasi ini telah di-deploy ke Streamlit Community Cloud dan dapat diakses melalui link berikut:
[Student Success Predictor](https://dsstudentsperformance-nbon53ohzaeomfn4sthpnn.streamlit.app/)

### 🛠️ Local Development

#### Prerequisites

* Python 3.12.7
* pip (Python package manager)

#### Installation

1. Clone repository ini:

   ```bash
   git clone https://github.com/agummds/DS_Students_Performance
   cd DS_Students_Performance
   ```
2. Aktifkan virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Pastikan file-file berikut ada di direktori yang sama dengan `app.py`:

   * `model.pkl` (model machine learning)
   * `data_agum.csv` (dataset)
5. Jalankan aplikasi secara lokal:

   ```bash
   streamlit run app.py
   ```

## 📋 Requirements

File `requirements.txt` berisi semua dependensi yang diperlukan:

```
streamlit==1.32.0
pandas==2.2.1
numpy==1.26.4
scikit-learn
matplotlib
seaborn
```

# Conclusion

Analisis terhadap fenomena mahasiswa yang mengalami dropout di Jaya Jaya Institut menunjukkan bahwa terdapat lima kelompok faktor utama yang memengaruhi keputusan mahasiswa untuk keluar dari studi, yaitu: karakteristik demografis, latar belakang pendidikan, kondisi ekonomi, situasi keluarga dan sosial, serta pencapaian akademik.

Dari hasil analisis data, faktor akademik terbukti menjadi prediktor paling signifikan terhadap kemungkinan dropout, khususnya performa pada semester awal. Jumlah mata kuliah yang lulus di semester kedua dan total satuan kredit (SKS) yang disetujui merupakan indikator yang paling kuat, diikuti oleh nilai akademik pada semester pertama.

Ditemukan pula bahwa nilai per mata kuliah memiliki pengaruh lebih besar dibandingkan frekuensi evaluasi yang dilakukan. Sementara itu, skor risiko dropout dan nilai masuk berperan secara moderat, dan usia, riwayat akademis sebelumnya, serta status pembayaran biaya kuliah menunjukkan pengaruh yang relatif kecil.

Secara keseluruhan, keberhasilan akademik pada awal masa studi, khususnya di semester kedua, menjadi penentu utama dalam mempertahankan mahasiswa hingga lulus.

# Rekomendasi Action Items Berdasarkan Analisis Dashboard

Berdasarkan analisis dashboard yang telah dibuat, berikut adalah beberapa temuan kunci:

### 1. Distribusi Status Mahasiswa

* Mayoritas mahasiswa masih dalam status "Enrolled"
* Proporsi mahasiswa yang "Dropout" perlu mendapat perhatian khusus
* Tingkat kelulusan ("Graduate") menunjukkan area yang perlu ditingkatkan

### 2. Faktor-faktor yang Mempengaruhi

* Kinerja akademik semester pertama sangat mempengaruhi keberhasilan
* Status beasiswa memiliki korelasi dengan tingkat kelulusan
* Usia saat pendaftaran menunjukkan pola tertentu

### 3. Tren dan Pola

* Ada korelasi antara nilai sebelumnya dengan keberhasilan
* Faktor ekonomi keluarga mempengaruhi kelangsungan studi
* Performa semester pertama menjadi indikator penting

## 🎯 Action Items

### 1. Program Intervensi Dini

* **Target**: Mahasiswa semester pertama
* **Aksi**:

  * Implementasi sistem early warning untuk mengidentifikasi mahasiswa berisiko
  * Program mentoring intensif untuk mahasiswa semester pertama
  * Workshop pengembangan keterampilan belajar
* **Timeline**: Implementasi di awal semester
* **KPI**: Penurunan tingkat dropout di semester pertama

### 2. Penguatan Program Beasiswa

* **Target**: Mahasiswa dengan latar belakang ekonomi menengah ke bawah
* **Aksi**:

  * Evaluasi dan perluasan program beasiswa
  * Penambahan jenis bantuan finansial
  * Program pendampingan untuk penerima beasiswa
* **Timeline**: Evaluasi triwulanan
* **KPI**: Peningkatan tingkat kelulusan penerima beasiswa

### 3. Program Akademik

* **Target**: Semua mahasiswa
* **Aksi**:

  * Pengembangan program remedial untuk mata kuliah kritis
  * Implementasi sistem tutoring peer-to-peer
  * Workshop pengembangan soft skills
* **Timeline**: Berkelanjutan
* **KPI**: Peningkatan nilai rata-rata dan tingkat kelulusan

### 4. Sistem Monitoring dan Evaluasi

* **Target**: Tim akademik dan administrasi
* **Aksi**:

  * Pengembangan dashboard real-time untuk monitoring
  * Implementasi sistem pelaporan berkala
  * Program evaluasi dan penyesuaian berkelanjutan
* **Timeline**: Evaluasi bulanan
* **KPI**: Ketepatan waktu dalam identifikasi masalah

### 5. Program Dukungan Keluarga

* **Target**: Orang tua/wali mahasiswa
* **Aksi**:

  * Program komunikasi rutin dengan orang tua
  * Workshop parenting untuk mendukung mahasiswa
  * Portal informasi untuk orang tua
* **Timeline**: Program semesteran
* **KPI**: Peningkatan keterlibatan orang tua

## 📈 Metrik Sukses

### Jangka Pendek (6 Bulan)

* Penurunan 20% tingkat dropout semester pertama
* Peningkatan 15% tingkat kelulusan
* Peningkatan 25% partisipasi dalam program mentoring

### Jangka Menengah (1 Tahun)

* Penurunan 30% tingkat dropout keseluruhan
* Peningkatan 25% tingkat kelulusan
* Peningkatan 40% kepuasan mahasiswa

### Jangka Panjang (2 Tahun)

* Penurunan 50% tingkat dropout
* Peningkatan 40% tingkat kelulusan
* Peningkatan 60% kepuasan stakeholder

## 🔄 Proses Evaluasi

### Evaluasi Bulanan

* Review metrik utama
* Penyesuaian program berdasarkan feedback
* Pelaporan ke stakeholder

### Evaluasi Triwulanan

* Analisis mendalam terhadap program
* Penyesuaian strategi
* Pelatihan dan pengembangan tim

### Evaluasi Tahunan

* Review komprehensif
* Perencanaan strategis
* Pengembangan program baru


# Email dan Password Metabase

* **Email**: [root@mail.com](mailto:root@mail.com)
* **Password**: root123
