import yaml
from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessing
from src.model_training import ModelTraining
from src.model_evaluation import ModelEvaluation
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import sys
from dotenv import load_dotenv

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.info("Info: Configuration loaded successfully")
        return config
    except Exception as e:
        logging.error("Error: Error occurred while loading the configuration")
        logging.critical("Critical: This is a critical error in loading configuration")
        raise CustomException(e, sys)

def main():
    try:
        load_dotenv()  # Load environment variables from .env file if present

        logging.info("Info: Starting the main pipeline")
        config = load_config("config/config.yaml")

        # Data Ingestion
        data_ingestion = DataIngestion(config)
        raw_data = data_ingestion.load_data()

        # Data Preprocessing
        data_preprocessing = DataPreprocessing(config)
        processed_data = data_preprocessing.preprocess_data(raw_data)
        data_ingestion.save_data(processed_data)

        # Splitting the data
        X = processed_data.drop('species', axis=1)
        y = processed_data['species']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Model Training
        model_training = ModelTraining(config)
        model, cv_score = model_training.train_model(X_train, y_train)

        # Model Evaluation
        model_evaluation = ModelEvaluation(config)
        accuracy = model_evaluation.evaluate_model(model, X_test, y_test)
        logging.info(f"Info: Model Accuracy: {accuracy}")
        logging.info(f"Info: Cross-Validation Score: {cv_score}")

    except CustomException as e:
        logging.error("Error: An error occurred during the main execution")
        logging.critical("Critical: This is a critical error in the main execution")
        sys.exit(1)

if __name__ == "__main__":
    main()