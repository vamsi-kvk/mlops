import unittest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from src.model_evaluation import ModelEvaluation
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

class TestModelEvaluation(unittest.TestCase):
    def setUp(self):
        self.config = load_config("config/config.yaml")
        self.model_evaluation = ModelEvaluation(self.config)
        self.model = RandomForestClassifier(**self.config['model']['hyperparameters'])
        iris = load_iris()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def test_evaluate_model(self):
        accuracy = self.model_evaluation.evaluate_model(self.model, self.X_test, self.y_test)
        self.assertGreaterEqual(accuracy, 0)

if __name__ == "__main__":
    unittest.main()