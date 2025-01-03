# Setup Instructions

## Prerequisites
- Python 3.8+
- Ollama installed (https://ollama.ai)

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce-llm-assistant.git
cd ecommerce-llm-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run the data preparation script:
```bash
python scripts/prepare_data.py
```

## Running the Demo

1. Start Jupyter notebook:
```bash
jupyter notebook
```

2. Open the `notebooks/demo.ipynb` file and follow the instructions to run the demo.

3. Run the test script to evaluate the model:
```bash
python scripts/test_model.py
```

