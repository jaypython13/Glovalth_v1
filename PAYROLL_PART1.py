
import streamlit as st
import pandas as pd
import numpy as np
import csv

#df1 = pd.read_csv('E001_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])
#df2 = pd.read_csv('E012_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])
def filters_widgets(df, columns=None, allow_single_value_widgets=False):
    # Parse the df and get filter widgets based for provided columns
    if not columns: #if columns not provided, use all columns to create widgets
        columns=df.columns.tolist()
    if allow_single_value_widgets:
        threshold=0
    else:
        threshold=1
    widget_dict = {}
    filter_widgets = st.container()
    filter_widgets.warning(
        "After selecting filters press the 'Apply Filters' button at the bottom.")
    if not allow_single_value_widgets:
        filter_widgets.markdown("Only showing columns that contain more than 1 unique value.")
    with filter_widgets.form(key="data_filters"):
        not_showing = [] 
        for y in df[columns]:
            if str(y) in st.session_state: #update value from session state if exists
                selected_opts = st.session_state[str(y)]
            else: #if doesnt exist use all values as defaults
                selected_opts = df[y].unique().tolist()
            if len(df[y].unique().tolist()) > threshold: #checks if above threshold
                widget_dict[y] = st.multiselect(
                    label=str(y),
                    options=df[y].unique().tolist(),
                    default=selected_opts,
                    key=str(y),
                )
            else:#if doesnt pass threshold
                not_showing.append(y)
        if not_showing:#if the list is not empty, show this warning
            st.warning(
                f"Not showing filters for {' '.join(not_showing)} since they only contain one unique value."
            )
        submit_button = st.form_submit_button("Apply Filters")
    #reset button to return all unselected values back
    reset_button = filter_widgets.button(
        "Reset All Filters",
        key="reset_buttons",
        on_click=reset_filter_widgets_to_default,
        args=(df, columns),
    )
    filter_widgets.warning(
        "Dont forget to apply filters by pressing 'Apply Filters' at the bottom."
    )

def reset_filter_widgets_to_default(df, columns):
    for y in df[columns]:
        if str(y) in st.session_state:
            del st.session_state[y]


# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon =":guardsman:", layout ="wide")
st.image("Glovalth_logo.jpeg", width = 400)
st.title("Glovalth Health Tech Care Limited")
menu = ["About Us","Employee Work Management Portal"]
choice = st.sidebar.selectbox("Menu",menu)


if choice == "Employee Work Management Portal":
	st.title(" Welcome to Glovalth Employee TimeSheet Management system Portal")
	emp_number = st.text_input(r"$\textsf{\Large Enter your Employee ID here}$")
	df1 = pd.concat(map(pd.read_csv, ['E001_EMP_DATA.csv','E012_EMP_DATA.csv']))   
	if emp_number:
		data = df1[df1['Employee ID'] == emp_number]
		st.write("""## Check Your Timesheet allocation here""")
		df=pd.DataFrame(data)
		filters_widgets(df)
		st.write(df)
		#regular_search_term = data.Date.unique().tolist()
		#regular_search_time = data.ShiftTiming.unique().tolist()
		#choices = st.multiselect(" ",regular_search_term)
		#st.write(data[data.Date.isin(choices)])
		#choices = st.multiselect(" ",regular_search_time)
		#st.write(data[data.ShiftTiming.isin(choices)])
		
		#st.write(data[["Employee ID",'Location','Date','Day','Shift Timing','Tasks']])
    
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

