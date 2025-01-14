import streamlit as st
import pandas as pd
from datetime import datetime
import os
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
st.set_page_config(
page_title="Training Attendance Form",
)
def reset_form():
    st.session_state.form_submitted = True

def fill_form():
    st.session_state.form_submitted = False

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if st.session_state.form_submitted:
    st.write("### Thank you!")
    st.write("Your attendance has been confirmed.")
    st.write("Please close the page.")
    if st.button("FIll Form Again"):
        fill_form()
else:
    st.image('logo.webp', width=None)
    st.title('Training Attendance Form')

    employee_code = st.text_input("Employee Code")
    employee_name = st.text_input("Employee Name")
    designation = st.text_input("Designation")
    department = st.text_input("Department")
    location = st.text_input("Location")
    date = st.date_input("Date", min_value=datetime.today(), format="DD.MM.YYYY")
    timing = st.time_input("Training Start Time", value = None)
    topic = st.selectbox("Topic", ["Quality", "Safety", "Strategy", "Warehouse"])
    trainer_name = st.text_input("Trainer's Name")
    training_mode = st.selectbox("Training Mode", ["Offline", "Online"])
    session_duration = st.selectbox("Session Duration (Minutes)", ["15", "30", "60"])

    if st.button("Confirm Attendance"):
        form_data = {
            'Employee Code' : employee_code,
            'Employee Name': employee_name,
            'Designation': designation,
            'Department': department,
            'Location': location,
            'Date': date.strftime('%m/%d/%Y'),
            'Timing': timing.strftime('%H:%M'),
            'Topic': topic,
            'Trainer\'s Name': trainer_name,
            'Training Mode': training_mode,
            'Session Duration': session_duration
        }

        
        st.success("Attendance has been confirmed!")
        
        st.session_state.form_submitted = True
        reset_form()
        st.rerun()
