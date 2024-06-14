
import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber

def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()
	return all_page_text

def read_pdf2(file):
	with pdfplumber.open(file) as pdf:
	    page = pdf.pages[0]
	    return page.extract_text()


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 
	
			
def main():
	
	# Streamlit Dashboard          
	st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
	st.image("logo.png", width = 400)
	st.title("Global HR Implementation Services Limited")
	menu = ["About Us","Upload Payslip","AI Net Pay Difference Finder"]
	choice = st.sidebar.selectbox("Menu",menu)


				                   				
	if choice == "Upload Payslip":
		st.subheader("Upload your payslip")
		docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
		if st.button("Process"):
			if docx_file is not None:
				file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
				st.write(file_details)
				# Check File Type
				if docx_file.type == "text/plain":
					# raw_text = docx_file.read() # read as bytes
					# st.write(raw_text)
					# st.text(raw_text) # fails
					st.text(str(docx_file.read(),"utf-8")) # empty
					raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for further processing
					# st.text(raw_text) # Works
					st.write(raw_text) # works
				elif docx_file.type == "application/pdf":
					# raw_text = read_pdf(docx_file)
					# st.write(raw_text)
					try:
						with pdfplumber.open(docx_file) as pdf:
							page = pdf.pages[0]
							text = page.extract_text()
							st.write(text)
							for row in text.split('\n'):
								if row.startswith('Net Pay'):
									NetPay = row.split()[-1]
					except:
						st.write("None")
					    	
				elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
				# Use the right file processor ( Docx,Docx2Text,etc)
					raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class 
					st.write(raw_text)
					
	elif choice == "AI Net Pay Difference Finder":
		st.subheader("AI Net Pay Difference Finder")
		file = st.file_uploader("Upload File",type=["csv"])
		if file is not None:
			df = pd.read_csv(file)
			month1 = st.selectbox("Select the first month", df.columns)
			month2 = st.selectbox("Select the second month", df.columns)
			Net_Pay_Diff = st.text_input("Enter the name of the new column", "Net Pay Difference")
			df[Net_Pay_Diff] = df[month1] - df[month2]
			#st.write("Net Pay Difference of all the Employees")
			#st.write(df)
			emp_number = st.text_input("Enter the employee number:")
			for row in df:
				if emp_number:
					empdata = df[df['Employee Number'] == int(emp_number)]
					st.write("The net pay difference for employee number {} is:".format(emp_number))
					st.write(empdata)
					break
							
	else:
		st.subheader("About Us")
		st.info("Global HR Implementataion Sevices Ltd")
		st.text("Here at Global HRIS, we specialise in global payroll implementation services. \nFrom data migration services to payroll project management. \nWe support clients on their digital transformation journey.")
		st.info("+44 161 317 2903")
		st.info("info@globalhris.co.uk")
		st.info("International House, 61 Mosley Street, Manchester, M2 3HZ")
		

if __name__ == '__main__':
	main()         
    
		 
