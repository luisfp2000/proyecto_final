import os
import pytest
from load.load_data import DataRetriever


def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
  
    # Provide the path to your CSV file that needs to be tested
    # refactored folder
    REFACTORED_DIRECTORY = "C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions"

    os.chdir(REFACTORED_DIRECTORY)
    csv_file_path = "./data/ds_salaries.csv"

    DATASETS_DIR = "./data/"

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)
    # Use Pytest's assert statement to check if the file exists
    assert file_exists == True, f"The CSV file at '{csv_file_path}' does not exist."

def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)


if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])

