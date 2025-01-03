# E-commerce LLM Assistant

A demonstration of fine-tuning Large Language Models (LLMs) for e-commerce customer service using Ollama.

## Overview

This project showcases how to create custom-trained language models for e-commerce customer service applications. It demonstrates fine-tuning open-source LLMs to understand product catalogs, FAQs, and company policies, enabling accurate and context-aware customer support responses.


## Prerequisites

- Python 3.10+
- Ollama
- Required Python packages (see requirements.txt)

## Quick Start

1. Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Clone this repository:
```bash
git clone https://github.com/yourusername/ecommerce-llm-assistant.git
cd ecommerce-llm-assistant
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the demo:
```bash
python scripts/test_model.py
```

## Demo Contents

The demonstration includes:

- Sample e-commerce product catalog
- Common customer service scenarios
- Before/after comparison of responses
- Performance metrics

## Sample Use Cases

1. Product Information
```python
Query: "What are the specifications of the wireless earbuds?"
```

2. Return Policies
```python
Query: "How do I return a defective item?"
```

3. Shipping Information
```python
Query: "What are the shipping options to Europe?"
```

## Model Configuration

The project uses Ollama with Mistral/Llama2 as the base model. Custom knowledge is integrated through the modelfile:

```
FROM mistral
SYSTEM "You are a customer service assistant..."
# Additional configuration
```

## Data Preparation

Guidelines for preparing your own data:
1. Product catalog formatting
2. FAQ document structure
3. Policy document organization

See `docs/data_preparation.md` for detailed instructions.

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Ollama team for their excellent LLM deployment tool
- Mistral AI/Meta for the base models
- Contributors and testers