import streamlit as st
import pandas as pd

st.set_page_config(page_title="Γαμος Νικου - Βασιλικης", layout="wide")
st.title("Λιστα καλεσμενων")

# Read data from Excel file
df = pd.read_excel("wedding.xlsx")
df = df.fillna('')
df['Τηλεφωνο'] = df['Τηλεφωνο'].astype(str).str.replace('[,.]', '')

# Get unique values for the 'Επωνυμο' column
column_values = df['Επωνυμο '].tolist()

# Allow user to select one or multiple values from the 'Επωνυμο' column
selected_values = st.multiselect('Επιλογη επωνυμου καλεσμενου', column_values)

# Filter the data based on the selected values
if selected_values:
    filtered_df = df[df['Επωνυμο '].isin(selected_values)]
    edited_df = st.experimental_data_editor(filtered_df, num_rows="dynamic")
    if st.button('Save changes'):
        # Update the original Excel file with the changes made in the data editor
        df.update(edited_df)
        df.to_excel("wedding.xlsx", index=False)
else:
    edited_df = st.experimental_data_editor(df, num_rows="dynamic")
    if st.button('Save changes'):
        # Update the original Excel file with the changes made in the data editor
        df.update(edited_df)
        df.to_excel("wedding.xlsx", index=False)
