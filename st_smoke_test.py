import os
import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = os.getenv("APP_PATH", default="streamlit_app.py")
SKIP_SMOKE = os.getenv("SKIP_SMOKE", "False").lower() in ("true", "1", "t")


def get_file_paths() -> list[str]:
    page_folder = Path(APP_PATH).parent / "pages"
    if not page_folder.exists():
        return [APP_PATH]
    page_files = page_folder.glob("*.py")
    file_paths = [str(file.absolute().resolve()) for file in page_files]
    return [APP_PATH] + file_paths


def pytest_generate_tests(metafunc):
    """
    Generate a file path for each page in the pages folder, which will
    automatically be used if a test function has a file_path argument

    The automatically-generated test will only have the individual file name
    """
    if "file_path" in metafunc.fixturenames:
        metafunc.parametrize(
            "file_path", get_file_paths(), ids=lambda x: x.split("/")[-1]
        )


@unittest.skipIf(SKIP_SMOKE, "smoke test is disabled by config")
def test_smoke_page(file_path):
    at = AppTest.from_file(file_path, default_timeout=100).run()
    assert not at.exception
