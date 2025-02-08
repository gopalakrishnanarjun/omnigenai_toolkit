
# test_interactive_interfaces.py
import unittest
from omnigenai_toolkit.interactive_interfaces import create_chat_interface, deploy_app

class TestInteractiveInterfaces(unittest.TestCase):
    def test_create_chat_interface(self):
        result = create_chat_interface("gpt-3.5-turbo", title="Test Chat Interface")
        self.assertIsNone(result)  # Expecting None as it's a Streamlit app
    
    def test_deploy_app(self):
        app_code = "app_code.py"
        platform = "huggingface"
        result = deploy_app(app_code, platform)
        self.assertIsNone(result)  # Placeholder for deployment logic

if __name__ == "__main__":
    unittest.main()
