# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah lembaga pendidikan tinggi yang berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah meluluskan banyak mahasiswa dengan prestasi gemilang. Namun demikian, masih terdapat sejumlah mahasiswa yang tidak berhasil menyelesaikan studi mereka atau mengalami dropout. Untuk itu, diperlukan sebuah analisis terhadap faktor-faktor yang berkontribusi terhadap tingginya angka dropout, agar Jaya Jaya Institut dapat segera memberikan pendampingan khusus kepada mahasiswa yang berisiko.

## Permasalahan Bisnis
Jaya Jaya Institut saat ini dihadapkan pada tantangan besar terkait tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Fenomena ini tidak hanya berdampak pada reputasi dan stabilitas keuangan institusi, tetapi juga membawa konsekuensi negatif bagi para mahasiswa yang gagal menyelesaikan pendidikan mereka. Dropout yang tinggi berpotensi menurunkan tingkat kepercayaan calon mahasiswa beserta orang tua terhadap mutu pendidikan yang ditawarkan. Beberapa isu bisnis utama yang muncul akibat kondisi ini meliputi:

- Citra Institusi: Tingkat dropout yang signifikan berisiko menodai reputasi Jaya Jaya Institut sebagai lembaga pendidikan yang kredibel dan berkualitas.

- Penurunan Pendapatan: Setiap mahasiswa yang keluar sebelum lulus menyebabkan hilangnya potensi pemasukan dari biaya kuliah dan pendukung lainnya.

- Dampak terhadap Akreditasi: Persentase kelulusan yang rendah dapat memengaruhi penilaian akreditasi institusi secara keseluruhan.

- Ketidakpuasan Para Pemangku Kepentingan: Kepercayaan mahasiswa, orang tua, dan masyarakat luas bisa menurun apabila institusi dianggap kurang efektif dalam membimbing mahasiswa hingga lulus.

# Cakupan Proyek

- Melakukan pengumpulan serta pengolahan data mahasiswa.

- Menganalisis data untuk mengidentifikasi pola serta faktor-faktor yang berkontribusi terhadap dropout mahasiswa.

- Mengembangkan model prediksi menggunakan algoritma Random Forest Classifier.

- Mendesain dashboard interaktif untuk memvisualisasikan hasil analisis dan prediksi.

- Menyusun rekomendasi strategis berdasarkan temuan yang diperoleh.

# Persiapan
Berikut adalah tahapan untuk menyiapkannya:

sumber data: [Student Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Di sini untuk melakukan proses saya sepenuhnya menggunakan Google Colab. Baru kemudian pada bagian visualisasi menggunakan Metadata menggunakan Docker.. Tapi jika ingin menjalankan proyek di local, dapat dilakukan dengan cara berikut:
1. Buka terminal di VSCODE.
2. Jalankan perintah berikut.
```
 conda create --name submissionds python==3.9.21
```
3. Jalankan perintah kedua
```
conda activate submissionds
```

# Business Dashboard

Dashboard bisnis ini dirancang untuk memprediksi kemungkinan seorang mahasiswa mengalami dropout di Jaya Jaya Institut. Prediksi dilakukan menggunakan model machine learning yang telah dilatih sebelumnya dan diintegrasikan ke dalam dashboard untuk memberikan hasil secara real-time berdasarkan data yang dimasukkan.

Dashboard menyediakan berbagai kolom input yang merepresentasikan faktor-faktor yang dapat memengaruhi keputusan mahasiswa untuk berhenti studi, seperti jalur pendaftaran, mata kuliah yang diambil, latar belakang pendidikan, pekerjaan orang tua, serta aspek akademik lainnya. Hasil prediksi ditampilkan secara langsung menggunakan model yang sudah disimpan, sehingga pengguna dapat memperoleh wawasan cepat mengenai risiko dropout setiap mahasiswa.

Dengan adanya dashboard ini, diharapkan pihak Jaya Jaya Institut dapat segera mengidentifikasi mahasiswa yang berisiko dan menerapkan langkah-langkah pencegahan lebih awal guna menekan angka dropout dan meningkatkan keberhasilan studi mahasiswa.

# Menjalankan Sistem Machine Learning

Aplikasi prediksi keberhasilan mahasiswa menggunakan machine learning yang diimplementasikan dengan Streamlit.

### 🚀 Deployment

Aplikasi ini telah di-deploy ke Streamlit Community Cloud dan dapat diakses melalui link berikut:
[Student Success Predictor](https://student-success-predictor.streamlit.app)

### 🛠️ Local Development

### Prerequisites
- Python 3.9 atau lebih baru
- pip (Python package manager)

### Installation

1. Clone repository ini:
```bash
git clone https://github.com/agummds/DS_Students_Performance
cd DS_Students_Performance
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Pastikan file-file berikut ada di direktori yang sama dengan `app.py`:
   - `model.pkl` (model machine learning)
   - `data_agum.csv` (dataset)

4. Jalankan aplikasi secara lokal:
```bash
streamlit run app.py
```

## 📋 Requirements

File `requirements.txt` berisi semua dependensi yang diperlukan:
```
streamlit==1.30.0
pandas==2.1.4
numpy==1.25.2
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.2.2
```

# Conclusion

Fenomena dropout mahasiswa di Jaya Jaya Institut dipengaruhi oleh sejumlah faktor yang dapat dikelompokkan ke dalam lima kategori utama, yakni karakteristik demografis, latar belakang pendidikan, kondisi ekonomi, situasi keluarga dan sosial, serta pencapaian akademik.

Mahasiswa yang berisiko lebih tinggi untuk tidak menyelesaikan studi umumnya memiliki usia yang lebih tua pada saat pendaftaran, termasuk dalam kategori over 23 years old atau mahasiswa transfer, serta mengambil program studi Manajemen kelas malam atau Teknik Informatika. Selain itu, mahasiswa dengan nilai awal masuk (admission grade) yang rendah serta yang tidak memperoleh beasiswa juga menunjukkan kecenderungan yang lebih besar untuk mengalami dropout.

Dari sisi latar belakang keluarga, mahasiswa yang berasal dari lingkungan dengan dukungan pendidikan yang rendah—terutama apabila tingkat pendidikan ayah dan ibu tidak diketahui—juga memiliki potensi lebih tinggi untuk keluar dari institusi sebelum menyelesaikan program studi. Secara umum, mahasiswa yang mengalami dropout menunjukkan performa akademik yang cenderung lebih rendah dibandingkan rekan-rekan mereka yang melanjutkan studi hingga lulus.

# Rekomendasi Action Items Berdasarkan Analisis Dashboard

Berdasarkan analisis dashboard yang telah dibuat, berikut adalah beberapa temuan kunci:

### 1. Distribusi Status Mahasiswa
- Mayoritas mahasiswa masih dalam status "Enrolled"
- Proporsi mahasiswa yang "Dropout" perlu mendapat perhatian khusus
- Tingkat kelulusan ("Graduate") menunjukkan area yang perlu ditingkatkan

### 2. Faktor-faktor yang Mempengaruhi
- Kinerja akademik semester pertama sangat mempengaruhi keberhasilan
- Status beasiswa memiliki korelasi dengan tingkat kelulusan
- Usia saat pendaftaran menunjukkan pola tertentu

### 3. Tren dan Pola
- Ada korelasi antara nilai sebelumnya dengan keberhasilan
- Faktor ekonomi keluarga mempengaruhi kelangsungan studi
- Performa semester pertama menjadi indikator penting

## 🎯 Action Items

### 1. Program Intervensi Dini
- **Target**: Mahasiswa semester pertama
- **Aksi**:
  - Implementasi sistem early warning untuk mengidentifikasi mahasiswa berisiko
  - Program mentoring intensif untuk mahasiswa semester pertama
  - Workshop pengembangan keterampilan belajar
- **Timeline**: Implementasi di awal semester
- **KPI**: Penurunan tingkat dropout di semester pertama

### 2. Penguatan Program Beasiswa
- **Target**: Mahasiswa dengan latar belakang ekonomi menengah ke bawah
- **Aksi**:
  - Evaluasi dan perluasan program beasiswa
  - Penambahan jenis bantuan finansial
  - Program pendampingan untuk penerima beasiswa
- **Timeline**: Evaluasi triwulanan
- **KPI**: Peningkatan tingkat kelulusan penerima beasiswa

### 3. Program Akademik
- **Target**: Semua mahasiswa
- **Aksi**:
  - Pengembangan program remedial untuk mata kuliah kritis
  - Implementasi sistem tutoring peer-to-peer
  - Workshop pengembangan soft skills
- **Timeline**: Berkelanjutan
- **KPI**: Peningkatan nilai rata-rata dan tingkat kelulusan

### 4. Sistem Monitoring dan Evaluasi
- **Target**: Tim akademik dan administrasi
- **Aksi**:
  - Pengembangan dashboard real-time untuk monitoring
  - Implementasi sistem pelaporan berkala
  - Program evaluasi dan penyesuaian berkelanjutan
- **Timeline**: Evaluasi bulanan
- **KPI**: Ketepatan waktu dalam identifikasi masalah

### 5. Program Dukungan Keluarga
- **Target**: Orang tua/wali mahasiswa
- **Aksi**:
  - Program komunikasi rutin dengan orang tua
  - Workshop parenting untuk mendukung mahasiswa
  - Portal informasi untuk orang tua
- **Timeline**: Program semesteran
- **KPI**: Peningkatan keterlibatan orang tua

## 📈 Metrik Sukses

1. **Jangka Pendek (6 Bulan)**:
   - Penurunan 20% tingkat dropout semester pertama
   - Peningkatan 15% tingkat kelulusan
   - Peningkatan 25% partisipasi dalam program mentoring

2. **Jangka Menengah (1 Tahun)**:
   - Penurunan 30% tingkat dropout keseluruhan
   - Peningkatan 25% tingkat kelulusan
   - Peningkatan 40% kepuasan mahasiswa

3. **Jangka Panjang (2 Tahun)**:
   - Penurunan 50% tingkat dropout
   - Peningkatan 40% tingkat kelulusan
   - Peningkatan 60% kepuasan stakeholder

## 🔄 Proses Evaluasi

1. **Evaluasi Bulanan**:
   - Review metrik utama
   - Penyesuaian program berdasarkan feedback
   - Pelaporan ke stakeholder

2. **Evaluasi Triwulanan**:
   - Analisis mendalam terhadap program
   - Penyesuaian strategi
   - Pelatihan dan pengembangan tim

3. **Evaluasi Tahunan**:
   - Review komprehensif
   - Perencanaan strategis
   - Pengembangan program baru

## 📋 Rekomendasi Tambahan

1. **Teknologi**:
   - Implementasi sistem AI untuk prediksi risiko
   - Pengembangan aplikasi mobile untuk monitoring
   - Integrasi sistem informasi akademik

2. **SDM**:
   - Pelatihan khusus untuk dosen dan staf
   - Pengembangan tim konseling
   - Program pengembangan profesional

3. **Infrastruktur**:
   - Pengembangan fasilitas belajar
   - Peningkatan akses teknologi
   - Pengembangan ruang kolaborasi

# Email dan password Metabase
- **Email**: root@mail.com 
- **Password**: root123 

