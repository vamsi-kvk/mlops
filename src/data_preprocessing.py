import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys
from sklearn.preprocessing import StandardScaler


class DataPreprocessing:
    def __init__(self, config):
        self.config = config

    def preprocess_data(self, data):
        try:
            logging.debug("Debug: Starting data preprocessing")
            logging.info("Info: Preprocessing data")
            scaler = StandardScaler()
            data_scaled = scaler.fit_transform(data.drop('species', axis=1))
            data_scaled_df = pd.DataFrame(data_scaled, columns=data.columns[:-1])
            data_scaled_df['species'] = data['species'].values
            logging.info("Info: Data preprocessing completed successfully")
            return data_scaled_df
        except Exception as e:
            logging.error("Error: Error occurred during data preprocessing")
            logging.critical("Critical: This is a critical error in data preprocessing")
            raise CustomException(e, sys)
