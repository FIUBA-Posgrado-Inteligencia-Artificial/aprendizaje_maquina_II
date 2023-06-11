"""
test_functions.py

Fixture - The test function test_import_data() will 
use the return of path() as an argument
"""

# test_import_data.py

import pytest
from data_handle import import_data

@pytest.fixture
def dataset_path():
    # Provide the path to the dataset file as needed
    return "Test_BigMart_wrong.csv"

# Test case 1: Test if the dataset is read successfully
def test_read_dataset(dataset_path):
    dataset = import_data(dataset_path)
    assert dataset is not None

# Test case 2: Test if an error is raised when the file is not found
def test_read_dataset_file_not_found():
    with pytest.raises(FileNotFoundError):
        import_data("path/to/nonexistent_file.csv")

# Test case 3: Test if dataframe contains data
def test_read_dataset_file_is_empty(dataset_path):
    dataset = import_data(dataset_path)
    assert len(dataset) > 0
