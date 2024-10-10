import unittest
from src.data_ingestion import DataIngestion
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

class TestDataIngestion(unittest.TestCase):
    def setUp(self):
        self.config = load_config("config/config.yaml")
        self.data_ingestion = DataIngestion(self.config)

    def test_load_data(self):
        data = self.data_ingestion.load_data()
        self.assertIsNotNone(data)

if __name__ == "__main__":
    unittest.main()