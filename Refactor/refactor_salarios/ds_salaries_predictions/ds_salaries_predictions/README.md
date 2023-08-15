# Data-Science-Job-Salaries Predective Model - Project Overview

The "Data Science Salaries" dataset provides valuable insights into the compensation trends and variations in the field of data science from 2020 to 2023. This dataset encompasses a comprehensive collection of salary information from various industries, organizations, and geographic regions, enabling data professionals, researchers, and organizations to analyze and understand the prevailing salary landscape in the data science domain during this four-year period. By examining this dataset, one can gain a deeper understanding of the factors influencing data science salaries, such as job roles, experience levels, educational backgrounds, and geographical locations. The dataset serves as a valuable resource for individuals seeking career guidance, companies aiming to benchmark their compensation strategies, and researchers investigating the evolving dynamics of the data science job market.

## Objective: Exploration and Modeling of Salary Trends in Data Science

The primary goal of this project is to conduct an in-depth analysis of the data contained in the "Data Science Salaries" dataset, with the aim of understanding salary trends and variations in the field of data science during the period from 2020 to 2023. Through this analysis, we aim to identify key factors influencing salaries of data professionals, such as job roles, experience, educational background, and geographical locations.

This project will be divided into two interconnected phases. In the first phase, we will perform a comprehensive exploratory data analysis, visualizing the distribution of salaries in relation to the independent variables, investigating temporal and geographical patterns, and uncovering correlations between professional attributes and salaries.

In the second phase, we will develop a regression model to predict the salaries of data science professionals. We will employ advanced machine learning techniques to train and fine-tune the model, considering the relative importance of the features identified in the previous phase. We will evaluate the model's performance using metrics such as Mean Absolute Error (MAE) and R-squared, refining the model to achieve more accurate predictions.

The outcomes of this project will provide valuable insights to individuals seeking career guidance in data science as well as companies aiming to establish competitive salary strategies. Additionally, it will contribute to the global understanding of changing dynamics in the data science job market and pave the way for future research in the realm of compensation and salary trends.

## Scope
This project represents a proof of concept aiming to develop a basic framework for a school project focused on salary prediction using dataset analysis. The scope intentionally includes minimal essential components to demonstrate the feasibility of predicting salaries based on the dataset. However, it should be noted that this proof of concept does not encompass an exhaustive development process and does not represent the most optimal approach to salary prediction. The primary objective is to provide a foundational understanding of the predictive modeling concept within the context of the dataset, serving as a starting point for further exploration and refinement.

## Requeriments
Please view the requirements.txt in the main directory


## Resources
* Data Source: The data used is in a csv file containing 3755 records and 11 features. 
  Available on Kaggle: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/

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

This dataset has undergone collaborative efforts involving a minimum of 14 individuals who have approached the task of salary prediction from diverse perspectives. As a result of this collective endeavor, a range of distinct ideas and methodologies have been explored. By virtue of this multi-faceted approach, the dataset offers a unique opportunity to discern and amalgamate the most advantageous insights and techniques, thereby enabling the synthesis of an integrated and refined predictive model. This amalgamation of viewpoints serves to enrich the overall predictive efficacy while encompassing a spectrum of innovative strategies derived from the collective experience and expertise of the contributing participants.
You can see the notebooks in the next link:

https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/code?datasetId=3125926


## Other models to use
Certainly, here are some other machine learning models that could be used for predicting salaries in addition to linear regression:

* Ridge and Lasso Regression: These are extensions of linear regression that handle multicollinearity and overfitting by adding regularization terms to the objective function. Ridge and Lasso can be useful when dealing with numerous features and aiming to prevent excessive model complexity.
* K-Nearest Neighbors (KNN) Regression: This model calculates predictions based on the values of the k nearest instances in the training set. It can be helpful when there are local patterns in the data that might not be captured by a global regression.
* Decision Trees and Random Forests: Decision trees split data into branches based on decision rules, and random forests consist of multiple trees. These models can handle nonlinear features and capture complex relationships.
* Support Vector Machines (SVM): SVMs can be used for both regression and classification. In the regression context, they seek to find a hyperplane that maximizes the margin between the data points and the regression line.
* Neural Networks: Neural networks can be very powerful for salary prediction, especially when dealing with large datasets. However, they can be more complex to configure and may require more data to avoid overfitting.
* Gradient Boosting and XGBoost: These models are ensemble techniques that combine multiple simpler models into a stronger model. They can handle nonlinear features and capture complex interactions.

## Summary of insights EDA:
* Most Data Science jobs require Senior-level/Expert experience level and very few positions are available for Executive-level/Directors.
* The most common job titles in the Data Science field are Data Scientist, Data Engineer, Data Analyst and Machine Learning Engineer.
* Most Data Science jobs are Full-time positions.
* Most Data Science employees and Companies are resident in the United States. However, the location where the highest average salary is paid is Russia; followed closely by the United States.
* The Number of Data Science jobs and the salary are increasing with each year and experience-level.
* Medium-sized and Large-sized companies pay high salaries in comparison to small-sized companies.
* The average salary for Data Science Jobs in USD is 112,297.87.


## Follow the instructions below to the notebook.

Run the existing notebook

1. Create a virtual Enviroment 

Install Python 3.10.9:
Download the latest version of Python 3.10.9 from the official Python website (https://www.python.org/downloads/). Make sure to check the "Add Python to PATH" option during installation.

Open Command Prompt:
Press Win + R, type "cmd," and press Enter to open the Windows Command Prompt.

Install virtualenv (optional but recommended):
You can install the virtualenv tool to create virtual environments more conveniently. In the command prompt, execute the following command to install virtualenv:

pip install virtualenv

Create a Directory for Your Project:
In the command prompt, navigate to the location where you want to create your project. You can use the cd command to change directories.

Create the Virtual Environment:
To create a virtual environment named "myenv," execute the following command:

python -m venv myenv

This will create a "myenv" directory containing the virtual environment.

Activate the Virtual Environment:
To activate the virtual environment, navigate to the "myenv" folder you just created in the command prompt and then run:

myenv\Scripts\activate

You'll notice that the command prompt changes, indicating that you're inside the virtual environment.

Install Packages:
With the virtual environment activated, you can install packages using pip just like you would outside the virtual environment.

Deactivate the Virtual Environment:
To deactivate the virtual environment and return to the global Python system, simply run:

deactivate

2. Install libraries

Run the following command to install the necesary libraries for the project.

pip install -r /requirements.txt

Verify the installation with this command:

pip freeze
   
