from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from src.logger import logging
from src.exception import CustomException
import sys
import numpy as np


class ModelTraining:
    def __init__(self, config):
        self.config = config

    def train_model(self, X_train, y_train):
        try:
            logging.debug("Debug: Starting model training with cross-validation")
            logging.info("Info: Training the model with cross-validation")
            model = RandomForestClassifier(**self.config['model']['hyperparameters'])
            cv_scores = cross_val_score(model, X_train, y_train, cv=5)
            logging.info(f"Info: Cross-validation scores: {cv_scores}")
            logging.info(f"Info: Mean cross-validation score: {np.mean(cv_scores)}")
            model.fit(X_train, y_train)
            logging.info("Info: Model training completed successfully")
            return model, np.mean(cv_scores)
        except Exception as e:
            logging.error("Error: Error occurred during model training")
            logging.critical("Critical: This is a critical error in model training")
            raise CustomException(e, sys)
