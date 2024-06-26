import streamlit as st
import pandas as pd
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

#def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    #"""
    #Adds a UI on top of a dataframe to let viewers filter columns

    #Args:
        #df (pd.DataFrame): Original dataframe

    #Returns:
        #pd.DataFrame: Filtered dataframe
    #"""
    #modify = st.checkbox("Add filters")

    #if not modify:
        #return df 

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
		for col in data.columns:
			if is_object_dtype(data[col]):
    				try:
    	    				data[col] = pd.to_datetime(data[col])
    				except Exception:
    	    				pass
			if is_datetime64_any_dtype(data[col]):
        			data[col] = data[col].dt.tz_localize(None)

		
		modification_container = st.container()
		with modification_container:
        		to_filter_columns = st.multiselect("Filter dataframe on", data.columns)
        		for column in to_filter_columns:
            			left, right = st.columns((1, 20))
            			# Treat columns with < 10 unique values as categorical
            			if is_categorical_dtype(data[column]) or data[column].nunique() < 10:
                			user_cat_input = right.multiselect(
                   				 f"Values for {column}",
                    				 data[column].unique(),
                    				 default=list(data[column].unique()),
					)data = data[data[column].isin(user_cat_input)]
				elif is_numeric_dtype(data[column]):
                			_min = float(data[column].min())
               	 			_max = float(data[column].max())
                			step = (_max - _min) / 100
                			user_num_input = right.slider(
                    				f"Values for {column}",
                    				min_value=_min,
                    				max_value=_max,
                    				value=(_min, _max),
                    				step=step,
					)
					data = data[data[column].between(*user_num_input)]
            			elif is_datetime64_any_dtype(data[column]):
                			user_date_input = right.date_input(
                    				f"Values for {column}",
                    				value=(
                        				data[column].min(),
                        				data[column].max(),
                    				),
                			)
                			if len(user_date_input) == 2:
                    				user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    				start_date, end_date = user_date_input
                    				data = data.loc[data[column].between(start_date, end_date)]
            			else:
               	 			user_text_input = right.text_input(
                    				f"Substring or regex in {column}",
                			)
                			if user_text_input:
                    				data = data[data[column].astype(str).str.contains(user_text_input)]
		st.write("""## Check Your Timesheet allocation here""")
        	st.write(data[["Employee ID",'Location','Date','Day','Shift Timing','Tasks']])
    
	else:
	   st.write("""##### If you dont know your Employee number or work is not allocated, Please contact your organisation""")
                
else:
	st.subheader ("Our Base")
	st.info(""" #### Proudly serving the UK’s care homes from our Leicester headquarters. We specialize in timesheet management solutions tailored for the care industry. Our tools simplify payroll, boost productivity, and ensure compliance. Partner with us for efficient and reliable staff management.""")
	st.subheader("What We Do")
	st.info(""" #### Our Business team ensures smooth and efficient operations, supporting every aspect of our business. From handling client inquiries to managing internal processes, they are the backbone of our organization. Their dedication to excellence and attention to detail guarantee high-quality service and operational integrity. Our primary objective is to develop comprehensive and standardized HR software applications tailored specifically for UK industries. We aim to provide solutions that streamline human resource management, enhance operational efficiency, and support the unique needs of businesses across various sectors in the UK. By leveraging advanced technology and industry best practices, we strive to deliver user-friendly and adaptable software that meets the evolving demands of the modern workforce.""")
	st.subheader("How we support")
	st.info(""" #### Our primary objective is to develop comprehensive and standardized HR software applications tailored specifically for UK industries. We aim to provide solutions that streamline human resource management, enhance operational efficiency, and support the unique needs of businesses across various sectors in the UK. By leveraging advanced technology and industry best practices, we strive to deliver user-friendly and adaptable software that meets the evolving demands of the modern workforce.""")
	st.subheader("Reach Us")
	st.info(""" #### Get in touch with us today to discover how our HR management solutions can transform your business. Whether you have questions, need support, or want to schedule a consultation, our dedicated team is here to help. Reach out via phone, email, or our online form – we look forward to connecting with you!""")
	st.info( """ ##### Address: St George’s House, 3rd floor, St George’s house, Leicestershire, United Kingdom.""")
	st.info( """ ##### Call us: +44 7436 295021 """)
	st.info( """ ##### Email: glovalthhealthtechcarelmt@gmail.com """)

