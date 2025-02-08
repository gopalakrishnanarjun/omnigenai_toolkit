
# test_multi_modal.py
import unittest
from omnigenai_toolkit.multi_modal import process_text_and_image

class TestMultiModal(unittest.TestCase):
    def test_process_text_and_image(self):
        text = "Describe this image:"
        image_path = "example.jpg"
        result = process_text_and_image(text, image_path)
        self.assertEqual(result, f"Processed text: {text} and image: {image_path}")

if __name__ == "__main__":
    unittest.main()
