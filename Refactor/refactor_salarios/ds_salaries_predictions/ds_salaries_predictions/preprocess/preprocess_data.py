from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array
import pandas as pd
import re
import numpy as np

class MissingIndicator(BaseEstimator, TransformerMixin):
    """
    Custom scikit-learn transformer to create indicator features for missing values in specified variables.

    Parameters:
        variables (list or str, optional): List of column names (variables) to create indicator features for.
            If a single string is provided, it will be treated as a single variable. Default is None.

    Attributes:
        variables (list): List of column names (variables) to create indicator features for.

    Methods:
        fit(X, y=None):
            This method does not perform any actual training or fitting.
            It returns the transformer instance itself.

        transform(X):
            Creates indicator features for missing values in the specified variables and returns the modified DataFrame.

    Example usage:
    ```
    from sklearn.pipeline import Pipeline

    # Instantiate the custom transformer
    missing_indicator = MissingIndicator(variables=['age', 'income'])

    # Define the pipeline with the custom transformer
    pipeline = Pipeline([
        ('missing_indicator', missing_indicator),
        # Other pipeline steps...
    ])

    # Fit and transform the data using the pipeline
    X_transformed = pipeline.fit_transform(X)
    ```
    """
    def __init__(self, variables=None):
        """
        Initialize the MissingIndicator transformer.

        Parameters:
            variables (list or str, optional): List of column names (variables) to create indicator features for.
                If a single string is provided, it will be treated as a single variable. Default is None.
        """
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        """
        This method does not perform any actual training or fitting, as indicator features are created based on data.
        It returns the transformer instance itself.

        Parameters:
            X (pd.DataFrame): Input data to be transformed. Not used in this method.
            y (pd.Series or np.array, optional): Target variable. Not used in this method.

        Returns:
            self (MissingIndicator): The transformer instance.
        """
        return self

    def transform(self, X):
        """
        Creates indicator features for missing values in the specified variables and returns the modified DataFrame.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            X_transformed (pd.DataFrame): Transformed DataFrame with additional indicator features for missing values.
        """
        X = X.copy()
        for var in self.variables:
            X[f'{var}_nan'] = X[var].isnull().astype(int)

        return X
    
    """
    Custom scikit-learn transformer to impute missing values in numerical variables.

    Parameters:
        variables (list or str, optional): List of column names (variables) to impute missing values for.
            If a single string is provided, it will be treated as a single variable. Default is None.

    Attributes:
        variables (list): List of column names (variables) to impute missing values for.
        median_dict_ (dict): Dictionary to store the median values for each specified numerical variable during fitting.

    Methods:
        fit(X, y=None):
            Calculates the median values for the specified numerical variables from the training data.
            It returns the transformer instance itself.

        transform(X):
            Imputes missing values in the specified numerical variables using the median values and returns the modified DataFrame.

    Example usage:
    ```
    from sklearn.pipeline import Pipeline

    # Instantiate the custom transformer
    imputer = NumericalImputer(variables=['age', 'income'])

    # Define the pipeline with the custom transformer
    pipeline = Pipeline([
        ('imputer', imputer),
        # Other pipeline steps...
    ])

    # Fit and transform the data using the pipeline
    X_transformed = pipeline.fit_transform(X)
    ```
    """
    def __init__(self, variables=None):
        """
        Initialize the NumericalImputer transformer.

        Parameters:
            variables (list or str, optional): List of column names (variables) to impute missing values for.
                If a single string is provided, it will be treated as a single variable. Default is None.
        """
        self.variables = [variables] if not isinstance(variables, list) else variables

    def fit(self, X, y=None):
        """
        Calculates the median values for the specified numerical variables from the training data.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            self (NumericalImputer): The transformer instance.
        """
        self.median_dict = {}
        for var in self.variables:
            self.median_dict[var] = X[var].median()
        return self


    def transform(self, X):
        """
        Imputes missing values in the specified numerical variables using the median values and returns the modified DataFrame.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            X_transformed (pd.DataFrame): Transformed DataFrame with missing values imputed for the specified numerical variables.
        """
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].fillna(self.median_dict[var])
        return X
    
    """
    Custom scikit-learn transformer to encode rare categories in categorical variables.

    Parameters:
        tol (float, optional): The tolerance level to define rare categories.
            Categories with a frequency lower than tol will be encoded as 'rare'.
            Default is 0.05.
        variables (list or str, optional): List of column names (variables) to encode rare categories for.
            If a single string is provided, it will be treated as a single variable. Default is None.

    Attributes:
        tol (float): The tolerance level to define rare categories.
        variables (list): List of column names (variables) to encode rare categories for.
        rare_labels_dict (dict): Dictionary to store the rare category labels for each specified categorical variable during fitting.

    Methods:
        fit(X, y=None):
            Calculates the rare category labels for the specified categorical variables from the training data.
            It returns the transformer instance itself.

        transform(X):
            Encodes rare categories in the specified categorical variables and returns the modified DataFrame.

    Example usage:
    ```
    from sklearn.pipeline import Pipeline

    # Instantiate the custom transformer
    encoder = RareLabelCategoricalEncoder(tol=0.1, variables=['category1', 'category2'])

    # Define the pipeline with the custom transformer
    pipeline = Pipeline([
        ('encoder', encoder),
        # Other pipeline steps...
    ])

    # Fit and transform the data using the pipeline
    X_transformed = pipeline.fit_transform(X)
    ```
    """
    def __init__(self, tol=0.05, variables=None):
        """
        Initialize the RareLabelCategoricalEncoder transformer.

        Parameters:
            tol (float, optional): The tolerance level to define rare categories.
                Categories with a frequency lower than tol will be encoded as 'rare'.
                Default is 0.05.
            variables (list or str, optional): List of column names (variables) to encode rare categories for.
                If a single string is provided, it will be treated as a single variable. Default is None.
        """
        self.tol = tol
        self.variables = [variables] if not isinstance(variables, list) else variables

    def fit(self, X, y=None):
        """
        Calculates the rare category labels for the specified categorical variables from the training data.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            self (RareLabelCategoricalEncoder): The transformer instance.
        """
        self.rare_labels_dict = {}
        for var in self.variables:
            t = pd.Series(X[var].value_counts() / float(X.shape[0]))
            self.rare_labels_dict[var] = list(t[t<self.tol].index)
        return self

    def transform(self, X):
        """
        Encodes rare categories in the specified categorical variables and returns the modified DataFrame.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            X_transformed (pd.DataFrame): Transformed DataFrame with rare categories encoded for the specified categorical variables.
        """
        X = X.copy()
        for var in self.variables:
            X[var] = np.where(X[var].isin(self.rare_labels_dict[var]), 'rare', X[var])
        return X  
class OneHotEncoder(BaseEstimator, TransformerMixin):
    """
    Custom scikit-learn transformer to perform one-hot encoding for categorical variables.

    Parameters:
        variables (list or str, optional): List of column names (variables) to perform one-hot encoding for.
            If a single string is provided, it will be treated as a single variable. Default is None.

    Attributes:
        variables (list): List of column names (variables) to perform one-hot encoding for.
        dummies (list): List of column names representing the one-hot encoded dummy variables.

    Methods:
        fit(X, y=None):
            Calculates the one-hot encoded dummy variable columns for the specified categorical variables from the training data.
            It returns the transformer instance itself.

        transform(X):
            Performs one-hot encoding for the specified categorical variables and returns the modified DataFrame.

    Example usage:
    ```
    from sklearn.pipeline import Pipeline

    # Instantiate the custom transformer
    encoder = OneHotEncoder(variables=['category1', 'category2'])

    # Define the pipeline with the custom transformer
    pipeline = Pipeline([
        ('encoder', encoder),
        # Other pipeline steps...
    ])

    # Fit and transform the data using the pipeline
    X_transformed = pipeline.fit_transform(X)
    ```
    """
    def __init__(self, variables=None):
        """
        Initialize the OneHotEncoder transformer.

        Parameters:
            variables (list or str, optional): List of column names (variables) to perform one-hot encoding for.
                If a single string is provided, it will be treated as a single variable. Default is None.
        """
        self.variables = [variables] if not isinstance(variables, list) else variables

    def fit(self, X, y=None):
        """
        Calculates the one-hot encoded dummy variable columns for the specified categorical variables from the training data.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            self (OneHotEncoder): The transformer instance.
        """
        self.dummies = pd.get_dummies(X[self.variables], drop_first=True).columns
        return self

    def transform(self, X):
        """
        Performs one-hot encoding for the specified categorical variables and returns the modified DataFrame.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            X_transformed (pd.DataFrame): Transformed DataFrame with one-hot encoded dummy variables for the specified categorical variables.
        """
        X = X.copy()
        X = pd.concat([X, pd.get_dummies(X[self.variables], drop_first=True)], axis=1)
        X.drop(self.variables, axis=1)

        # Adding missing dummies, if any
        missing_dummies = [var for var in self.dummies if var not in X.columns]
        if len(missing_dummies) != 0:
            for col in missing_dummies:
                X[col] = 0

        return X

