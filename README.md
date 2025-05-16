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
```

## Menjalankan Sistem Machine Learning

Aplikasi prediksi keberhasilan mahasiswa telah dideploy dan dapat diakses secara publik melalui link berikut:

🔗 [Student Success Predictor – Streamlit App](https://dsstudentsperformance-nbon53ohzaeomfn4sthpnn.streamlit.app/)

## Business Dashboard

Dashboard bisnis ini dirancang untuk memprediksi kemungkinan seorang mahasiswa mengalami dropout di Jaya Jaya Institut. Prediksi dilakukan menggunakan model machine learning yang telah dilatih sebelumnya dan diintegrasikan ke dalam dashboard untuk memberikan hasil secara real-time berdasarkan data yang dimasukkan.

Dashboard menyediakan berbagai kolom input yang merepresentasikan faktor-faktor yang dapat memengaruhi keputusan mahasiswa untuk berhenti studi, seperti jalur pendaftaran, mata kuliah yang diambil, latar belakang pendidikan, pekerjaan orang tua, serta aspek akademik lainnya. Hasil prediksi ditampilkan secara langsung menggunakan model yang sudah disimpan, sehingga pengguna dapat memperoleh wawasan cepat mengenai risiko dropout setiap mahasiswa.

Dengan adanya dashboard ini, diharapkan pihak Jaya Jaya Institut dapat segera mengidentifikasi mahasiswa yang berisiko dan menerapkan langkah-langkah pencegahan lebih awal guna menekan angka dropout dan meningkatkan keberhasilan studi mahasiswa.

## Conclusion

Analisis terhadap fenomena mahasiswa yang mengalami dropout di Jaya Jaya Institut menunjukkan bahwa terdapat lima kelompok faktor utama yang memengaruhi keputusan mahasiswa untuk keluar dari studi, yaitu: karakteristik demografis, latar belakang pendidikan, kondisi ekonomi, situasi keluarga dan sosial, serta pencapaian akademik.

Dari hasil analisis data, faktor akademik terbukti menjadi prediktor paling signifikan terhadap kemungkinan dropout, khususnya performa pada semester awal. Jumlah mata kuliah yang lulus di semester kedua dan total satuan kredit (SKS) yang disetujui merupakan indikator yang paling kuat, diikuti oleh nilai akademik pada semester pertama. Ditemukan pula bahwa nilai per mata kuliah memiliki pengaruh lebih besar dibandingkan frekuensi evaluasi yang dilakukan. Sementara itu, skor risiko dropout dan nilai masuk berperan secara moderat, dan usia, riwayat akademis sebelumnya, serta status pembayaran biaya kuliah menunjukkan pengaruh yang relatif kecil.

Secara keseluruhan, keberhasilan akademik pada awal masa studi, khususnya di semester kedua, menjadi penentu utama dalam mempertahankan mahasiswa hingga lulus. Mahasiswa yang berhasil memperoleh nilai lebih tinggi dan meluluskan lebih banyak mata kuliah cenderung memiliki kemungkinan lebih besar untuk menyelesaikan pendidikan mereka.

## Rekomendasi Action Items Berdasarkan Analisis Dashboard

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

1. **Evaluasi Bulanan**

   * Review metrik utama
   * Penyesuaian program berdasarkan feedback
   * Pelaporan ke stakeholder

2. **Evaluasi Triwulanan**

   * Analisis mendalam terhadap program
   * Penyesuaian strategi
   * Pelatihan dan pengembangan tim

3. **Evaluasi Tahunan**

   * Review komprehensif
   * Perencanaan strategis
   * Pengembangan program baru

## 📋 Rekomendasi Tambahan

### Teknologi

* Implementasi sistem AI untuk prediksi risiko
* Pengembangan aplikasi mobile untuk monitoring
* Integrasi sistem informasi akademik

### SDM

* Pelatihan khusus untuk dosen dan staf
* Pengembangan tim konseling
* Program pengembangan profesional

### Infrastruktur

* Pengembangan fasilitas belajar
* Peningkatan akses teknologi
* Pengembangan ruang kolaborasi

## 🔐 Akses Metabase

* **Email**: `root@mail.com`
* **Password**: `root123`

---

