import streamlit as st
import pandas as pd
import mysql.connector

# Streamlit app title
st.title("Upload CSV to MySQL")

# Upload file
uploaded_file = st.file_uploader("Choose a CSV file", type=".csv")

# MySQL database connection details
host = '127.0.0.1'
user = 'root'
password = 'LeakTimeBike4242'
database = 'globalhris'

# Function to create MySQL table
def create_table(cursor, table_name, columns):
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(query)

# Function to insert data into MySQL table
def insert_data(cursor, table_name, data):
    placeholders = ", ".join(["%s"] * len(data.columns))
    columns = ", ".join(data.columns)
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.executemany(query, data.values.tolist())

# Connect to MySQL database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

if conn.is_connected():
    cursor = conn.cursor()

    # Streamlit button to upload CSV and insert data into MySQL
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Streamlit data preview
        st.write(data)

        # Streamlit button to insert data into MySQL
        if st.button("Insert Data"):
            table_name = st.text_input("Enter table name:")
            columns = ", ".join(data.columns)
            create_table(cursor, table_name, columns)
            insert_data(cursor, table_name, data)
            conn.commit()
            st.success("Data inserted into MySQL table successfully.")

    # Close MySQL database connection
    conn.close()
