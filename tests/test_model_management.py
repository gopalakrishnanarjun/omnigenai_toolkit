
# test_model_management.py
import unittest
from omnigenai_toolkit.model_management import download_model, fine_tune_model

class TestModelManagement(unittest.TestCase):
    def test_download_model(self):
        model_name = "bert-base-uncased"
        save_path = "./models"
        model, tokenizer = download_model(model_name, save_path)
        self.assertIsNotNone(model)
        self.assertIsNotNone(tokenizer)
    
    def test_fine_tune_model(self):
        model = "dummy_model"
        dataset_path = "data/train.csv"
        output_path = "./fine_tuned_model"
        epochs = 5
        result = fine_tune_model(model, dataset_path, output_path, epochs)
        self.assertIsNone(result)  # Expecting None since this is a placeholder

if __name__ == "__main__":
    unittest.main()
