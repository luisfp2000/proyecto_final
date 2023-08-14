from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from preprocess.preprocess_data import MissingIndicator
from preprocess.preprocess_data import OneHotEncoder

class SalaryDataPipeline:
    """
    A class representing the DS_SAlary data processing and modeling pipeline.

    Attributes:
        NUMERICAL_VARS (list): A list of numerical variables in the dataset.
        CATEGORICAL_VARS_WITH_NA (list): A list of categorical variables with missing values.
        NUMERICAL_VARS_WITH_NA (list): A list of numerical variables with missing values.
        CATEGORICAL_VARS (list): A list of categorical variables in the dataset.
        SEED_MODEL (int): A seed value for reproducibility.

    Methods:
        create_pipeline(): Create and return the Titanic data processing pipeline.
    """
    
    def __init__(self, numerical_vars, 
                  categorical_vars):
        self.NUMERICAL_VARS = numerical_vars
        self.CATEGORICAL_VARS = categorical_vars

        
    def create_pipeline(self):
        """
        Create and return the Titanic data processing pipeline.

        Returns:
            Pipeline: A scikit-learn pipeline for data processing and modeling.
        """
        self.PIPELINE = Pipeline(
            [
                                ('missing_indicator', MissingIndicator(variables=self.NUMERICAL_VARS)),
                                ('dummy_vars', OneHotEncoder(variables=self.CATEGORICAL_VARS)),
                                ('scaling', MinMaxScaler()),
                              ]
        )
        return self.PIPELINE
    
    def fit_linear_regression(self, X_train, y_train):
        """
        Fit a Linear Regression model using the predefined data preprocessing pipeline.

        Parameters:
        - X_train (pandas.DataFrame or numpy.ndarray): The training input data.
        - y_train (pandas.Series or numpy.ndarray): The target values for training.

        Returns:
        - linear_regression_model (linear_regression): The fitted linear Regression model.
        """
        linear_regression = LinearRegression()

        pipeline = self.create_pipeline()
        pipeline.fit(X_train, y_train)
        
        linear_regression.fit(pipeline.transform(X_train), y_train)
        return linear_regression
    
    def transform_test_data(self, X_test):
        """
        Apply the data preprocessing pipeline on the test data.

        Parameters:
        - X_test (pandas.DataFrame or numpy.ndarray): The test input data.

        Returns:
        - transformed_data (pandas.DataFrame or numpy.ndarray): The preprocessed test data.
        """
        pipeline = self.create_pipeline()
        return pipeline.transform(X_test)