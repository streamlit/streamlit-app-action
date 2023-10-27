import os
from streamlit.testing.v1 import AppTest

def smoke_test():
    APP_PATH = os.getenv("APP_PATH", default="streamlit_app.py")
    at = AppTest.from_file(APP_PATH).run()
    assert not at.exception
