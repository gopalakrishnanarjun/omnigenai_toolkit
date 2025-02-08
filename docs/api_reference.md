# API Reference for OmniGenAI Toolkit

## Overview
The **OmniGenAI Toolkit** provides a collection of tools and utilities for building, deploying, and managing Generative AI applications. This document outlines the modules and their key functions, providing developers with a clear guide on how to use the package.

---

## Modules

### 1. `OmniGenAI_toolkit.model_management`
Provides tools for downloading, managing, and fine-tuning AI models.

#### **Functions**
- **`download_model(model_name: str, save_path: str)`**
  Downloads a pre-trained model from the specified repository.
  
  **Parameters:**
  - `model_name` (str): Name of the model to download.
  - `save_path` (str): Directory to save the downloaded model.

- **`fine_tune_model(model, dataset_path: str, output_path: str, epochs: int)`**
  Fine-tunes a pre-trained model on a custom dataset.
  
  **Parameters:**
  - `model`: The model to fine-tune.
  - `dataset_path` (str): Path to the dataset.
  - `output_path` (str): Directory to save the fine-tuned model.
  - `epochs` (int): Number of training epochs.

---

### 2. `OmniGenAI_toolkit.data_handling`
Includes utilities for preprocessing and handling datasets.

#### **Functions**
- **`clean_text(text: str)`**
  Cleans and normalizes text by removing unwanted characters and whitespace.
  
  **Parameters:**
  - `text` (str): Input text to be cleaned.

- **`extract_text_from_file(file_path: str)`**
  Extracts text from documents such as PDF or Word files.
  
  **Parameters:**
  - `file_path` (str): Path to the document.

---

### 3. `OmniGenAI_toolkit.interactive_interfaces`
Tools for building interactive interfaces using frameworks like Streamlit.

#### **Functions**
- **`create_chat_interface(model, title: str)`**
  Creates a chat interface for user interaction with an LLM.
  
  **Parameters:**
  - `model`: The model used for generating responses.
  - `title` (str): Title of the chat interface.

- **`deploy_app(app_code: str, platform: str)`**
  Deploys a web application to the specified platform.
  
  **Parameters:**
  - `app_code` (str): Code for the web application.
  - `platform` (str): Platform to deploy (e.g., Hugging Face Spaces).

---

### 4. `OmniGenAI_toolkit.multi_modal`
Handles multi-modal inputs such as text and images.

#### **Functions**
- **`process_text_and_image(text: str, image_path: str)`**
  Processes text and image inputs to generate a combined response.
  
  **Parameters:**
  - `text` (str): Input text.
  - `image_path` (str): Path to the image file.

---

### 5. `OmniGenAI_toolkit.rag`
Implements Retrieval-Augmented Generation (RAG) pipelines.

#### **Functions**
- **`generate_embeddings(text: str)`**
  Generates embeddings for a given text input.
  
  **Parameters:**
  - `text` (str): Input text.

- **`rag_pipeline(query: str, documents: list)`**
  Combines document retrieval with generative response generation.
  
  **Parameters:**
  - `query` (str): User query.
  - `documents` (list): List of documents for retrieval.

---

### 6. `OmniGenAI_toolkit.collaboration`
Provides tools for multi-agent collaboration and workflow automation.

#### **Functions**
- **`create_agent_workflow(agents: list, task: str)`**
  Defines a workflow for multiple agents to collaborate on a task.
  
  **Parameters:**
  - `agents` (list): List of agents participating in the workflow.
  - `task` (str): Task description.

- **`automate_task(agent, input_data)`**
  Automates a specific task using the specified agent.
  
  **Parameters:**
  - `agent`: The AI agent assigned to the task.
  - `input_data`: Data required for the task.

---

### 7. `OmniGenAI_toolkit.utils`
General-purpose utility functions.

#### **Functions**
- **`load_config(config_path: str)`**
  Loads configuration settings from a file.
  
  **Parameters:**
  - `config_path` (str): Path to the configuration file.

- **`log_event(event: str, log_path: str)`**
  Logs an event to a specified file.
  
  **Parameters:**
  - `event` (str): Event description.
  - `log_path` (str): Path to the log file.

---

## How to Use
1. Install the package:
   ```bash
   pip install OmniGenAI-toolkit
   ```

2. Import the modules and use the functions as needed:
   ```python
   from OmniGenAI_toolkit.model_management import download_model

   download_model("gpt-3.5-turbo", "./models")
   ```

3. Refer to the examples provided in the `examples/` directory for detailed use cases.

---

For more details, visit the [GitHub Repository](https://github.com/gopalakrishnanarjun/OmniGenAI-Toolkit.git).
