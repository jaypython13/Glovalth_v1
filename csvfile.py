import streamlit as st
import pandas as pd



st.title('Text to CSV Converter')
file = st.file_uploader("Upload a text file", type=["txt"])

if file:
    st.write(f"Uploading file: {file.name}")
    #text_to_csv(file)
    data = []
    for line in file:
        data.append(line.strip().split())
        df = pd.DataFrame(data)
        df.to_csv('output.csv', index=False)
    st.download_button(
        label="Download CSV",
        data=open('output.csv', 'rb').read(),
        file_name='output.csv',
        mime='text/csv'
    )
