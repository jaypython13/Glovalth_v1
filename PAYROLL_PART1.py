import streamlit as st
import pandas as pd


# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon =":guardsman:", layout ="wide")
st.image("Glovalth_logo.jpeg", width = 400)
st.title("Glovalth Health Tech Care")
st.title(" Welcome to Glovalth Employee TimeSheet Management system Portal")
menu = ["About Us","Employee Work plan"]
choice = st.sidebar.selectbox("Menu",menu)
emp_number = st.text_input(r"$\textsf{\Large Enter your Employee ID here}$")


#df1 = pd.read_csv('E001_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])
#df2 = pd.read_csv('E012_EMP_DATA.csv',usecols = ['Employee ID','Location', 'Date','Day', 'Shift Timing','Tasks'])
df = pd.concat(map(pd.read_csv, ['E001_EMP_DATA.csv','E012_EMP_DATA.csv']))


# Condition checking              
if emp_number:
    data = df[df['Employee ID'] == emp_number]
    st.write("""### Check Your Timesheet allocation here""")
    st.write(data[["Employee ID",'Location','Date','Day','Shift Timing','Tasks']])
    Date = st.selectbox("Select the date", df.columns)
    time = st.selectbox("Select the date", df.columns)
    #E012 = df[df['Employee ID'] == emp_number]
    #st.write("""### Check Your Timesheet allocation here""")
    #st.write(E012)
    #current_month_salary = int(row['Net Pay March'])
    #previous_month_salary = int(row['Net Pay Feb'])
    #difference = current_month_salary - previous_month_salary
    #st.write("The workplan for employee number {} is:".format(), difference)  
else:
    st.write("Employee number not found. Please contact your organisation")
                
    

