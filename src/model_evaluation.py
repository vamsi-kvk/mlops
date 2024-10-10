from sklearn.metrics import accuracy_score
from src.logger import logging
from src.exception import CustomException
import sys


class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def evaluate_model(self, model, X_test, y_test):
        try:
            logging.debug("Debug: Starting model evaluation")
            logging.info("Info: Evaluating the model")
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            logging.info(f"Info: Model evaluation completed with accuracy: {accuracy}")
            return accuracy
        except Exception as e:
            logging.error("Error: Error occurred during model evaluation")
            logging.critical("Critical: This is a critical error in model evaluation")
            raise CustomException(e, sys)
