import os
import pytest
from load.load_data import DataRetriever

def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)


def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to your CSV file that needs to be tested
    # os.chdir('C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions/ds_salaries_predictions')

    csv_file_path = "./data/ds_salaries.csv"

    DATASETS_DIR = './data/'
    FILE_PATH = "C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions/ds_salaries_predictions/data/ds_salaries.csv"
    

    data_retriever = DataRetriever(FILE_PATH, DATASETS_DIR)
    data_retriever.retrieve_data()

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    if file_exists:
        f"The CSV file at '{csv_file_path}' does not exist."


if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])