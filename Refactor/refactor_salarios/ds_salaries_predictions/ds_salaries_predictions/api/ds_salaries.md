# Demo Calculator-Fast-API
In this demo, you will be able to deploy a simple calculator with 4 basic operations (+, -, * and /) using Fast API.

## Setup
* Create a virtual environment with:
    ```bash
    python3 -m venv refactor_salarios
    ```

* Activate the virtual environment
    ```bash
    refactor_salarios/Scripts/activate
    ```

* Install the other libraries
Run the following command to install the libraries/packages.
    ```bash
    pip install -r requirements.txt
    ```

## Run FastAPI

* Change to the [ds_salaries_predictions](.) directory
* Run next command to start calculator api locally 
    ```bash
    uvicorn api.main:app --reload
    ```

## Checking endpoints
1. Access `http://127.0.0.1:8000/`, you will see a message like this `DS Salaries Predictor is all ready to go!`

2. Access `http://127.0.0.1:8000/docs`

3. Try running the predict endpoint by writing the values: 

{
  "experience_level": "Expert",
  "employment_type": "Full-Time",
  "job_title": "Principal Data Scientist",
  "employee_residence": "ES",
  "company_location": "ES",
  "company_size": "S",
  "remote_ratio": 50
}
The endpoint return the valor of prediction and the values used for that, you will see a message like this `"Resultado predicción: [136987.83103204] for data: ['Expert', 'Full_Time', 'Principal Data Scientist', 'ES', 'ES', 'S', 50.0]"`

4. Try running the predict endpoint, you will see a message like this `"Trained model ready to go!"`