import os
import json
from typing import List, Dict

def format_training_example(question: str, answer: str) -> str:
    """Format a Q&A pair into training format."""
    return f"<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n{answer}<|im_end|>\n"

def create_training_data() -> List[Dict]:
    """Create training examples from product catalog and policies."""
    training_data = []
    
    # Example training pairs
    examples = [
        {
            "question": "What's the price of the TG-Phone Pro X?",
            "answer": "The TG-Phone Pro X is priced at $899. It features a 6.7\" OLED display, 256GB storage, and is 5G capable."
        },
        {
            "question": "What's your return policy?",
            "answer": "We offer a 30-day return window for unopened items and a 14-day return window for opened items. Return shipping is paid by the customer, and refunds are processed within 5 business days."
        },
        # Add more examples as needed
    ]
    
    for example in examples:
        training_data.append(format_training_example(example["question"], example["answer"]))
    
    return training_data

def main():
    training_data = create_training_data()
    
    # Save formatted training data
    output_dir = "data/training"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/training_data.jsonl", "w") as f:
        for example in training_data:
            f.write(json.dumps({"text": example}) + "\n")

if __name__ == "__main__":
    main()
