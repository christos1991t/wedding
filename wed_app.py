import streamlit as st
import pandas as pd
import io


buffer = io.BytesIO()

st.set_page_config(page_title="Γαμος Νικου - Βασιλικης", layout="wide")
st.title("Λιστα καλεσμενων")

# Read data from Excel file
df = pd.read_excel("wedding.xlsx")
df = df.fillna('')
df['Τηλεφωνο'] = df['Τηλεφωνο'].astype(str).str.rstrip('.0')

column_values = df['Επωνυμο '].tolist()

# Allow user to select one or multiple values from the 'Επωνυμο' column
selected_values = st.multiselect('Επιλογη επωνυμου καλεσμενου', column_values)

# Filter the data based on the selected values
if selected_values:
    filtered_df = df[df['Επωνυμο '].isin(selected_values)]
    edited_df = st.experimental_data_editor(filtered_df, num_rows="dynamic")
    if st.button('Αποθηκευση Αλλαγων'):
        # Update the original Excel file with the changes made in the data editor
        df.update(edited_df)
        df.to_excel("wedding.xlsx", index=False)
        st.success("Η αλλαγες αποθηκευτικαν")
else:
    edited_df = st.experimental_data_editor(df, num_rows="dynamic")
    sum_guests =  edited_df['Ατομα'].sum()
    st.text(f'Συνολο καλεσμενων {sum_guests}')
    if st.button('Αποθηκευση Αλλαγων'):
        # Update the original Excel file with the changes made in the data editor
        df.update(edited_df)
        df.to_excel("wedding.xlsx", index=False)
        st.success("Η αλλαγες αποθηκευτικαν")

with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    # Write each dataframe to a different worksheet.
    edited_df.to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file to the buffer
    writer.save()

    st.download_button(
        label="Κατεβασμα Λιστας",
        data=buffer,
        file_name="Λιστα Καλεσμενων.xlsx",
        mime="application/vnd.ms-excel"
    )
