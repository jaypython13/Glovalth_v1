
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import csv
from streamlit_option_menu import option_menu
from streamlit_dynamic_filters import DynamicFilters
import base64
from pathlib import Path
from PIL import Image

# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon ="	:medical_symbol:", layout= "wide")

img = Image.open('Glovalth_logo.png')
st.image(img)
st.header(":blue[Glovalth Health Tech Care Limited]") 
st.subheader(":green[Empowering Care Homes with Smart Software Solutions for Seamless Operations and Exceptional Resident Care]")

   
video_file = open("Glovalth_product_POC_V1.mp4", "rb")
video_bytes = video_file.read()
col1,col2=st.columns([1,3])   
with col1:
	st.video(video_bytes)
	
#choice1 = option_menu("Main Menu", ["Home", "Employee Work Management Portal", "Employee Attendence Form", "Care Planning for Care Home", "Medication Activity", "Document Verification for Care Home", "Emergency", ], 
#icons=['house', 'list-task', 'cloud-upload', 'list-task', 'list-task','list-task'], menu_icon="cast", default_index=0)

choice = option_menu('Menu', [ "Home", "Login/Sign Up", "Employee Work Management Portal", "Task Completion Form", 
			      "Care Planning for Care Home", "Document Management Portal", "Document Sync","Medication Activity","Emergency"],  
		     icons=['home', 'home', 'home', 'home','home', 'home', 'home','home', 'home'],
        menu_icon="cast",default_index=0, orientation="horizontal",
	styles={
        "container": {"padding": "0!important" },
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"10px", "--hover-color":  "#000000","margin-color":"blue"},
        "nav-link-selected": {"background-color": "green"},
    	})

#menu = ["About Us","Employee Work Management Portal", "Employee Attendence Form", "Care Planning for Care Home", "Medication Activity"]
#choice = st.sidebar.selectbox( " ## Menu " ,menu)
if choice == "Home":
	st.title("Glovalth Health Tech Care Limited")
	st.subheader ("Who We Are")
	st.info(""" ##### Proudly serving the UK’s care homes from our Leicester headquarters. We specialize in timesheet management solutions tailored for the care industry. Our tools simplify payroll, boost productivity, and ensure compliance. Partner with us for efficient and reliable staff management.""")
	st.subheader("What We Do")
	st.info(""" ##### Our Business team ensures smooth and efficient operations, supporting every aspect of our business. From handling client inquiries to managing internal processes, they are the backbone of our organization. Their dedication to excellence and attention to detail guarantee high-quality service and operational integrity. Our primary objective is to develop comprehensive and standardized HR software applications tailored specifically for UK industries. We aim to provide solutions that streamline human resource management, enhance operational efficiency, and support the unique needs of businesses across various sectors in the UK. By leveraging advanced technology and industry best practices, we strive to deliver user-friendly and adaptable software that meets the evolving demands of the modern workforce.""")
	st.subheader("How We Support")
	st.info(""" ##### Our primary objective is to develop comprehensive and standardized HR software applications tailored specifically for UK industries. We aim to provide solutions that streamline human resource management, enhance operational efficiency, and support the unique needs of businesses across various sectors in the UK. By leveraging advanced technology and industry best practices, we strive to deliver user-friendly and adaptable software that meets the evolving demands of the modern workforce.""")
	st.subheader("Reach Us")
	st.info(""" ##### Get in touch with us today to discover how our HR management solutions can transform your business. Whether you have questions, need support, or want to schedule a consultation, our dedicated team is here to help. Reach out via phone, email, or our online form – we look forward to connecting with you!""")
	st.info( """ ##### Address: St George’s House, 3rd floor, St George’s house, Leicestershire, United Kingdom.""")
	st.info( """ ##### Call us: +44 7436 295021 """)
	st.info( """ ##### Email: glovalthhealthtechcarelmt@gmail.com """)
	
if choice == "Task Completion Form":
	st.title("Task Completion Form")
	st.subheader("Enter your Task details here 👇")
	with st.form("form1", clear_on_submit = True):
		
		id = st.text_input(' Employee ID *', placeholder = "Enter your Employee ID here") 
		Clientname = st.text_input("Client name *", placeholder = "Enter your Client Name here")
		date = st.date_input("Task Date *")
		starttime =  st.time_input("Start time*", datetime.time(0,0))
		endtime = st.time_input("End time *", datetime.time(0,0))
		Tasknotes = st.text_area (" Notes Regarding Time Period *", placeholder = " Type your notes here")
		st.subheader(" Activity Record *")
		activity, check, notes = st.columns(3, vertical_alignment="bottom")
		activity.multiselect("Task Name",( "Medication Administration", "Assist with meal preparation", "Vital Signs Monitoring", "Transportation and Errands", "Housekeeping", "Wound Care", "Assistance with Medical Devices", "Mobility Assistance", "Personal Care with Medical Focus","Personal Hygiene", "Emotional Support"), placeholder = "Choose your Task activity here")
		check.checkbox("Task Completed")
		check.checkbox("Task Pending")
		notes.text_area(" ", placeholder = "Write notes on any task or pending task")
		clientnotes = st.text_area (" Patient Notes *", placeholder = " Type your feedback here")
		upload_image = st.file_uploader("Upload image file relevant to your task if needed", accept_multiple_files=True, type=['jpg','jpeg','png'])
		
		subdate = st.date_input("Form Submission Date*")
		st.subheader("Signature*")
		empsign, patientsign = st.columns(2, vertical_alignment="bottom")
		empsign.info("Employee Signature✍️ ")
		patientsign.info( "Patient Signature ✍️")
		st.warning("⚠️ Both the caregiver and the patient/client are required to sign this form.")
		#time_selection = col2.multiselect('select ShiftTime ', data.ShiftTime.unique().tolist(), key='time')
		submitted = st.form_submit_button("Submit this form")
	

if choice == "Employee Work Management Portal":
	st.title(" Welcome to Glovalth Employee Portal")
	emp_number = st.text_input(r"$\textsf{\Large Enter your Employee ID here}$", placeholder = " Type Employee ID as E001 OR E012 to test the prototype")
	df1 = pd.concat(map(pd.read_csv, ['E001_Week_1.csv','E012_Week_2.csv']))   
	if emp_number:
		data = df1[df1['EmployeeID'] == emp_number]
		df = pd.DataFrame(data)
		st.write("""#### Check your work allocation for this week here 👇 """)
		dynamic_filters = DynamicFilters(df, filters=['Date', 'ShiftTime', 'TaskType'])
		#st.write("Find your assigned work here 👇")
		dynamic_filters.display_filters(location='columns', num_columns=3, gap='medium')
		dynamic_filters.display_df()
	

		#col1, col2 = st.columns(2)
		#date_selection = col1.multiselect('select Date ', data.Date.unique().tolist(), key='date')
		#time_selection = col2.multiselect('select ShiftTime ', data.ShiftTime.unique().tolist(), key='time')
		#st.write(data.date)unique.tolist())
		#st.write(data[data.Date.isin(choices)])
		#search_date = data.Date.unique().tolist()
		
		#st.info("Choose the date below")
		#choices = st.multiselect(" ",search_date)
		#search_time = data.ShiftTime.unique().tolist()
		#choices = st.multiselect(" ",search_time)
		#st.write(data[data.Date.isin(choices)])
		
		#st.write(data[["Employee ID",'Location','Date','Day','Shift Timing','Tasks']])
    
	else:
	   st.write("""##### If you dont know your Employee number or work is not allocated, Please contact your organisation""")
                

if choice == "Login/Sign Up":
	st.header(":red[We are Working on It! Thank you for your interest in our product. We are currently fine-tuning this feature to provide you with the best experience possible. Please check back soon!]")

if choice == "Care Planning for Care Home":
	st.header(":red[We are Working on It! Thank you for your interest in our product. We are currently fine-tuning this feature to provide you with the best experience possible. Please check back soon!]")

if choice == "Document Management Portal":
	st.header(":red[We are Working on It! Thank you for your interest in our product. We are currently fine-tuning this feature to provide you with the best experience possible. Please check back soon!]")

if choice == "Document Sync":
	st.header(":red[We are Working on It! Thank you for your interest in our product. We are currently fine-tuning this feature to provide you with the best experience possible. Please check back soon!]")

if choice == "Medication Activity":
	st.header(":red[We are Working on It! Thank you for your interest in our product. We are currently fine-tuning this feature to provide you with the best experience possible. Please check back soon!]")

if choice == "Emergency":
	st.header(":red[We are Working on It! Thank you for your interest in our product. We are currently fine-tuning this feature to provide you with the best experience possible. Please check back soon!]")


