import streamlit as st
import pytest

def test_valid_name_input():
    # Test case for valid name input
    with st.echo(code_location='below'):
        name = "Alice"
        st.text_input("Enter your name:", name)
        output = st._get_widget_value(0)
        assert f"Hello {name}!!" in output

def test_numeric_input_error():
    # Test case for numeric input error
    with st.echo(code_location='below'):
        numeric_input = "123"
        st.text_input("Enter your name:", numeric_input)
        error_message = st.error_message
        assert "Error: Please enter a valid name." in error_message

def test_empty_input():
    # Test case for empty input
    with st.echo(code_location='below'):
        empty_input = ""
        st.text_input("Enter your name:", empty_input)
        prompt_message = st.write_message
        assert "Please enter your name." in prompt_message

if __name__ == "__main__":
    pytest.main()
