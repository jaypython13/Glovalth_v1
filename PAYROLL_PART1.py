
import streamlit as st
import pandas as pd
import numpy as np
import csv
from streamlit_option_menu import option_menu
from streamlit_dynamic_filters import DynamicFilters
import base64

#df1 = pd.read_csv('E001_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])
#df2 = pd.read_csv('E012_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])

# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon ="	:medical_symbol:")

primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
LOGO_IMAGE = "Glovalth_logo.png"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #FFFFFF !important;
        padding-top: 50px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Glovalth Health Tech Care Limited</p>
    </div>
    """,
    unsafe_allow_html=True
)


#st.image("Glovalth_logo.jpeg", width =200)


	#choice1 = option_menu("Main Menu", ["Home", "Employee Work Management Portal", "Employee Attendence Form", "Care Planning for Care Home", "Medication Activity", "Document Verification for Care Home", "Emergency", ], 
        #icons=['house', 'list-task', 'cloud-upload', 'list-task', 'list-task','list-task'], menu_icon="cast", default_index=0)

choice = option_menu("Menu", ["Home", "Employee Work Management Portal", "Task Completion Form", 
			      "Care Planning for Care Home", "Document Management Portal", "Document Sync","Medication Activity","Emergency"], 
        icons=['house'], menu_icon="cast",default_index=1, orientation="horizontal", 
	styles={
        "container": {"padding": "0!important" },
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color":  "#000000"},
        "nav-link-selected": {"background-color": "green"},
    	})

#menu = ["About Us","Employee Work Management Portal", "Employee Attendence Form", "Care Planning for Care Home", "Medication Activity"]
#choice = st.sidebar.selectbox( " ## Menu " ,menu)


if choice == "Employee Work Management Portal":
	st.title(" Welcome to Glovalth Employee Portal")
	emp_number = st.text_input(r"$\textsf{\Large Enter your Employee ID here}$")
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
                
if choice == "Home":
	st.title("Glovalth Health Tech Care Limited")
	st.subheader ("Who we are")
	st.info(""" ##### Proudly serving the UK’s care homes from our Leicester headquarters. We specialize in timesheet management solutions tailored for the care industry. Our tools simplify payroll, boost productivity, and ensure compliance. Partner with us for efficient and reliable staff management.""")
	st.subheader("What We Do")
	st.info(""" ##### Our Business team ensures smooth and efficient operations, supporting every aspect of our business. From handling client inquiries to managing internal processes, they are the backbone of our organization. Their dedication to excellence and attention to detail guarantee high-quality service and operational integrity. Our primary objective is to develop comprehensive and standardized HR software applications tailored specifically for UK industries. We aim to provide solutions that streamline human resource management, enhance operational efficiency, and support the unique needs of businesses across various sectors in the UK. By leveraging advanced technology and industry best practices, we strive to deliver user-friendly and adaptable software that meets the evolving demands of the modern workforce.""")
	st.subheader("How we support")
	st.info(""" ##### Our primary objective is to develop comprehensive and standardized HR software applications tailored specifically for UK industries. We aim to provide solutions that streamline human resource management, enhance operational efficiency, and support the unique needs of businesses across various sectors in the UK. By leveraging advanced technology and industry best practices, we strive to deliver user-friendly and adaptable software that meets the evolving demands of the modern workforce.""")
	st.subheader("Reach Us")
	st.info(""" ##### Get in touch with us today to discover how our HR management solutions can transform your business. Whether you have questions, need support, or want to schedule a consultation, our dedicated team is here to help. Reach out via phone, email, or our online form – we look forward to connecting with you!""")
	st.info( """ ##### Address: St George’s House, 3rd floor, St George’s house, Leicestershire, United Kingdom.""")
	st.info( """ ##### Call us: +44 7436 295021 """)
	st.info( """ ##### Email: glovalthhealthtechcarelmt@gmail.com """)

