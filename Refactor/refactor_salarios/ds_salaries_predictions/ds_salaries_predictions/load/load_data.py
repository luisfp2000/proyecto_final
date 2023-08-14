import pandas as pd
import numpy as np
import re
import os

class DataRetriever:
    """
    A class for retrieving data from a given URL and processing it for further analysis.

    Parameters:
        url (str): The URL from which the data will be loaded.

    Attributes:
        url (str): The URL from which the data will be loaded.

    Example usage:
    ```
    URL = 'https://raw.githubusercontent.com/luisfp2000/proyecto_final/main/Baseline/Dataset/ds_salaries.csv'
    data_retriever = DataRetriever(URL)
    result = data_retriever.retrieve_data()
    print(result)
    ```
    """

    DROP_COLS = ['work_year','salary','salary_currency']
    DATASETS_DIR = './data/'  # Directory where data will be saved.
    RETRIEVED_DATA = 'ds_salaries.csv'  # File name for the retrieved data.

    def __init__(self, url, data_path):
        self.url = url
        self.DATASETS_DIR = data_path

    def _get_employment_type_desc(self, employee):
        """
        Helper function to extract the employment type description

        Parameters:
            employee (str): The type of employment for the role.

        Returns:
            str: The employment type description extracted from the employment type.
        """
        line = employee
        if re.search('PT', line):
            return 'Part_time'
        elif re.search('FT', line):
            return 'Full_time'
        elif re.search('CT', line):
            return 'Contract'
        elif re.search('FL', line):
            return 'Freelance'
        else:
            return 'Other'

    def _get_level(self, employee):
        """
        Helper function to extract the level from a employee's experence

        Parameters:
            employee (str): The level description of the employee.

        Returns:
            str: The level description extracted from the level's experence.
        """
        line = employee
        if re.search('EN', line):
            return 'Junior'
        elif re.search('MI', line):
            return 'Intermediate'
        elif re.search('SE', line):
            return 'Expert'
        elif re.search('EX', line):
            return 'Director'
        else:
            return 'Other'


    def retrieve_data(self):
        """
        Retrieves data from the specified URL, processes it, and stores it in a CSV file.

        Returns:
            str: A message indicating the location of the stored data.
        """
        # Loading data from specific URL
        data = pd.read_csv(self.url)

        # Uncovering missing data
        data.replace('?', np.nan, inplace=True)
        data['salary'] = data['salary'].astype('float')
        data['salary_in_usd'] = data['salary_in_usd'].astype('float')
        data['remote_ratio'] = data['remote_ratio'].astype('float')
        data['work_year'] = data['work_year'].astype('float')
        

        # Extract the first cabin | Extract the title from 'name'

        data['employment_type'] = data['employment_type'].apply(self._get_employment_type_desc)
        data['experience_level'] = data['experience_level'].apply(self._get_level)

        # Drop irrelevant columns
        data.drop(self.DROP_COLS, axis=1, inplace=True)

        # Create directory if it does not exist
        if not os.path.exists(self.DATASETS_DIR):
            os.makedirs(self.DATASETS_DIR)
            print(f"Directory '{self.DATASETS_DIR}' created successfully.")
        else:
            print(f"Directory '{self.DATASETS_DIR}' already exists.")

        # Save data to CSV file
        data.to_csv(self.DATASETS_DIR + self.RETRIEVED_DATA, index=False)

        return f'Data stored in {self.DATASETS_DIR + self.RETRIEVED_DATA}'
    