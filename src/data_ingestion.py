import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def load_data(self):
        try:
            logging.debug("Debug: Starting to load raw data")
            logging.info("Info: Loading raw data")
            data = pd.read_csv(self.config['data']['raw_data_path'])
            logging.info("Info: Raw data loaded successfully")
            return data
        except Exception as e:
            logging.error("Error: Error occurred while loading raw data")
            logging.critical("Critical: This is a critical error in loading data")
            raise CustomException(e, sys)

    def save_data(self, data):
        try:
            logging.debug("Debug: Starting to save processed data")
            logging.info("Info: Saving processed data")
            data.to_csv(self.config['data']['processed_data_path'], index=False)
            logging.info("Info: Processed data saved successfully")
        except Exception as e:
            logging.error("Error: Error occurred while saving processed data")
            logging.critical("Critical: This is a critical error in saving data")
            raise CustomException(e, sys)