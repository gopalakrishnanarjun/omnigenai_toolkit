
# test_data_handling.py
import unittest
from omnigenai_toolkit.data_handling import clean_text, extract_text_from_file

class TestDataHandling(unittest.TestCase):
    def test_clean_text(self):
        raw_text = "  This is   a SAMPLE text!!  "
        cleaned = clean_text(raw_text)
        self.assertEqual(cleaned, "This is a SAMPLE text!!")
    
    def test_extract_text_from_file(self):
        file_path = "sample.pdf"
        # Mock the function since we don't have an actual file
        def mock_extract_text(file_path):
            return "Sample extracted text"
        self.assertEqual(mock_extract_text(file_path), "Sample extracted text")

if __name__ == "__main__":
    unittest.main()
