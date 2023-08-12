# Data-Science-Job-Salaries Predective Model - Project Overview
The purpose of this project is to explore every feature in the Dataset to uncover insights and make a predictive model for predict the salary for Data Scientist Roles.
## Requeriments

## Resources
* Data Source: The data used is in a csv file containing 607 records and 12 features. 
  Available on Kaggle: https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

To conduct this analysis, a dataset containing relevant information about Data Scientists was used. The dataset includes the following variables:

1. `work_year`: The year the salary was paid.
2. `experience_level`: The experience level in the job during the year.
    - `EN` > Entry-level / Junior
    - `MI` > Mid-level / Intermediate
    - `SE` > Senior-level / Expert
    - `EX` > Executive-level / Director
3. `employment_type`: The type of employment for the role.
    - `PT` > Part-time
    - `FT` > Full-time
    - `CT` > Contract
    - `FL` > Freelance
4. `job_title`: The role worked in during the year.
5. `salary`: The total gross salary amount paid.
6. `salary_currency`: The currency of the salary paid as an ISO 4217 currency code.
7. `salaryinusd`: The salary in USD.
8. `employee_residence`: Employee's primary country of residence during the work year as an ISO 3166 country code.
9. `remote_ratio`: The overall amount of work done remotely.
10. `company_location`: The country of the employer's main office or contracting branch.
11. `company_size`: The median number of people that worked for the company during the year.


## Summary of insights EDA:
* Most Data Science jobs require Senior-level/Expert experience level and very few positions are available for Executive-level/Directors.
* The most common job titles in the Data Science field are Data Scientist, Data Engineer, Data Analyst and Machine Learning Engineer.
* Most Data Science jobs are Full-time positions.
* Most Data Science employees and Companies are resident in the United States. However, the location where the highest average salary is paid is Russia; followed closely by the United States.
* The Number of Data Science jobs and the salary are increasing with each year and experience-level.
* Medium-sized and Large-sized companies pay high salaries in comparison to small-sized companies.
* The average salary for Data Science Jobs in USD is 112,297.87.


Follow the instructions below to the notebook.
### Run the existing notebook

1. Create a virtual environment with `Python 3.10.9`
    * Create venv
        ```
        python3 -m venv venv
        ```

    * Activate the virtual environment

        ```
        source venv/bin/activate
        ```

2. Install libraries
    Run the following command to install the necesary libraries for the project.

    ```bash
    pip install -r /requirements.txt
    ```
    Verify the installation with this command:
    ```bash
    pip freeze
    ```
    
    
