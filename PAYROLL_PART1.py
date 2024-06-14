import streamlit as st
import pandas as pd
#df1 = pd.read_csv('E001_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])#df2 = pd.read_csv('E012_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])

# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon =":guardsman:", layout ="wide")
st.image("Glovalth_logo.jpeg", width = 400)
st.title("Glovalth Health Tech Care")
menu = ["About Us","Employee Work Management Portal"]
choice = st.sidebar.selectbox("Menu",menu)


if choice == "Employee Work Management Portal":
	st.title(" Welcome to Glovalth Employee TimeSheet Management system Portal")
	emp_number = st.text_input(r"$\textsf{\Large Enter your Employee ID here}$")
	df = pd.concat(map(pd.read_csv, ['E001_EMP_DATA.csv','E012_EMP_DATA.csv']))   
	if emp_number:
        	data = df[df['Employee ID'] == emp_number]
       		st.write("""### Check Your Timesheet allocation here""")
        	st.write(data[["Employee ID",'Location','Date','Day','Shift Timing','Tasks']])
		option = st.selectbox("Choose here", data.columns)
		st.write(data[option])
	else:
	   st.write(""" ##If you dont know your Employee number or work is not allocated, Please contact your organisation""")
                
else:
	st.subheader(" What we do")
	st.info(""" ### Our Business team ensures smooth and efficient operations, supporting every aspect of our business. From handling client inquiries to managing internal processes, they are the backbone of our organization. Their dedication to excellence and attention to detail guarantee high-quality service and operational integrity.""")

