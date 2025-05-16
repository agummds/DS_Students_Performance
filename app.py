import streamlit as st
import pandas as pd
import pickle
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Prediktor Risiko Dropout Siswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
        background-color: #f0f2f6;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background-color: #4a90e2;
        color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #357abd;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Prediction box styling */
    .prediction-box {
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        background-color: #ffffff;
    }
    
    /* Section headers */
    .section-header {
        color: #2c3e50;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.2rem;
        padding-bottom: 0.8rem;
        border-bottom: 3px solid #4a90e2;
    }
    
    /* Info text */
    .info-text {
        color: #2c3e50;
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
        line-height: 1.5;
    }
    
    /* Form elements */
    .stSelectbox, .stNumberInput {
        margin-bottom: 1.2rem;
    }
    
    /* Input fields */
    .stSelectbox > div > div {
        background-color: #ffffff;
        border: 2px solid #4a90e2;
        border-radius: 6px;
    }
    
    .stNumberInput > div > div > input {
        background-color: #ffffff;
        border: 2px solid #4a90e2;
        border-radius: 6px;
        color: #2c3e50;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #2c3e50;
        color: #ffffff;
    }
    
    .sidebar .sidebar-content {
        background-color: #2c3e50;
    }
    
    /* Card styling */
    .card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Title styling */
    h1 {
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    /* Help text styling */
    .help-text {
        color: #7f8c8d;
        font-size: 0.9rem;
        font-style: italic;
    }
    
    /* Success message styling */
    .success-message {
        background-color: #e8f5e9;
        border: 2px solid #2e7d32;
        color: #1b5e20;
    }
    
    /* Warning message styling */
    .warning-message {
        background-color: #fff3e0;
        border: 2px solid #ef6c00;
        color: #e65100;
    }

    /* Fix for selectbox text color */
    .stSelectbox > div > div > div {
        color: #2c3e50 !important;
    }

    /* Fix for number input text color */
    .stNumberInput > div > div > input {
        color: #2c3e50 !important;
    }

    /* Fix for sidebar text color */
    .sidebar .sidebar-content .stMarkdown {
        color: #ffffff !important;
    }

    /* Fix for form labels */
    .stForm label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }

    /* Fix for selectbox options */
    .stSelectbox [data-baseweb="select"] {
        color: #2c3e50 !important;
    }

    /* Fix for number input labels */
    .stNumberInput label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }

    /* Fix for sidebar headers */
    .sidebar h1, .sidebar h2, .sidebar h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* Fix for sidebar paragraphs */
    .sidebar p {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Fix for sidebar lists */
    .sidebar ul, .sidebar ol {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Fix for form section headers */
    .section-header {
        color: #2c3e50 !important;
        font-weight: 700 !important;
    }

    /* Fix for form info text */
    .info-text {
        color: #2c3e50 !important;
        font-weight: 500 !important;
    }

    /* Fix for selectbox dropdown text */
    .stSelectbox [data-baseweb="popover"] {
        color: #2c3e50 !important;
    }

    /* Fix for number input value text */
    .stNumberInput [data-baseweb="input"] {
        color: #2c3e50 !important;
    }

    /* Fix for selectbox dropdown background */
    .stSelectbox [data-baseweb="popover"] {
        background-color: #ffffff !important;
    }

    /* Fix for selectbox option hover */
    .stSelectbox [data-baseweb="option"]:hover {
        background-color: #e8eaf6 !important;
    }

    /* Fix for selectbox selected option */
    .stSelectbox [data-baseweb="option"][aria-selected="true"] {
        background-color: #c5cae9 !important;
        color: #2c3e50 !important;
    }

    /* Fix for number input focus */
    .stNumberInput [data-baseweb="input"]:focus {
        border-color: #4a90e2 !important;
        box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2) !important;
    }

    /* Fix for selectbox focus */
    .stSelectbox [data-baseweb="select"]:focus {
        border-color: #4a90e2 !important;
        box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2) !important;
    }

    /* Main background */
    .stApp {
        background-color: #f0f2f6;
    }

    /* Form background */
    .stForm {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Section background */
    .section-background {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Semester section styling */
    .semester-section {
        background-color: #e8f0fe;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #4a90e2;
    }

    .semester-section h4 {
        color: #2c3e50;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #4a90e2;
    }

    /* Update the semester headers in the form */
    .stMarkdown h4 {
        background-color: #e8f0fe;
        padding: 1rem;
        border-radius: 8px;
        color: #2c3e50 !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        border: 1px solid #4a90e2;
    }

    /* Popup styling */
    .popup-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        animation: fadeIn 0.3s ease-in-out;
    }

    .popup-content {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        max-width: 600px;
        width: 90%;
        animation: slideIn 0.3s ease-in-out;
    }

    .popup-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 3px solid;
    }

    .popup-title.success {
        color: #1b5e20;
        border-color: #2e7d32;
    }

    .popup-title.warning {
        color: #b71c1c;
        border-color: #c62828;
    }

    .popup-message {
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        line-height: 1.6;
    }

    .popup-message.success {
        color: #1b5e20;
    }

    .popup-message.warning {
        color: #b71c1c;
    }

    .popup-actions {
        text-align: center;
        margin-top: 2rem;
    }

    .popup-button {
        padding: 1rem 2.5rem;
        border-radius: 8px;
        border: none;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .popup-button.success {
        background-color: #2e7d32;
        color: white;
    }

    .popup-button.warning {
        background-color: #c62828;
        color: white;
    }

    .popup-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .popup-list {
        text-align: left;
        margin: 1rem 0;
        padding-left: 2rem;
    }

    .popup-list li {
        margin-bottom: 0.8rem;
        color: #b71c1c;
        font-size: 1.1rem;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <h2 style='color: white; margin-bottom: 1rem;'>Prediktor Risiko Dropout</h2>
            <p style='color: #ecf0f1; margin-bottom: 2rem;'>
                Alat untuk pendidik mengidentifikasi siswa yang berisiko dropout
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #34495e; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;'>
            <h3 style='color: white; margin-bottom: 0.5rem;'>Tentang Alat Ini</h3>
            <p style='color: #ecf0f1; font-size: 0.9rem;'>
                Alat ini membantu pendidik mengidentifikasi siswa yang mungkin membutuhkan dukungan tambahan untuk melanjutkan studi mereka dengan sukses.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #34495e; padding: 1rem; border-radius: 8px;'>
            <h3 style='color: white; margin-bottom: 0.5rem;'>Cara Penggunaan</h3>
            <ol style='color: #ecf0f1; font-size: 0.9rem; padding-left: 1.2rem;'>
                <li>Masukkan informasi akademik siswa</li>
                <li>Isi latar belakang pribadi mereka</li>
                <li>Tambahkan metrik kinerja mereka</li>
                <li>Klik 'Prediksi' untuk mendapatkan hasil</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

# Add this at the beginning of the file, after the imports
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

class StudentPredictor:
    def __init__(self):
        self.model = None
        self.feature_names = [
            'Application_mode', 'Course', 'Previous_qualification_grade',
            'Mothers_qualification', 'Fathers_qualification',
            'Mothers_occupation', 'Fathers_occupation', 'Admission_grade',
            'Displaced', 'Gender', 'Scholarship_holder', 'Age_at_enrollment',
            'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations',
            'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_enrolled',
            'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
            'Unemployment_rate', 'Inflation_rate', 'GDP', 'Status',
            'Ratio_approved_1st_sem', 'Ratio_approved_2nd_sem'
        ]
        # Features that need encoding
        self.categorical_features = [
            'Application_mode', 'Course', 'Mothers_qualification',
            'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
            'Displaced', 'Gender', 'Scholarship_holder', 'Status'
        ]

    def load_model(self):
        try:
            with open('model.pkl', 'rb') as f:
                self.model = pickle.load(f)
            return True
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return False

    def prepare_input_data(self, form_data):
        # Create a DataFrame from the form data
        input_df = pd.DataFrame([form_data], columns=self.feature_names)
        
        # Define the expected categories for each feature
        expected_categories = {
            'Application_mode': [15, 9254],
            'Course': [9254, 9853],
            'Mothers_qualification': [1, 2, 3],
            'Fathers_qualification': [3, 4, 5],
            'Mothers_occupation': [1, 2, 3],
            'Fathers_occupation': [1, 2, 3],
            'Displaced': [0, 1],
            'Gender': [0, 1],
            'Scholarship_holder': [0, 1],
            'Status': [0, 1]
        }
        
        # Create binary columns for categorical features
        for feature in self.categorical_features:
            # Create binary columns for each expected category
            for value in expected_categories[feature]:
                col_name = f"{feature}_{value}"
                input_df[col_name] = (input_df[feature] == value).astype(int)
            
            # Drop the original categorical column
            input_df = input_df.drop(columns=[feature])
        
        # Ensure we have exactly 259 features
        expected_features = 259
        current_features = input_df.shape[1]
        
        if current_features < expected_features:
            # Add missing features with zeros
            missing_features = expected_features - current_features
            for i in range(missing_features):
                input_df[f'missing_feature_{i}'] = 0
        elif current_features > expected_features:
            # Keep only the first 259 features
            input_df = input_df.iloc[:, :expected_features]
        
        return input_df

    def predict(self, input_data):
        if self.model is None:
            return None
        
        try:
            # Ensure input_data has exactly 259 features
            if input_data.shape[1] != 259:
                st.error(f"Expected 259 features but got {input_data.shape[1]}")
                return None
                
            # Suppress any warnings
            import warnings
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore")
                result = self.model.predict(input_data)[0]
                
            return str(result)  # Convert to string for consistency
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
            return None

def create_input_form():
    with st.form("student_form"):
        st.markdown('<div class="section-header">Informasi Akademik</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-text">Silakan isi detail akademik siswa</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            application_mode = st.selectbox(
                "Mode Pendaftaran",
                options=[15, 9254],
                help="Mode pendaftaran (15: Reguler, 9254: Khusus)",
                format_func=lambda x: "Reguler" if x == 15 else "Khusus"
            )
            course = st.selectbox(
                "Program Studi",
                options=[9254, 9853],
                help="Program studi yang dipilih (9254: Ilmu Komputer, 9853: Sistem Informasi)",
                format_func=lambda x: "Ilmu Komputer" if x == 9254 else "Sistem Informasi"
            )
            previous_qualification_grade = st.number_input(
                "Nilai Kualifikasi Sebelumnya",
                min_value=0.0,
                max_value=200.0,
                value=160.0,
                help="Nilai dari kualifikasi sebelumnya (0-200)"
            )
            admission_grade = st.number_input(
                "Nilai Penerimaan",
                min_value=0.0,
                max_value=200.0,
                value=142.5,
                help="Nilai saat diterima (0-200)"
            )

        with col2:
            mothers_qualification = st.selectbox(
                "Kualifikasi Ibu",
                options=[1, 2, 3],
                help="Kualifikasi tertinggi ibu (1: Dasar, 2: Menengah, 3: Tinggi)",
                format_func=lambda x: {1: "Dasar", 2: "Menengah", 3: "Tinggi"}[x]
            )
            fathers_qualification = st.selectbox(
                "Kualifikasi Ayah",
                options=[3, 4, 5],
                help="Kualifikasi tertinggi ayah (3: Tinggi, 4: Sarjana, 5: Magister)",
                format_func=lambda x: {3: "Tinggi", 4: "Sarjana", 5: "Magister"}[x]
            )
            mothers_occupation = st.selectbox(
                "Pekerjaan Ibu",
                options=[1, 2, 3],
                help="Pekerjaan ibu (1: Pelajar, 2: Karyawan, 3: Wiraswasta)",
                format_func=lambda x: {1: "Pelajar", 2: "Karyawan", 3: "Wiraswasta"}[x]
            )
            fathers_occupation = st.selectbox(
                "Pekerjaan Ayah",
                options=[1, 2, 3],
                help="Pekerjaan ayah (1: Pelajar, 2: Karyawan, 3: Wiraswasta)",
                format_func=lambda x: {1: "Pelajar", 2: "Karyawan", 3: "Wiraswasta"}[x]
            )

        st.markdown('<div class="section-header">Informasi Pribadi</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-text">Silakan isi detail pribadi siswa</div>', unsafe_allow_html=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            displaced = st.selectbox(
                "Tergeser",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Apakah siswa tergeser dari rumah mereka"
            )
            gender = st.selectbox(
                "Jenis Kelamin",
                options=[0, 1],
                format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan",
                help="Jenis kelamin siswa"
            )
            scholarship_holder = st.selectbox(
                "Penerima Beasiswa",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
                help="Apakah siswa menerima beasiswa"
            )
            age_at_enrollment = st.number_input(
                "Usia Saat Mendaftar",
                min_value=17,
                max_value=100,
                value=19,
                help="Usia siswa saat mendaftar"
            )

        with col4:
            status = st.selectbox(
                "Status",
                options=[0, 1],
                format_func=lambda x: "Aktif" if x == 1 else "Tidak Aktif",
                help="Status siswa saat ini"
            )
            unemployment_rate = st.number_input(
                "Tingkat Pengangguran (%)",
                min_value=0.0,
                max_value=100.0,
                value=13.9,
                help="Tingkat pengangguran saat ini dalam persentase"
            )
            inflation_rate = st.number_input(
                "Tingkat Inflasi (%)",
                min_value=-100.0,
                max_value=100.0,
                value=-0.3,
                help="Tingkat inflasi saat ini dalam persentase"
            )
            gdp = st.number_input(
                "PDB (dalam jutaan)",
                min_value=0.0,
                max_value=100000.0,
                value=0.79,
                help="PDB saat ini dalam jutaan"
            )

        st.markdown('<div class="section-header">Kinerja Akademik</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-text">Silakan isi detail kinerja akademik siswa</div>', unsafe_allow_html=True)
        
        col5, col6 = st.columns(2)
        
        with col5:
            st.markdown('<div class="semester-section"><h4>Semester Pertama</h4></div>', unsafe_allow_html=True)
            curricular_units_1st_sem_enrolled = st.number_input(
                "Unit yang Diambil",
                min_value=0,
                max_value=20,
                value=6,
                key="1st_enrolled",
                help="Jumlah unit kurikuler yang diambil di semester pertama"
            )
            curricular_units_1st_sem_evaluations = st.number_input(
                "Unit yang Dievaluasi",
                min_value=0,
                max_value=20,
                value=6,
                key="1st_evaluations",
                help="Jumlah unit kurikuler yang dievaluasi di semester pertama"
            )
            curricular_units_1st_sem_approved = st.number_input(
                "Unit yang Lulus",
                min_value=0,
                max_value=20,
                value=6,
                key="1st_approved",
                help="Jumlah unit kurikuler yang lulus di semester pertama"
            )
            ratio_approved_1st_sem = st.number_input(
                "Rasio Kelulusan",
                min_value=0.0,
                max_value=1.0,
                value=1.0,
                key="1st_ratio",
                help="Rasio unit yang lulus di semester pertama"
            )

        with col6:
            st.markdown('<div class="semester-section"><h4>Semester Kedua</h4></div>', unsafe_allow_html=True)
            curricular_units_2nd_sem_enrolled = st.number_input(
                "Unit yang Diambil",
                min_value=0,
                max_value=20,
                value=6,
                key="2nd_enrolled",
                help="Jumlah unit kurikuler yang diambil di semester kedua"
            )
            curricular_units_2nd_sem_evaluations = st.number_input(
                "Unit yang Dievaluasi",
                min_value=0,
                max_value=20,
                value=6,
                key="2nd_evaluations",
                help="Jumlah unit kurikuler yang dievaluasi di semester kedua"
            )
            curricular_units_2nd_sem_approved = st.number_input(
                "Unit yang Lulus",
                min_value=0,
                max_value=20,
                value=6,
                key="2nd_approved",
                help="Jumlah unit kurikuler yang lulus di semester kedua"
            )
            ratio_approved_2nd_sem = st.number_input(
                "Rasio Kelulusan",
                min_value=0.0,
                max_value=1.0,
                value=1.0,
                key="2nd_ratio",
                help="Rasio unit yang lulus di semester kedua"
            )

        submitted = st.form_submit_button("Prediksi Risiko Dropout")
        
        if submitted:
            return {
                'Application_mode': application_mode,
                'Course': course,
                'Previous_qualification_grade': previous_qualification_grade,
                'Mothers_qualification': mothers_qualification,
                'Fathers_qualification': fathers_qualification,
                'Mothers_occupation': mothers_occupation,
                'Fathers_occupation': fathers_occupation,
                'Admission_grade': admission_grade,
                'Displaced': displaced,
                'Gender': gender,
                'Scholarship_holder': scholarship_holder,
                'Age_at_enrollment': age_at_enrollment,
                'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
                'Curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
                'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
                'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
                'Curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
                'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
                'Unemployment_rate': unemployment_rate,
                'Inflation_rate': inflation_rate,
                'GDP': gdp,
                'Status': status,
                'Ratio_approved_1st_sem': ratio_approved_1st_sem,
                'Ratio_approved_2nd_sem': ratio_approved_2nd_sem
            }
    return None

def display_prediction(prediction):
    if prediction == '1':
        st.markdown("""
            <div class="popup-overlay" id="prediction-popup">
                <div class="popup-content">
                    <h2 class="popup-title success">🎓 Risiko Dropout Rendah</h2>
                    <p class="popup-message success">
                        Siswa kemungkinan besar akan melanjutkan studi mereka dengan sukses.
                    </p>
                    <p class="popup-message success">
                        Tetap pantau kemajuan mereka dan berikan dukungan sesuai kebutuhan.
                    </p>
                    <div class="popup-actions">
                        <p style="color: #1b5e20; font-size: 1.1rem; margin-top: 1rem;">
                            Silakan refresh browser Anda untuk melakukan prediksi baru
                        </p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="popup-overlay" id="prediction-popup">
                <div class="popup-content">
                    <h2 class="popup-title warning">⚠️ Risiko Dropout Tinggi</h2>
                    <p class="popup-message warning">
                        Siswa mungkin membutuhkan dukungan tambahan untuk melanjutkan studi mereka.
                    </p>
                    <p class="popup-message warning">
                        Tindakan yang Direkomendasikan:
                    </p>
                    <ul class="popup-list">
                        <li>Jadwalkan pertemuan dengan siswa</li>
                        <li>Tinjau kinerja akademik</li>
                        <li>Pertimbangkan layanan dukungan tambahan</li>
                        <li>Pantau kemajuan secara ketat</li>
                    </ul>
                    <div class="popup-actions">
                        <p style="color: #b71c1c; font-size: 1.1rem; margin-top: 1rem;">
                            Silakan refresh browser Anda untuk melakukan prediksi baru
                        </p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 style='color: #2c3e50;'>Prediktor Risiko Dropout Siswa</h1>
            <p style='color: #34495e; font-size: 1.2rem; max-width: 800px; margin: 0 auto;'>
                Alat profesional untuk pendidik mengidentifikasi dan mendukung siswa yang berisiko dropout.
                Silakan masukkan informasi siswa di bawah ini untuk mendapatkan prediksi.
            </p>
        </div>
    """, unsafe_allow_html=True)

    predictor = StudentPredictor()
    if predictor.load_model():
        form_data = create_input_form()
        
        if form_data is not None:
            with st.spinner("Menganalisis data siswa..."):
                input_data = predictor.prepare_input_data(form_data)
                prediction = predictor.predict(input_data)
                
                if prediction is not None:
                    display_prediction(prediction)
                    
                    # Add timestamp
                    st.markdown(f"""
                        <div style='text-align: center; margin-top: 2rem; color: #7f8c8d; font-size: 0.9rem;'>
                            Analisis selesai pada {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
                        </div>
                    """, unsafe_allow_html=True)

# Add this JavaScript to handle the popup
st.markdown("""
    <script>
    function closePopup() {
        document.getElementById('prediction-popup').style.display = 'none';
    }
    </script>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()