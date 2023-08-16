import os
import sys

from fastapi import FastAPI
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse

from .models.models import DSSalariesPrediction

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
    X = [ds_salaries_features.company_location,
         ds_salaries_features.company_location,
         ds_salaries_features.employee_residence,
         ds_salaries_features.employment_type,
         ds_salaries_features.employee_residence,
         ds_salaries_features.job_title]
    prediction = predictor.predict([X])
    return JSONResponse(f"Resultado predicción: {prediction}")