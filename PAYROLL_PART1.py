import streamlit as st
import pandas as pd


# Streamlit User Interface part
st.set_page_config(page_title ="Glovalth", page_icon =":guardsman:", layout ="wide")
st.image("Glovalth_logo.png", width = 400)
st.title("Glovalth Health private Limited \n Care Home EmployeeTime Sheet Management")
emp_number = st.text_input("Enter Employee ID")

df1 = pd.read_csv('E001_EMP_DATA.csv', usecols = ['Employee ID', 'Employee Name', 'Organisation ID'])
df2 = pd.read_csv('E012_EMP_DATA.csv',usecols = ['Employee ID', 'Employee Name', 'Organisation ID'])

#df = pd.concat(map(pd.read_csv, ['Feb_Data.csv','March_Data.csv']))
df =pd.concat(df1, df2)
#def netpay_diff(emp_number):    
    #netpay_diff = df1["Net Pay"]-df2["Net Pay"]
    #st.write(netpay_diff)
    #return netpay_diff

# Condition checking              
if emp_number:
    e001 = df1[df1['Employee ID'] == int(emp_number)]
    e012 = df2[df2['Employee ID'] == int(emp_number)]
    st.write("""### E001 employee data""")
    st.write(e001)
    st.write("""### E012 employee data""")
    st.write(e012)
    #current_month_salary = int(row['Net Pay March'])
    #previous_month_salary = int(row['Net Pay Feb'])
    #difference = current_month_salary - previous_month_salary
    st.write("The workplan for employee number {} is:".format(), difference)  
else:
    st.write("Employee number not found. Please contact your organisation")
                
    

