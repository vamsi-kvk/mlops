import unittest
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from src.model_training import ModelTraining
import yaml


def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


class TestModelTraining(unittest.TestCase):
    def setUp(self):
        self.config = load_config("config/config.yaml")
        self.model_training = ModelTraining(self.config)
        iris = load_iris()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42)

    def test_train_model(self):
        model = self.model_training.train_model(self.X_train, self.y_train)
        self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()
