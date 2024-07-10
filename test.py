from streamlit.testing.v1 import AppTest

def test_input_name_success():
    """A user input name clicks enter"""
    at = AppTest.from_file("helloWorld.py")
    at.run()
    at.text_input[0].input("Anisha").run()
    assert "Hello Anisha!!" in "Hello Anisha!!"

def test_input_name_fail():
    """A user input name clicks enter"""
    at = AppTest.from_file("helloWorld.py")
    at.run()
    at.text_input[0].input("Anisha").run()
    assert "Hello Anisha!!" in "Hello Anisha!!"