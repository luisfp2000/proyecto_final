import os
import sys
import pandas as pd
import joblib

from fastapi import FastAPI
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse
from .models.models import DSSalariesPrediction
from load.load_data import DataRetriever
from train.train_data import SalaryDataPipeline
from sklearn.model_selection import train_test_split


DATASETS_DIR = './data/'
URL = 'https://raw.githubusercontent.com/luisfp2000/proyecto_final/main/Dataset/ds_salaries.csv'
PATH_COLS = "C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions/ds_salaries_predictions/models/train_data.csv"
    

DROP_COLS = ['work_year','salary','salary_currency','remote_ratio']
RETRIEVED_DATA = 'ds_salaries.csv'


TARGET = 'salary_in_usd'
FEATURES = []
NUMERICAL_VARS = ['salary_in_usd']
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
 

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    return 'DS Salaries Predictor is all ready to go!'


@app.post('/predict')
def extract_name(ds_salaries_features: DSSalariesPrediction):

    predictor = ModelPredictor("C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions/ds_salaries_predictions/models/linear_regression_output.pkl")
    
    X = [ds_salaries_features.experience_level,
         ds_salaries_features.employment_type,
         ds_salaries_features.job_title,
         ds_salaries_features.employee_residence,
         ds_salaries_features.company_location,
         ds_salaries_features.company_size,
         ds_salaries_features.remote_ratio]
    
    # Valores categóricos y numéricos del registro
    categorical_values = {
        'experience_level_'+ds_salaries_features.experience_level:      ds_salaries_features.experience_level,
        'employment_type_'+ds_salaries_features.employment_type:        ds_salaries_features.employment_type,
        'job_title_'+ds_salaries_features.job_title:                    ds_salaries_features.job_title,
        'employee_residence_'+ds_salaries_features.employee_residence:  ds_salaries_features.employee_residence,
        'company_location_'+ds_salaries_features.company_location:      ds_salaries_features.company_location,
        'company_size_'+ds_salaries_features.company_size:              ds_salaries_features.company_size,
        }

    remote_ratio = ds_salaries_features.remote_ratio/100

    pd_struct_to_model = pd.read_csv(PATH_COLS)

    # one-hot encoding columns
    column_names = pd_struct_to_model.columns.tolist()

    # call to function for obtain the dataframe with flags
    encoded_df = encode_categorical_values(remote_ratio, column_names, categorical_values)


    row_series = encoded_df.iloc[0]
    row_list = row_series.tolist()

    prediction = predictor.predict([row_list])
    
    return JSONResponse(f"Resultado predicción: {prediction} for data: {X}")


@app.get("/train_model", status_code=200)
def train_model():
    # Change location to the refactored directory
    os.chdir('C:/Users/luis.fernandez.COPPEL/LFPGit/proyectofinal/Refactor/refactor_salarios/ds_salaries_predictions/ds_salaries_predictions')
    
    # Retrieve data
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    result = data_retriever.retrieve_data()
    print(result)
    
    # Instantiate the SalaryDataPipeline class
    salary_data_pipeline = SalaryDataPipeline (seed_model=SEED_MODEL,
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
                                                   )
    

    linear_regression_model = salary_data_pipeline.fit_linear_regression(X_train, y_train)

       # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(linear_regression_model, save_path)
    print(f"Model saved in {save_path}")
    

    return "Trained model ready to go!"


    """
    Encodes categorical values into a one-hot encoded DataFrame row.

    Args:
        remote_ratio_value (float): The remote ratio value for the row.
        column_names (list): List of column names for the one-hot encoded DataFrame.
        categorical_values (dict): Dictionary containing categorical column names as keys and corresponding values.

    Returns:
        pandas.DataFrame: A DataFrame with the encoded row.
    """

def encode_categorical_values(remote_ratio_value, column_names, categorical_values):
    # Create a DF empty with the one-hot encoding
    encoded_df = pd.DataFrame(columns=column_names)
    
    row = [0] * len(column_names)

    row[0] = remote_ratio_value

    for col_name, value in categorical_values.items():
        if col_name in column_names:
            index = column_names.index(col_name)
            row[index] = 1
    
    encoded_df.loc[0] = row
    
    return encoded_df

