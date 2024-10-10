import unittest
import pandas as pd
from src.data_preprocessing import DataPreprocessing
import yaml


def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        self.config = load_config("config/config.yaml")
        self.data_preprocessing = DataPreprocessing(self.config)

    def test_preprocess_data(self):
        sample_data = pd.DataFrame({
            'sepal_length': [5.1, 4.9, 4.7],
            'sepal_width': [3.5, 3.0, 3.2],
            'petal_length': [1.4, 1.4, 1.3],
            'petal_width': [0.2, 0.2, 0.2],
            'species': [0, 0, 0]
        })
        processed_data = self.data_preprocessing.preprocess_data(sample_data)
        self.assertIsNotNone(processed_data)


if __name__ == "__main__":
    unittest.main()
