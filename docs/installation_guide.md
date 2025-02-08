# Installation Guide for omnigenai_toolkit

The **omnigenai_toolkit** is a Python package designed to simplify the development and deployment of Generative AI applications. This guide will walk you through the steps to install the package and set up your environment.

---

## Prerequisites
Before you begin, ensure the following prerequisites are met:

1. **Python Version**: Python 3.7 or higher is required. You can check your Python version by running:
   ```bash
   python --version
   ```

2. **Package Manager**: Ensure `pip` is installed and updated:
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Virtual Environment (Optional but Recommended)**: Create and activate a virtual environment to isolate your dependencies:
   ```bash
   python -m venv OmniGenAI_env
   source OmniGenAI_env/bin/activate  # For Linux/Mac
   OmniGenAI_env\Scripts\activate   # For Windows
   ```

---

## Installation

### Step 1: Install from PyPI
The omnigenai_toolkit is available on PyPI and can be installed using `pip`:
```bash
pip install OmniGenAI-toolkit
```

### Step 2: Verify Installation
After installation, verify that the package is installed correctly:
```bash
python -m pip show OmniGenAI-toolkit
```
You should see details about the package, such as version, location, and dependencies.

---

## Optional Dependencies
Depending on your use case, you might need additional dependencies. Below are some common ones:

- **GPU Support**: If you're using a GPU for AI model training, install `torch` with GPU support:
  ```bash
  pip install torch --index-url https://download.pytorch.org/whl/cu117
  ```

- **Streamlit for Interactive Interfaces**:
  ```bash
  pip install streamlit
  ```

- **Document Handling**:
  ```bash
  pip install PyPDF2 python-docx
  ```

- **Web Scraping**:
  ```bash
  pip install beautifulsoup4 selenium
  ```

---

## Installing from Source
If you want the latest version or to contribute to development, you can install the package directly from the GitHub repository:

### Step 1: Clone the Repository
```bash
git clone https://github.com/gopalakrishnanarjun/OmniGenAI-toolkit.git
cd OmniGenAI-toolkit
```

### Step 2: Install the Package
```bash
pip install .
```

### Step 3: Install Development Dependencies (Optional)
If you're contributing to the package, install additional dependencies for testing and development:
```bash
pip install -r requirements-dev.txt
```

---

## Updating the Package
To update the package to the latest version, use:
```bash
pip install --upgrade OmniGenAI-toolkit
```

---

## Uninstallation
To uninstall the package, run:
```bash
pip uninstall OmniGenAI-toolkit
```

---

For further assistance or issues, please visit the [GitHub Repository](https://github.com/gopalakrishnanarjun/OmniGenAI-Toolkit.git) or open an issue. Happy coding!
