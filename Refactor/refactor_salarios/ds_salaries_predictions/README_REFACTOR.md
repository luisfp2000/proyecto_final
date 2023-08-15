# ITESM-MLOps-Project
This repository contains the files related to first part of the final proyect 

Student ID : A01688409

Student Name : Luis Fernandez Pérez

Teacher: Dr. Carlos Noé López Mejía

This project uses the following dataset : 

https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/

# Data-Science-Job-Salaries Predective Model - Project Overview

The "Data Science Salaries" dataset provides valuable insights into the compensation trends and variations in the field of data science from 2020 to 2023. This dataset encompasses a comprehensive collection of salary information from various industries, organizations, and geographic regions, enabling data professionals, researchers, and organizations to analyze and understand the prevailing salary landscape in the data science domain during this four-year period. By examining this dataset, one can gain a deeper understanding of the factors influencing data science salaries, such as job roles, experience levels, educational backgrounds, and geographical locations. The dataset serves as a valuable resource for individuals seeking career guidance, companies aiming to benchmark their compensation strategies, and researchers investigating the evolving dynamics of the data science job market.

**Features list**

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


## Scope
This project represents a proof of concept aiming to develop a basic framework for a school project focused on salary prediction using dataset analysis. The scope intentionally includes minimal essential components to demonstrate the feasibility of predicting salaries based on the dataset. However, it should be noted that this proof of concept does not encompass an exhaustive development process and does not represent the most optimal approach to salary prediction. The primary objective is to provide a foundational understanding of the predictive modeling concept within the context of the dataset, serving as a starting point for further exploration and refinement.


# About the project requirements and venv
This project was developed using Python 3.10.9 .

Check the **requirements.txt** file for information on the packages' versions used in the project.

Check the **requirements_extended.txt** file for information on all the packages' versions used in the development.

To create virtual environment and install requirements use the following lines

```
py -3.10 -m venv refactor_salarios

.\refactor_salarios\Scripts\activate

pip install -r requirements.txt
```

# Main file

The main file named *main.py* has all the functions needed to solve the objective. 

This file uses funcions from the modules in the project folders.

## Load Module

This module keeps the processes to import the dataset. 

We use a Dataset Copy of the original in a repo in git, because kaggle don´t have the raw data

The current functionality of this project is :
 
1. Download the dataset from the url from the 'https://raw.githubusercontent.com/luisfp2000/proyecto_final/main/Dataset/ds_salaries.csv'

1. Copy you local path to the dataset in the variable **FILE_PATH** in the *main.py* file

1. After using the load functionality in the *main.py* file , delete the dataset from the data folder in order to avoid commiting with file in the project. This project can't handle large files.

## Preprocess

This module keeps the transformations done to the dataset.

## Train 

This module holds the Pipeline to preprocess the dataset and the models methods that are going to be trained with the data.

## Models 

The main file export the trained model in this file to keep the results.

## Test

This module holds test to validate the functionalities in the other modules.

It has its own ReadMe

## Notebook

This folder keeps the original notebook