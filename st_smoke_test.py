import os
import glob
import unittest
from streamlit.testing.v1 import AppTest

APP_PATH = os.getenv("APP_PATH", default="streamlit_app.py")
SKIP_SMOKE = os.getenv("SKIP_SMOKE", 'False').lower() in ('true', '1', 't')

@unittest.skipIf(SKIP_SMOKE, "smoke test is disabled by config")
def test_smoke_main():
    at = AppTest.from_file(APP_PATH, default_timeout = 100).run()
    assert not at.exception

@unittest.skipIf(SKIP_SMOKE, "smoke test is disabled by config")
def test_smoke_pages():
    pages_pattern = os.path.join(os.path.dirname(APP_PATH), "pages/*.py")
    page_files = glob.glob(pages_pattern)
    if not page_files:
        raise unittest.SkipTest("No pages found")
    for file in page_files:
        file_path  = os.path.abspath(file)
        at = AppTest.from_file(file_path, default_timeout = 100).run()
        assert not at.exception
