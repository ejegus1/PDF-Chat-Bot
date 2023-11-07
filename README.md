

# PDF ChatBot

Create a conversational chatbot that harnesses the capabilities of Langchain, a Python library designed for building Large Language Models (LLMs), and Streamlit, another Python library for creating web applications. This chatbot is specifically designed to interact with and provide information from your own collection of PDF documents. Users can engage in natural language conversations with the chatbot, which will retrieve and present relevant content, answers, or insights from the PDFs in response to their queries or requests.

**Note:** You must provide your own API key in the attached `.env` file.

## Getting Started

Before you begin, make sure you have the following software and dependencies installed:

### Prerequisites

- [Python 3.11](https://www.python.org/downloads/)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/download)

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the chatbot application, run the following command in your VS Code terminal:

```bash
streamlit run app.py
```

