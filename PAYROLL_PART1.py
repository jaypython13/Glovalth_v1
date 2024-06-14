import streamlit as st
import pandas as pd
#df1 = pd.read_csv('E001_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])#df2 = pd.read_csv('E012_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])

# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon =":guardsman:", layout ="wide")
st.image("Glovalth_logo.jpeg", width = 400)
st.title("Glovalth Health Tech Care Limited")
menu = ["About Us","Employee Work Management Portal"]
choice = st.sidebar.selectbox("Menu",menu)


if choice == "Employee Work Management Portal":
	st.title(" Welcome to Glovalth Employee TimeSheet Management system Portal")
	emp_number = st.text_input(r"$\textsf{\Large Enter your Employee ID here}$")
	df = pd.concat(map(pd.read_csv, ['E001_EMP_DATA.csv','E012_EMP_DATA.csv']))   
	if emp_number:
        	data = df[df['Employee ID'] == emp_number]
       		st.write("""## Check Your Timesheet allocation here""")
        	st.write(data[["Employee ID",'Location','Date','Day','Shift Timing','Tasks']])
		
		
	else:
	   st.write("""##### If you dont know your Employee number or work is not allocated, Please contact your organisation""")
                
else:
	st.subheader("What We Do")
	st.info(""" ### Our Business team ensures smooth and efficient operations, supporting every aspect of our business. From handling client inquiries to managing internal processes, they are the backbone of our organization. Their dedication to excellence and attention to detail guarantee high-quality service and operational integrity.""")
	st.subheader ("Our Base")
	st.info(""" ### Proudly serving the UK’s care homes from our Leicester headquarters. We specialize in timesheet management solutions tailored for the care industry. Our tools simplify payroll, boost productivity, and ensure compliance. Partner with us for efficient and reliable staff management.""")
	st.subheader("Contact US")
	st.info(""" ### Get in touch with us today to discover how our HR management solutions can transform your business. Whether you have questions, need support, or want to schedule a consultation, our dedicated team is here to help. Reach out via phone, email, or our online form – we look forward to connecting with you!""")
	st.info( """ ## Address: LEICESTER, St George’s House, 3rd floor, St George’s house, Leicestershire, United Kingdom.""")
	st.info( """ Telephone: +44 7436 295021 """)
	st.info( """ Email: glovalthhealthtechcarelmt@gmail.com """)

