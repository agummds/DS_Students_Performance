import streamlit as st
import pandas as pd
import pickle
import numpy as np

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
        with open('modelku.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error("Error loading model. Please make sure 'modelku.pkl' exists in the correct location.")
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
        application_mode = st.selectbox(
            "Application Mode",
            options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 39, 40, 42, 43, 44, 51, 53],
            help="The method through which the student applied"
        )
        course = st.selectbox(
            "Course",
            options=sorted(data['Course'].unique()),
            help="The course the student is enrolled in"
        )
        previous_qualification_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            help="Grade from previous qualification"
        )
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
        
    with col2:
        st.markdown("### Personal Information")
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
        age_at_enrollment = st.number_input(
            "Age at Enrollment",
            min_value=17,
            max_value=100,
            value=19,
            help="Student's age when enrolled"
        )
        gender = st.selectbox(
            "Gender",
            options=[0, 1],
            format_func=lambda x: "Male" if x == 1 else "Female",
            help="Student's gender"
        )
        
    with col3:
        st.markdown("### Academic Performance")
        displaced = st.selectbox(
            "Displaced",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student is displaced"
        )
        scholarship_holder = st.selectbox(
            "Scholarship Holder",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No",
            help="Whether the student has a scholarship"
        )
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
    
    # Add prediction button
    if st.button("🔮 Predict Student Success", type="primary"):
        with st.spinner("Analyzing student data..."):
            # Prepare input data
            input_data = pd.DataFrame([[
                application_mode, course, previous_qualification_grade,
                mothers_qualification, fathers_qualification,
                mothers_occupation, fathers_occupation,
                admission_grade, displaced, gender,
                scholarship_holder, age_at_enrollment,
                curricular_units_1st_sem_enrolled,
                curricular_units_1st_sem_evaluations,
                curricular_units_1st_sem_approved,
                curricular_units_2nd_sem_enrolled,
                curricular_units_2nd_sem_evaluations,
                curricular_units_2nd_sem_approved
            ]], columns=[
                'Application_mode', 'Course', 'Previous_qualification_grade',
                'Mothers_qualification', 'Fathers_qualification',
                'Mothers_occupation', 'Fathers_occupation',
                'Admission_grade', 'Displaced', 'Gender',
                'Scholarship_holder', 'Age_at_enrollment',
                'Curricular_units_1st_sem_enrolled',
                'Curricular_units_1st_sem_evaluations',
                'Curricular_units_1st_sem_approved',
                'Curricular_units_2nd_sem_enrolled',
                'Curricular_units_2nd_sem_evaluations',
                'Curricular_units_2nd_sem_approved'
            ])
            
            # Calculate ratio columns
            input_data['Ratio_approved_1st_sem'] = input_data['Curricular_units_1st_sem_approved'] / input_data['Curricular_units_1st_sem_enrolled'].replace(0, 1)
            input_data['Ratio_approved_2nd_sem'] = input_data['Curricular_units_2nd_sem_approved'] / input_data['Curricular_units_2nd_sem_enrolled'].replace(0, 1)
            
            # Make prediction
            prediction = model.predict(input_data)
            
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
                    - Application Mode: {application_mode}
                    - Course: {course}
                    - Previous Qualification Grade: {previous_qualification_grade}
                    - Mother's Qualification: {mothers_qualification}
                    - Father's Qualification: {fathers_qualification}
                    
                    Personal Information:
                    - Mother's Occupation: {mothers_occupation}
                    - Father's Occupation: {fathers_occupation}
                    - Admission Grade: {admission_grade}
                    - Age at Enrollment: {age_at_enrollment}
                    - Gender: {"Male" if gender == 1 else "Female"}
                    - Displaced: {"Yes" if displaced == 1 else "No"}
                    - Scholarship Holder: {"Yes" if scholarship_holder == 1 else "No"}
                    
                    Academic Performance:
                    First Semester:
                    - Units Enrolled: {curricular_units_1st_sem_enrolled}
                    - Units Evaluated: {curricular_units_1st_sem_evaluations}
                    - Units Approved: {curricular_units_1st_sem_approved}
                    
                    Second Semester:
                    - Units Enrolled: {curricular_units_2nd_sem_enrolled}
                    - Units Evaluated: {curricular_units_2nd_sem_evaluations}
                    - Units Approved: {curricular_units_2nd_sem_approved}
                    
                    Prediction: {"Graduate" if prediction[0] == 2 else "Enrolled" if prediction[0] == 1 else "Dropout"}
                    """,
                    file_name="student_prediction_report.txt",
                    mime="text/plain"
                )

else:
    st.error("""
    ❌ Required files are missing or cannot be loaded.
    
    Please make sure you have:
    1. 'modelku.pkl' - The trained model file
    2. 'data_agum.csv' - The dataset file
    
    Both files should be in the same directory as this application.
    """) 