import streamlit as st
import csv
import pandas as pd

# Streamlit User Interface part
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")

# Get the employee number from the user
employee_number = st.text_input("Enter the employee number:")
# Open the CSV file containing employee data
with open('netpaydata.csv', 'r') as file:
     reader = pd.read_csv(file)
# Loop through each row in the CSV file
for row in reader:
     if row['Employee_number'] == str(employee_number):
           current_month_salary = int(row['Net Pay March'])
           previous_month_salary = int(row['Net Pay Feb'])
           break
     else:
         # If employee number is not found in the CSV file
          st.write("Employee number not found in the CSV file.")
          
        
# Calculate the difference
difference = current_month_salary - previous_month_salary  
# Display the result
st.write("The net pay difference for employee number {} is:".format(employee_number), difference)


