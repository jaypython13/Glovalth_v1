#Importing Libraries
import streamlit as st
import pandas as pd
from PIL import Image

# Streamlit Dashboard          
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 400)
st.title("Global HR Implementation Services Limited \n Net Pay Difference Calculator")

file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf", "csv"])

# Set up the Streamlit interface
st.title("Upload the input file to check the difference")
st.write("Upload an  PDF, or CSV file below:")

# uploading input file as payslip pdf
st.write("Please upload a pdf file")

uploaded_pdffile = st.file_uploader("Choose a pdf file", type=["pdf"])
if uploaded_pdffile is not None:
        pdf = pdftotext.PDF(file)
        first_page = pdf[0]
        st.write(first_page)        
    

# Uploading the input csv file

st.write("Please upload a csv file")
uploaded_csvfile = st.file_uploader("Choose a csv file", type=["csv"])

if uploaded_csvfile is not None:
    df = pd.read_csv(uploaded_file)
    column1 = st.selectbox("Select the first month", df.columns)
    column2 = st.selectbox("Select the second month", df.columns)
    new_column_name = st.text_input("Enter the name of the new column", "Net Pay Difference")
    df[new_column_name] = df[column1] - df[column2]
    st.write("Net Pay Difference of all the Employees")
    st.write(df)
    emp_number = st.text_input("Enter the employee number:")
    for row in df:
        if emp_number:
                 empdata = df[df['Employee Number'] == int(emp_number)]
                 st.write("The net pay difference for employee number {} is:".format(emp_number))
                 st.write(empdata)   
                 break
                    

     

       
          
