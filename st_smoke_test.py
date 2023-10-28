import os
from streamlit.testing.v1 import AppTest

def test_noop():
    # Needed to work around result xml bug
    # See https://github.com/pmeier/pytest-results-action/issues/10#issuecomment-1677254333
    assert True

def test_smoke():
    APP_PATH = os.getenv("APP_PATH", default="streamlit_app.py")
    at = AppTest.from_file(APP_PATH).run()
    assert not at.exception
