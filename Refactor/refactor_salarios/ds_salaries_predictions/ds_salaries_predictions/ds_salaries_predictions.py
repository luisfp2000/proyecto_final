"""Main module."""

from load.load_data import DataRetriever
from train.train_data import SalaryDataPipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import os
from sklearn.metrics import accuracy_score, roc_auc_score

DATASETS_DIR = './data/'
URL = 'https://raw.githubusercontent.com/luisfp2000/proyecto_final/main/Baseline/Dataset/ds_salaries.csv'



DROP_COLS = ['work_year','salary','salary_currency']
RETRIEVED_DATA = 'ds_salaries.csv'


SEED_SPLIT = 404
TRAIN_DATA_FILE = DATASETS_DIR + 'train.csv'
TEST_DATA_FILE  = DATASETS_DIR + 'test.csv'

TARGET = 'salary_in_usd'
FEATURES = []
NUMERICAL_VARS = ['remote_ratio','salary_in_usd']
CATEGORICAL_VARS = ['experience_level','employment_type','job_title' ,'employee_residence','company_location','company_size']


NUMERICAL_VARS_WITH_NA = []
CATEGORICAL_VARS_WITH_NA = []
NUMERICAL_NA_NOT_ALLOWED = [var for var in NUMERICAL_VARS if var not in NUMERICAL_VARS_WITH_NA]
CATEGORICAL_NA_NOT_ALLOWED = [var for var in CATEGORICAL_VARS if var not in CATEGORICAL_VARS_WITH_NA]


SEED_MODEL = 404

SELECTED_FEATURES = []

TRAINED_MODEL_DIR = './models/'
PIPELINE_NAME = 'linear_regression'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'



if __name__ == "__main__":
    
    print(os.getcwd())
    os.chdir('C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions/ds_salaries_predictions')
    
    # Retrieve data
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    result = data_retriever.retrieve_data()
    print(result)
    
    # Instantiate the SalaryDataPipeline class
    salary_data_pipeline = SalaryDataPipeline(seed_model=SEED_MODEL,
                                                numerical_vars=NUMERICAL_VARS, 
                                                categorical_vars_with_na=CATEGORICAL_VARS_WITH_NA,
                                                numerical_vars_with_na=NUMERICAL_VARS_WITH_NA,
                                                categorical_vars=CATEGORICAL_VARS,
                                                selected_features=SELECTED_FEATURES)
    
    # Read data
    df = pd.read_csv(DATASETS_DIR + RETRIEVED_DATA)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
                                                        df.drop(TARGET, axis=1),
                                                        df[TARGET],
                                                        test_size=0.2,
                                                        random_state=404
                                                   )
    
    
    linear_regression_model = salary_data_pipeline.fit_linear_regression(X_train, y_train)
    
    X_test = salary_data_pipeline.PIPELINE.fit_transform(X_test)
    y_pred = linear_regression_model.predict(X_test)
    
    class_pred = linear_regression_model.predict(X_test)
    proba_pred = linear_regression_model.predict_proba(X_test)[:,1]
    print(f'test roc-auc : {roc_auc_score(y_test, proba_pred)}')
    print(f'test accuracy: {accuracy_score(y_test, class_pred)}')
    
    # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(linear_regression_model, save_path)
    print(f"Model saved in {save_path}")
    