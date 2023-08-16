from pydantic import BaseModel


class DSSalariesPrediction (BaseModel):
    """
    Representa los atributos para poder realizar el pronostico del precio de la casa
    Attributes:
    experience_level
    employment_type
    job_title
    employee_residence
    company_location
    company_size,
    remote_ratio
    """
    experience_level: str
    employment_type:str
    job_title:str
    employee_residence:str
    company_location:str
    company_size:str
    remote_ratio:float

    