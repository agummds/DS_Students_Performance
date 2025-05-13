import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Set page config
st.set_page_config(
    page_title="Student Success Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title and description
st.title("🎓 Student Success Predictor")
st.markdown("""
This application helps predict student success based on various academic and demographic factors.
The prediction will show whether a student is likely to:
- 🎯 Graduate
- 📚 Stay Enrolled
- ⚠️ Dropout

Please fill in the student's information below to get a prediction.
""")

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Load the data
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('data_agum.csv')
        return data
    except Exception as e:
        st.error("Error loading data. Please make sure 'data_agum.csv' exists in the correct location.")
        return None

# Load model and data
model = load_model()
data = load_data()

if model is not None and data is not None:
    # Display sample data with explanation
    with st.expander("📊 View Sample Data"):
        st.dataframe(data.head())
        st.caption("This is a sample of the data used to train the model.")
    
    # Create input fields based on your model's features
    st.subheader("📝 Enter Student Information")
    
    # Create three columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Academic Information")
        marital_status = st.selectbox(
            "Marital Status",
            options=sorted(data['Marital_status'].unique()),
            help="Student's marital status"
        )
        application_mode = st.selectbox(
            "Application Mode",
            options=sorted(data['Application_mode'].unique()),
            help="The method through which the student applied"
        )
        application_order = st.number_input(
            "Application Order",
            min_value=0,
            max_value=10,
            value=1,
            help="Order of application"
        )
        course = st.selectbox(
            "Course",
            options=sorted(data['Course'].unique()),
            help="The course the student is enrolled in"
        )
        daytime_evening_attendance = st.selectbox(
            "Daytime/Evening Attendance",
            options=[0, 1],
            format_func=lambda x: "Daytime" if x == 1 else "Evening",
            help="Whether the student attends daytime or evening classes"
        )
        previous_qualification = st.selectbox(
            "Previous Qualification",
            options=sorted(data['Previous_qualification'].unique()),
            help="Previous qualification type"
        )
        previous_qualification_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            help="Grade from previous qualification"
        )
        nacionality = st.selectbox(
            "Nationality",
            options=sorted(data['Nacionality'].unique()),
            help="Student's nationality"
        )
        
    with col2:
        st.markdown("### Personal Information")
        mothers_qualification = st.selectbox(
            "Mother's Qualification",
            options=sorted(data['Mothers_qualification'].unique()),
            help="Mother's highest qualification"
        )
        fathers_qualification = st.selectbox(
            "Father's Qualification",
            options=sorted(data['Fathers_qualification'].unique()),
            help="Father's highest qualification"
        )
        mothers_occupation = st.selectbox(
            "Mother's Occupation",
            options=sorted(data['Mothers_occupation'].unique()),
            help="Mother's occupation"
        )
        fathers_occupation = st.selectbox(
            "Father's Occupation",
            options=sorted(data['Fathers_occupation'].unique()),
            help="Father's occupation"
        )
        admission_grade = st.number_input(
            "Admission Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            help="Grade at admission"
        )
        displaced = st.selectbox(
            "Displaced",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student is displaced"
        )
        educational_special_needs = st.selectbox(
            "Educational Special Needs",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student has special educational needs"
        )
        debtor = st.selectbox(
            "Debtor",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student is a debtor"
        )
        tuition_fees_up_to_date = st.selectbox(
            "Tuition Fees Up to Date",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student's tuition fees are up to date"
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
        international = st.selectbox(
            "International",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student is international"
        )
        
    with col3:
        st.markdown("### Academic Performance")
        curricular_units_1st_sem_enrolled = st.number_input(
            "1st Semester Units Enrolled",
            min_value=0,
            max_value=20,
            value=6,
            help="Number of units enrolled in first semester"
        )
        curricular_units_1st_sem_evaluations = st.number_input(
            "1st Semester Units Evaluated",
            min_value=0,
            max_value=20,
            value=6,
            help="Number of units evaluated in first semester"
        )
        curricular_units_1st_sem_approved = st.number_input(
            "1st Semester Units Approved",
            min_value=0,
            max_value=20,
            value=6,
            help="Number of units approved in first semester"
        )
        curricular_units_1st_sem_grade = st.number_input(
            "1st Semester Average Grade",
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            help="Average grade in first semester"
        )
        curricular_units_1st_sem_without_evaluations = st.number_input(
            "1st Semester Units Without Evaluations",
            min_value=0,
            max_value=20,
            value=0,
            help="Number of units without evaluations in first semester"
        )
        curricular_units_2nd_sem_enrolled = st.number_input(
            "2nd Semester Units Enrolled",
            min_value=0,
            max_value=20,
            value=6,
            help="Number of units enrolled in second semester"
        )
        curricular_units_2nd_sem_evaluations = st.number_input(
            "2nd Semester Units Evaluated",
            min_value=0,
            max_value=20,
            value=6,
            help="Number of units evaluated in second semester"
        )
        curricular_units_2nd_sem_approved = st.number_input(
            "2nd Semester Units Approved",
            min_value=0,
            max_value=20,
            value=6,
            help="Number of units approved in second semester"
        )
        curricular_units_2nd_sem_grade = st.number_input(
            "2nd Semester Average Grade",
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            help="Average grade in second semester"
        )
        curricular_units_2nd_sem_without_evaluations = st.number_input(
            "2nd Semester Units Without Evaluations",
            min_value=0,
            max_value=20,
            value=0,
            help="Number of units without evaluations in second semester"
        )
        unemployment_rate = st.number_input(
            "Unemployment Rate",
            min_value=0.0,
            max_value=100.0,
            value=10.0,
            help="Current unemployment rate"
        )
        inflation_rate = st.number_input(
            "Inflation Rate",
            min_value=-100.0,
            max_value=100.0,
            value=0.0,
            help="Current inflation rate"
        )
        gdp = st.number_input(
            "GDP",
            min_value=0.0,
            max_value=100000.0,
            value=1000.0,
            help="Current GDP"
        )
    
    # Add prediction button
    if st.button("🔮 Predict Student Success", type="primary"):
        with st.spinner("Analyzing student data..."):
            # Prepare input data
            input_data = pd.DataFrame([[
                marital_status, application_mode, application_order, course,
                daytime_evening_attendance, previous_qualification,
                previous_qualification_grade, nacionality, mothers_qualification,
                fathers_qualification, mothers_occupation, fathers_occupation,
                admission_grade, displaced, educational_special_needs, debtor,
                tuition_fees_up_to_date, gender, scholarship_holder,
                age_at_enrollment, international, curricular_units_1st_sem_enrolled,
                curricular_units_1st_sem_evaluations, curricular_units_1st_sem_approved,
                curricular_units_1st_sem_grade, curricular_units_1st_sem_without_evaluations,
                curricular_units_2nd_sem_enrolled, curricular_units_2nd_sem_evaluations,
                curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade,
                curricular_units_2nd_sem_without_evaluations, unemployment_rate,
                inflation_rate, gdp
            ]], columns=[
                'Marital_status', 'Application_mode', 'Application_order', 'Course',
                'Daytime_evening_attendance', 'Previous_qualification',
                'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
                'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
                'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
                'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
                'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_enrolled',
                'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
                'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
                'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations',
                'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
                'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate',
                'Inflation_rate', 'GDP'
            ])
            
            # Calculate additional features
            input_data['Total_Approved_Units'] = input_data['Curricular_units_1st_sem_approved'] + input_data['Curricular_units_2nd_sem_approved']
            input_data['Average_Grade'] = input_data[['Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_grade']].mean(axis=1)
            input_data['Engagement_Score'] = (
                input_data['Curricular_units_1st_sem_evaluations'] + input_data['Curricular_units_2nd_sem_evaluations']
            ) / (
                input_data['Curricular_units_1st_sem_enrolled'] + input_data['Curricular_units_2nd_sem_enrolled'] + 1e-5
            )
            input_data['Dropout_Risk_Score'] = (
                input_data['Debtor'] * 2 +
                (1 - input_data['Tuition_fees_up_to_date']) +
                (20 - input_data['Admission_grade']) / 20
            )
            
            # Create a template DataFrame with all possible features
            template_data = pd.get_dummies(data, columns=[
                'Marital_status', 'Application_mode', 'Course', 'Daytime_evening_attendance',
                'Previous_qualification', 'Nacionality', 'Mothers_qualification',
                'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
                'Displaced', 'Educational_special_needs', 'Debtor',
                'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
                'International'
            ])
            
            # Get all possible feature names from the template
            all_features = template_data.columns.tolist()
            
            # One-hot encode the input data
            encoded_data = pd.get_dummies(input_data, columns=[
                'Marital_status', 'Application_mode', 'Course', 'Daytime_evening_attendance',
                'Previous_qualification', 'Nacionality', 'Mothers_qualification',
                'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
                'Displaced', 'Educational_special_needs', 'Debtor',
                'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
                'International'
            ])
            
            # Print feature information for debugging
            st.write("Template features:", len(template_data.columns))
            st.write("Template feature names:", template_data.columns.tolist())
            st.write("Input features before alignment:", len(encoded_data.columns))
            st.write("Input feature names before alignment:", encoded_data.columns.tolist())
            
            # Ensure all columns from template exist in encoded data
            for col in all_features:
                if col not in encoded_data.columns:
                    encoded_data[col] = 0
            
            # Reorder columns to match template
            encoded_data = encoded_data[all_features]
            
            # Print final feature information
            st.write("Final input features:", len(encoded_data.columns))
            st.write("Final feature names:", encoded_data.columns.tolist())
            
            # Make prediction
            prediction = model.predict(encoded_data)
            
            # Display prediction with more details
            st.subheader("🎯 Prediction Result")
            
            # Create a container for the prediction
            prediction_container = st.container()
            
            with prediction_container:
                if prediction[0] == 0:
                    st.error("⚠️ The student is predicted to Dropout")
                    st.info("""
                    **Recommendations:**
                    - Consider additional academic support
                    - Review course load and difficulty
                    - Check for personal or financial issues
                    """)
                elif prediction[0] == 1:
                    st.warning("📚 The student is predicted to be Enrolled")
                    st.info("""
                    **Recommendations:**
                    - Continue current academic support
                    - Monitor progress regularly
                    - Maintain good study habits
                    """)
                else:
                    st.success("🎓 The student is predicted to Graduate")
                    st.info("""
                    **Recommendations:**
                    - Continue excellent performance
                    - Consider advanced courses
                    - Plan for post-graduation
                    """)
                
                # Add a download button for the prediction
                st.download_button(
                    label="📥 Download Prediction Report",
                    data=f"""
                    Student Success Prediction Report
                    ===============================
                    
                    Academic Information:
                    - Marital Status: {marital_status}
                    - Application Mode: {application_mode}
                    - Application Order: {application_order}
                    - Course: {course}
                    - Daytime/Evening Attendance: {"Daytime" if daytime_evening_attendance == 1 else "Evening"}
                    - Previous Qualification: {previous_qualification}
                    - Previous Qualification Grade: {previous_qualification_grade}
                    - Nationality: {nacionality}
                    
                    Personal Information:
                    - Mother's Qualification: {mothers_qualification}
                    - Father's Qualification: {fathers_qualification}
                    - Mother's Occupation: {mothers_occupation}
                    - Father's Occupation: {fathers_occupation}
                    - Admission Grade: {admission_grade}
                    - Displaced: {"Yes" if displaced == 1 else "No"}
                    - Educational Special Needs: {"Yes" if educational_special_needs == 1 else "No"}
                    - Debtor: {"Yes" if debtor == 1 else "No"}
                    - Tuition Fees Up to Date: {"Yes" if tuition_fees_up_to_date == 1 else "No"}
                    - Gender: {"Male" if gender == 1 else "Female"}
                    - Scholarship Holder: {"Yes" if scholarship_holder == 1 else "No"}
                    - Age at Enrollment: {age_at_enrollment}
                    - International: {"Yes" if international == 1 else "No"}
                    
                    Academic Performance:
                    First Semester:
                    - Units Enrolled: {curricular_units_1st_sem_enrolled}
                    - Units Evaluated: {curricular_units_1st_sem_evaluations}
                    - Units Approved: {curricular_units_1st_sem_approved}
                    - Average Grade: {curricular_units_1st_sem_grade}
                    - Units Without Evaluations: {curricular_units_1st_sem_without_evaluations}
                    
                    Second Semester:
                    - Units Enrolled: {curricular_units_2nd_sem_enrolled}
                    - Units Evaluated: {curricular_units_2nd_sem_evaluations}
                    - Units Approved: {curricular_units_2nd_sem_approved}
                    - Average Grade: {curricular_units_2nd_sem_grade}
                    - Units Without Evaluations: {curricular_units_2nd_sem_without_evaluations}
                    
                    Economic Indicators:
                    - Unemployment Rate: {unemployment_rate}
                    - Inflation Rate: {inflation_rate}
                    - GDP: {gdp}
                    
                    Calculated Metrics:
                    - Total Approved Units: {input_data['Total_Approved_Units'].iloc[0]}
                    - Average Grade: {input_data['Average_Grade'].iloc[0]:.2f}
                    - Engagement Score: {input_data['Engagement_Score'].iloc[0]:.2f}
                    - Dropout Risk Score: {input_data['Dropout_Risk_Score'].iloc[0]:.2f}
                    
                    Prediction: {"Graduate" if prediction[0] == 2 else "Enrolled" if prediction[0] == 1 else "Dropout"}
                    """,
                    file_name="student_prediction_report.txt",
                    mime="text/plain"
                )

else:
    st.error("""
    ❌ Required files are missing or cannot be loaded.
    
    Please make sure you have:
    1. 'model.pkl' - The trained model file
    2. 'data_agum.csv' - The dataset file
    
    All files should be in the same directory as this application.
    """) 