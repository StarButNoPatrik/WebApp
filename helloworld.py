import streamlit as st

st.title('Sample Streamlit Run..!!')

name = st.text_input("Enter your name:")

if name:
    if name.isnumeric():
        st.error("Error: Please enter a valid name.")
    else:
        st.write(f"Hello {name}!!")
else:
    st.write("Please enter your name.")
