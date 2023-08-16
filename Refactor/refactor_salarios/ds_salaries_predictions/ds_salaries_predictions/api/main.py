import os
import sys
import pandas as pd

from fastapi import FastAPI
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse
from train.train_data import SalaryDataPipeline
from .models.models import DSSalariesPrediction



NUMERICAL_VARS = ['remote_ratio']
CATEGORICAL_VARS = ['experience_level','employment_type','job_title' ,'employee_residence','company_location','company_size']
NUMERICAL_VARS_WITH_NA = []
SELECTED_FEATURES = []
CATEGORICAL_VARS_WITH_NA = []
NUMERICAL_NA_NOT_ALLOWED = [var for var in NUMERICAL_VARS if var not in NUMERICAL_VARS_WITH_NA]
CATEGORICAL_NA_NOT_ALLOWED = [var for var in CATEGORICAL_VARS if var not in CATEGORICAL_VARS_WITH_NA]
SEED_MODEL = 404

salary_data_pipeline = SalaryDataPipeline (seed_model=SEED_MODEL,
                                            numerical_vars=NUMERICAL_VARS, 
                                            categorical_vars_with_na=CATEGORICAL_VARS_WITH_NA,
                                            numerical_vars_with_na=NUMERICAL_VARS_WITH_NA,
                                            categorical_vars=CATEGORICAL_VARS,
                                            selected_features=SELECTED_FEATURES)



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

    #prediction = predictor.predict([X])
    
    #Dummy Value for the  test
    prediction = 123000

    return JSONResponse(f"Resultado predicción: {prediction} for data: {X}")