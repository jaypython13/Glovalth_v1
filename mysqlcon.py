import streamlit as st
import pandas as pd
import mysql.connector

# Create a function to connect to the MySQL database
def create_connection():
    conn = mysql.connector.connect(
        host="ASC-ACA8087",
        user="root",
        password="",
        database="globalhris"
    )
    return conn

# Create a function to load data from a CSV file into a MySQL database
def load_data(file_path):
    conn = create_connection()
    cursor = conn.cursor()
    # Load the data from the CSV file into a Pandas dataframe
    data1 = pd.read_csv(file_path)
    # Create the table in the database
    table_name = "NetPayData"
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} VARCHAR(255)' for col in data1.columns])})"
    cursor.execute(create_table_query)
    # Insert the data into the table
    for row in data1.itertuples():
        insert_query = f"INSERT INTO {table_name} ({', '.join(data1.columns)}) VALUES ({', '.join(['%s' for i in range(len(data1.columns))])})"
        cursor.execute(insert_query, row[1:])
    conn.commit()
    conn.close()

# Create a Streamlit app
def main():
    	# Streamlit Dashboard          
	st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
	st.image("logo.png", width = 400)
	st.title("Global HR Implementation Services Limited")
    	# Create a file uploader to allow the user to select a CSV file
	file = st.file_uploader("Upload CSV file", type="csv")
	if file is not None:
		# Display the file contents in a dataframe
		data = pd.read_csv(file)
		st.write(data)
		# Create a button to load the data into the MySQL database
	if st.button("Load Data"):
		load_data(data)
		st.write("Data loaded successfully!")
		
if __name__=="__main__":
	main()

