# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah lembaga pendidikan tinggi yang berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah meluluskan banyak mahasiswa dengan prestasi gemilang. Namun demikian, masih terdapat sejumlah mahasiswa yang tidak berhasil menyelesaikan studi mereka atau mengalami dropout. Untuk itu, diperlukan sebuah analisis terhadap faktor-faktor yang berkontribusi terhadap tingginya angka dropout, agar Jaya Jaya Institut dapat segera memberikan pendampingan khusus kepada mahasiswa yang berisiko.

## Permasalahan Bisnis

Jaya Jaya Institut saat ini dihadapkan pada tantangan besar terkait tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Fenomena ini tidak hanya berdampak pada reputasi dan stabilitas keuangan institusi, tetapi juga membawa konsekuensi negatif bagi para mahasiswa yang gagal menyelesaikan pendidikan mereka. Dropout yang tinggi berpotensi menurunkan tingkat kepercayaan calon mahasiswa beserta orang tua terhadap mutu pendidikan yang ditawarkan. Beberapa isu bisnis utama yang muncul akibat kondisi ini meliputi:

* **Citra Institusi**: Tingkat dropout yang signifikan berisiko menodai reputasi Jaya Jaya Institut sebagai lembaga pendidikan yang kredibel dan berkualitas.
* **Penurunan Pendapatan**: Setiap mahasiswa yang keluar sebelum lulus menyebabkan hilangnya potensi pemasukan dari biaya kuliah dan pendukung lainnya.
* **Dampak terhadap Akreditasi**: Persentase kelulusan yang rendah dapat memengaruhi penilaian akreditasi institusi secara keseluruhan.
* **Ketidakpuasan Para Pemangku Kepentingan**: Kepercayaan mahasiswa, orang tua, dan masyarakat luas bisa menurun apabila institusi dianggap kurang efektif dalam membimbing mahasiswa hingga lulus.

## Cakupan Proyek

* Melakukan pengumpulan serta pengolahan data mahasiswa.
* Menganalisis data untuk mengidentifikasi apa saja hal yang menyebabkan dropout mahasiswa.
* Mengembangkan model prediksi menggunakan 3 algoritma yang ada untuk memprediksi.
* Mendesain dashboard untuk memvisualisasikan prediksi.
* Menyusun *Action Recommendation* berdasarkan temuan yang diperoleh.

## Persiapan

### 📦 Sumber Data

Dataset yang digunakan berasal dari GitHub:
[Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

### 📍 Tools

* Proses analisis dan pembuatan model dilakukan di **Google Colab**.
* Visualisasi dan integrasi model ke dalam dashboard dilakukan menggunakan **Metabase** melalui **Docker**.

### 🧪 Local Setup (Opsional)

Jika ingin menjalankan proyek secara lokal, berikut langkah-langkahnya:

1. Buka terminal di VSCode
2. Buat environment baru:

   ```bash
   conda create --name submissionds python==3.12.7
   ```
3. Aktifkan environment:

   ```bash
   conda activate submissionds
   ```
4. Clone repositori:

   ```bash
   git clone https://github.com/agummds/DS_Students_Performance
   cd DS_Students_Performance
   ```
5. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```
6. Pastikan file `model.pkl` dan `data_agum.csv` berada dalam direktori yang sama dengan `app.py`
7. Jalankan aplikasi:

   ```bash
   streamlit run app.py
   ```

### 📋 Kebutuhan Teknis

```
streamlit==1.32.0  
pandas==2.2.1  
numpy==1.26.4  
scikit-learn  
matplotlib  
seaborn
sqlalchemy
```

## Menjalankan Sistem Machine Learning

Aplikasi prediksi keberhasilan mahasiswa telah dideploy dan dapat diakses secara publik melalui link berikut:

🔗 [Student Success Predictor – Streamlit App](https://dsstudentsperformance-nbon53ohzaeomfn4sthpnn.streamlit.app/)

Atau, jika ingin mengaksesnya secara local bisa jalankan dengan perintah berikut;
6. Pastikan file `model.pkl` dan `data_agum.csv` berada dalam direktori yang sama dengan `app.py`
7. Jalankan aplikasi:

   ```bash
   streamlit run app.py
   ```

## Business Dashboard

Dashboard bisnis dikembangkan untuk memvisualisasikan informasi terkait risiko dropout mahasiswa di Jaya Jaya Institut serta faktor-faktor utama yang berkontribusi terhadap keputusan mahasiswa untuk berhenti studi.

Dashboard ini menyajikan berbagai aspek yang relevan, termasuk jalur pendaftaran, latar belakang pendidikan, status pekerjaan orang tua, mata kuliah yang diambil, serta performa akademik mahasiswa. Setiap input ini digunakan oleh model machine learning yang telah dilatih sebelumnya untuk memprediksi kemungkinan terjadinya dropout secara real-time.

Dengan tampilan yang interaktif dan hasil prediksi yang langsung ditampilkan, dashboard ini memungkinkan pihak institusi untuk dengan cepat mengidentifikasi mahasiswa yang berisiko tinggi dropout. Hal ini mendukung pengambilan keputusan yang lebih tepat dalam menyusun strategi intervensi dini guna meningkatkan retensi dan keberhasilan studi mahasiswa.

## Conclusion

Analisis terhadap fenomena mahasiswa yang mengalami dropout di Jaya Jaya Institut menunjukkan bahwa terdapat lima kelompok faktor utama yang memengaruhi keputusan mahasiswa untuk keluar dari studi, yaitu: karakteristik demografis, latar belakang pendidikan, kondisi ekonomi, situasi keluarga dan sosial, serta pencapaian akademik.

Dari hasil analisis data, faktor akademik terbukti menjadi prediktor paling signifikan terhadap kemungkinan dropout, terutama performa akademik pada semester awal. Visualisasi hubungan antara Average Grade dan Engagement Score menunjukkan bahwa mahasiswa dengan nilai rata-rata tinggi cenderung memiliki tingkat keterlibatan yang juga tinggi. Hal ini mengindikasikan bahwa keterlibatan aktif mahasiswa secara tidak langsung berkaitan dengan keberhasilan akademik dan kemungkinan menyelesaikan studi.

Indikator seperti jumlah mata kuliah yang disetujui, nilai rata-rata, serta skor keterlibatan terbukti memiliki pengaruh yang kuat terhadap kelulusan. Di sisi lain, faktor seperti skor risiko dropout (Dropout Risk Score), nilai masuk, serta status pembayaran biaya kuliah memberikan kontribusi sedang hingga rendah terhadap prediksi dropout. Faktor demografis seperti usia atau latar belakang akademis sebelumnya menunjukkan pengaruh yang lebih kecil.

Secara keseluruhan, keberhasilan akademik pada awal masa studi—yang tercermin melalui kombinasi antara nilai akademik dan skor keterlibatan—menjadi penentu utama dalam mempertahankan mahasiswa hingga lulus. Mahasiswa yang menunjukkan keterlibatan tinggi dan nilai baik di awal studi memiliki kemungkinan lebih besar untuk menyelesaikan pendidikan mereka.

## Rekomendasi Action Items

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

## 🔐 Akses Metabase

* **Email**: `root@mail.com`
* **Password**: `root123`

---

