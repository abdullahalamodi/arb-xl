import pytest
from arb_xl.json_to_xls import json_to_xls
from arb_xl.xls_to_json import xls_to_json
from pathlib import Path
import json
import pandas as pd

# Define test files
TEST_JSON_FILE = Path("tests/test_en.json")
TEST_XLS_FILE = Path("tests/test_output.xlsx")
TEST_JSON_OUTPUT_DIR = Path("tests/output_json")

# Sample JSON data
SAMPLE_JSON = {
    "hello": "Hello",
    "bye": "Goodbye"
}

@pytest.fixture
def setup_json_file():
    """Creates a test JSON file."""
    with open(TEST_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(SAMPLE_JSON, f, indent=2, ensure_ascii=False)
    yield
    TEST_JSON_FILE.unlink()  # Clean up after test

def test_json_to_xls(setup_json_file):
    """Test converting JSON to XLS."""
    json_to_xls([TEST_JSON_FILE], TEST_XLS_FILE)
    
    # Check if file was created
    assert TEST_XLS_FILE.exists()

    # Read XLS file and verify content
    df = pd.read_excel(TEST_XLS_FILE)
    assert "Key" in df.columns
    assert "test_en" in df.columns  # File stem should be used as language name
    assert df.loc[df["Key"] == "hello", "test_en"].values[0] == "Hello"
    assert df.loc[df["Key"] == "bye", "test_en"].values[0] == "Goodbye"

    # Clean up
    TEST_XLS_FILE.unlink()

def test_xls_to_json(setup_json_file):
    """Test converting XLS to JSON."""
    json_to_xls([TEST_JSON_FILE], TEST_XLS_FILE)  # Convert JSON to XLS first
    TEST_JSON_OUTPUT_DIR.mkdir(exist_ok=True)  # Ensure output dir exists

    xls_to_json(TEST_XLS_FILE, TEST_JSON_OUTPUT_DIR)
    
    output_json_file = TEST_JSON_OUTPUT_DIR / "test_en.json"
    
    # Check if JSON file was created
    assert output_json_file.exists()
    
    with open(output_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert data["hello"] == "Hello"
    assert data["bye"] == "Goodbye"

    # Clean up
    TEST_XLS_FILE.unlink()
    output_json_file.unlink()
    TEST_JSON_OUTPUT_DIR.rmdir()
