import streamlit as st
import pandas as pd

st.set_page_config(page_title="Γαμος Νικου - Βασιλικης", layout="wide")
st.title("Λιστα καλεσμενων")

df = pd.read_excel("wedding.xlsx")
df = df.fillna('')
df['Τηλεφωνο'] = df['Τηλεφωνο'].astype(str).str.replace('[,.]', '')

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Get unique values for the 'column_name' column
column_values = df['Επωνυμο '].tolist()

# Allow user to select one or multiple values from the 'column_name' column
selected_values = st.multiselect('Επιλογη επωνυμου καλεσμενου', column_values)

# Filter the data based on the selected values
if selected_values:
    df = df[df['Επωνυμο '].isin(selected_values)]


st.table(df)
