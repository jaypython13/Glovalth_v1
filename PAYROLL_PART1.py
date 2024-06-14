import streamlit as st
import pandas as pd

# Streamlit User Interface part
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n AI Employee Net Pay Difference Calculator")
emp_number = st.text_input("Enter Employee Number")

df1 = pd.read_csv('Feb_Data.csv', usecols = ['Employee Number', 'Forename', 'Surname', 'Net Pay'])
df2 = pd.read_csv('March_Data.csv',usecols = ['Employee Number', 'Forename', 'Surname', 'Net Pay'])

#df = pd.concat(map(pd.read_csv, ['Feb_Data.csv','March_Data.csv']))
df =pd.concat(df1, df2)
#def netpay_diff(emp_number):    
    #netpay_diff = df1["Net Pay"]-df2["Net Pay"]
    #st.write(netpay_diff)
    #return netpay_diff

# Condition checking              
if emp_number:
    feb = df1[df1['Employee Number'] == int(emp_number)]
    Mar = df2[df2['Employee Number'] == int(emp_number)]
    st.write("""### February employee data""")
    st.write(feb)
    st.write("""### March employee data""")
    st.write(Mar)
    current_month_salary = int(row['Net Pay March'])
    previous_month_salary = int(row['Net Pay Feb'])
    difference = current_month_salary - previous_month_salary
    st.write("The net pay difference for employee number {} is:".format(employee_number), difference)  
else:
    st.write("Employee number not found in the CSV file.")
                
    

