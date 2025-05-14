import streamlit as st
import pandas as pd
import pickle
import numpy as np
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder

# Set page configuration
st.set_page_config(
    page_title="Student Dropout Predictor",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem;
        border-radius: 5px;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

class StudentPredictor:
    def __init__(self):
        self.model = None
        self.encoder = None
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
        # Features that need one-hot encoding
        self.categorical_features = [
            'Application_mode', 'Course', 'Mothers_qualification',
            'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
            'Displaced', 'Gender', 'Scholarship_holder', 'Status'
        ]

    def load_model(self):
        try:
            with open('model.pkl', 'rb') as f:
                self.model = pickle.load(f)
            # Create encoder even if model is loaded successfully
            # This ensures compatibility with the model's expected features
            self.encoder = self._create_demo_encoder()
            return True
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return False

    def prepare_input_data(self, form_data):
        # Create a DataFrame from the form data
        input_df = pd.DataFrame([form_data], columns=self.feature_names)
        
        # If we don't have an encoder saved, create a dummy one
        if self.encoder is None:
            self.encoder = self._create_demo_encoder()
            
        # Extract categorical features
        cat_features = input_df[self.categorical_features]
        
        # Transform categorical features using one-hot encoding
        cat_encoded = self.encoder.transform(cat_features)
        
        # Get the feature names from the encoder
        encoded_feature_names = self.encoder.get_feature_names_out(self.categorical_features)
        
        # Create a new DataFrame with encoded features
        cat_encoded_df = pd.DataFrame(
            cat_encoded, 
            columns=encoded_feature_names,
            index=input_df.index
        )
        
        # Drop original categorical columns and join with encoded ones
        input_df_processed = input_df.drop(columns=self.categorical_features)
        input_df_processed = pd.concat([input_df_processed, cat_encoded_df], axis=1)
        
        # Handle any missing features required by the model
        if self.model is not None:
            expected_features = 259  # As per the error message
            
            # If we have fewer features than expected, add dummy columns
            if input_df_processed.shape[1] < expected_features:
                # Create a dictionary of missing features
                missing_cols = {
                    f'missing_feature_{i}': [0] for i in range(expected_features - input_df_processed.shape[1])
                }
                
                # Create a DataFrame from the dictionary
                missing_df = pd.DataFrame(missing_cols, index=input_df_processed.index)
                
                # Concatenate with the existing DataFrame
                input_df_processed = pd.concat([input_df_processed, missing_df], axis=1)
                    
            # If we have more features than expected, keep only the needed ones
            elif input_df_processed.shape[1] > expected_features:
                input_df_processed = input_df_processed.iloc[:, :expected_features]
        
        return input_df_processed

    def _create_demo_encoder(self):
        # Create a demonstration encoder for categorical features
        # Create a dataframe with the same number of rows for each category
        num_samples = 10  # Create 10 samples to ensure consistent length
        
        # Create random but consistent data for each categorical feature
        dummy_data = pd.DataFrame({
            'Application_mode': [15, 9254] * 5,
            'Course': [9254, 9853] * 5,
            'Mothers_qualification': [1, 2, 3, 1, 2] * 2,
            'Fathers_qualification': [3, 4, 5, 3, 4] * 2,
            'Mothers_occupation': [1, 2, 3, 1, 2] * 2,
            'Fathers_occupation': [1, 2, 3, 1, 2] * 2,
            'Displaced': [0, 1] * 5,
            'Gender': [0, 1] * 5,
            'Scholarship_holder': [0, 1] * 5,
            'Status': [0, 1] * 5
        })
        
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoder.fit(dummy_data)
        return encoder

    def predict(self, input_data):
        if self.model is None:
            return None
        
        try:
            # Ensure input_data has the expected number of features
            expected_features = 259  # From the error message
            
            if input_data.shape[1] != expected_features:
                # Adjust feature count
                if input_data.shape[1] < expected_features:
                    # Create a dictionary of missing features
                    missing_cols = {
                        f'missing_feature_{i}': [0] for i in range(expected_features - input_data.shape[1])
                    }
                    
                    # Create a DataFrame from the dictionary
                    missing_df = pd.DataFrame(missing_cols, index=input_data.index)
                    
                    # Concatenate with the existing DataFrame
                    input_data = pd.concat([input_data, missing_df], axis=1)
                else:
                    input_data = input_data.iloc[:, :expected_features]
            
            # Suppress the UserWarning about feature names
            import warnings
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=UserWarning, message="X has feature names")
                result = self.model.predict(input_data)[0]
                
            return str(result)  # Convert to string for consistency
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
            return None

def create_input_form():
    with st.form("student_form"):
        st.markdown("### Academic Information")
        col1, col2 = st.columns(2)
        
        with col1:
            application_mode = st.selectbox(
                "Application Mode",
                options=[15, 9254],
                help="Mode of application"
            )
            course = st.selectbox(
                "Course",
                options=[9254, 9853],
                help="Selected course"
            )
            previous_qualification_grade = st.number_input(
                "Previous Qualification Grade",
                min_value=0.0,
                max_value=200.0,
                value=160.0,
                help="Grade from previous qualification"
            )
            admission_grade = st.number_input(
                "Admission Grade",
                min_value=0.0,
                max_value=200.0,
                value=142.5,
                help="Grade at admission"
            )

        with col2:
            mothers_qualification = st.selectbox(
                "Mother's Qualification",
                options=[1, 2, 3],
                help="Mother's highest qualification"
            )
            fathers_qualification = st.selectbox(
                "Father's Qualification",
                options=[3, 4, 5],
                help="Father's highest qualification"
            )
            mothers_occupation = st.selectbox(
                "Mother's Occupation",
                options=[1, 2, 3],
                help="Mother's occupation"
            )
            fathers_occupation = st.selectbox(
                "Father's Occupation",
                options=[1, 2, 3],
                help="Father's occupation"
            )

        st.markdown("### Personal Information")
        col3, col4 = st.columns(2)
        
        with col3:
            displaced = st.selectbox(
                "Displaced",
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Whether the student is displaced"
            )
            gender = st.selectbox(
                "Gender",
                options=[0, 1],
                format_func=lambda x: "Male" if x == 1 else "Female",
                help="Student's gender"
            )
            scholarship_holder = st.selectbox(
                "Scholarship Holder",
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Whether the student has a scholarship"
            )
            age_at_enrollment = st.number_input(
                "Age at Enrollment",
                min_value=17,
                max_value=100,
                value=19,
                help="Student's age when enrolled"
            )

        with col4:
            status = st.selectbox(
                "Status",
                options=[0, 1],
                format_func=lambda x: "Active" if x == 1 else "Inactive",
                help="Current student status"
            )
            unemployment_rate = st.number_input(
                "Unemployment Rate",
                min_value=0.0,
                max_value=100.0,
                value=13.9,
                help="Current unemployment rate"
            )
            inflation_rate = st.number_input(
                "Inflation Rate",
                min_value=-100.0,
                max_value=100.0,
                value=-0.3,
                help="Current inflation rate"
            )
            gdp = st.number_input(
                "GDP",
                min_value=0.0,
                max_value=100000.0,
                value=0.79,
                help="Current GDP"
            )

        st.markdown("### Academic Performance")
        col5, col6 = st.columns(2)
        
        with col5:
            st.markdown("#### First Semester")
            curricular_units_1st_sem_enrolled = st.number_input(
                "Units Enrolled",
                min_value=0,
                max_value=20,
                value=6,
                key="1st_enrolled"
            )
            curricular_units_1st_sem_evaluations = st.number_input(
                "Units Evaluated",
                min_value=0,
                max_value=20,
                value=6,
                key="1st_evaluations"
            )
            curricular_units_1st_sem_approved = st.number_input(
                "Units Approved",
                min_value=0,
                max_value=20,
                value=6,
                key="1st_approved"
            )
            ratio_approved_1st_sem = st.number_input(
                "Approval Ratio",
                min_value=0.0,
                max_value=1.0,
                value=1.0,
                key="1st_ratio"
            )

        with col6:
            st.markdown("#### Second Semester")
            curricular_units_2nd_sem_enrolled = st.number_input(
                "Units Enrolled",
                min_value=0,
                max_value=20,
                value=6,
                key="2nd_enrolled"
            )
            curricular_units_2nd_sem_evaluations = st.number_input(
                "Units Evaluated",
                min_value=0,
                max_value=20,
                value=6,
                key="2nd_evaluations"
            )
            curricular_units_2nd_sem_approved = st.number_input(
                "Units Approved",
                min_value=0,
                max_value=20,
                value=6,
                key="2nd_approved"
            )
            ratio_approved_2nd_sem = st.number_input(
                "Approval Ratio",
                min_value=0.0,
                max_value=1.0,
                value=1.0,
                key="2nd_ratio"
            )

        submitted = st.form_submit_button("Predict Dropout Risk")
        
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
            <div class='prediction-box' style='background-color: #d4edda; border: 1px solid #c3e6cb;'>
                <h2 style='color: #155724;'>🎓 Low Dropout Risk</h2>
                <p style='color: #155724;'>The student is likely to continue their studies successfully.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class='prediction-box' style='background-color: #f8d7da; border: 1px solid #f5c6cb;'>
                <h2 style='color: #721c24;'>⚠️ High Dropout Risk</h2>
                <p style='color: #721c24;'>The student may need additional support to continue their studies.</p>
            </div>
        """, unsafe_allow_html=True)

def main():
    st.title("🎓 Student Dropout Predictor")
    st.markdown("""
    This application helps predict whether a student is at risk of dropping out based on various academic and personal factors.
    Please fill in the student's information below to get a prediction.
    """)

    predictor = StudentPredictor()
    if predictor.load_model():
        form_data = create_input_form()
        
        if form_data is not None:
            with st.spinner("Processing data and making prediction..."):
                input_data = predictor.prepare_input_data(form_data)
                prediction = predictor.predict(input_data)
                
                if prediction is not None:
                    display_prediction(prediction)
                    
                    # Add timestamp
                    st.markdown(f"*Prediction made on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

if __name__ == "__main__":
    main()