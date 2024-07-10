import streamlit as st
import pythontest

def test_valid_name_input():
    # Test case for valid name input
    with st._is_running_with_streamlit():
        valid_name = "Alice"
        st.text_input("Enter your name:", valid_name)
        assert st._is_running_with_streamlit()

def test_numeric_input_error():
    # Test case for numeric input error
    with st._is_running_with_streamlit():
        numeric_input = "123"
        st.text_input("Enter your name:", numeric_input)
        error_message = st.error_message
        assert "Error: Please enter a valid name." in error_message

def test_empty_input():
    # Test case for empty input
    with st._is_running_with_streamlit():
        empty_input = ""
        st.text_input("Enter your name:", empty_input)
        assert "Please enter your name." in st.write_message

if __name__ == "__main__":
    pytest.main()
