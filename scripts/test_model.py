import subprocess
from typing import List, Dict
import json

def query_model(prompt: str) -> str:
    """Query the Ollama model with a prompt."""
    cmd = ["ollama", "run", "techgear", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

def run_test_cases() -> List[Dict]:
    """Run a series of test cases and record results."""
    test_cases = [
        {
            "category": "Product Info",
            "query": "What are the specs of the TG-Phone Pro X?",
            "expected": "Contains: 6.7\" OLED, 256GB, 5G"
        },
        {
            "category": "Policy",
            "query": "What's your return policy for opened items?",
            "expected": "Contains: 14-day return window"
        },
        # Add more test cases
    ]
    
    results = []
    for test in test_cases:
        response = query_model(test["query"])
        results.append({
            "category": test["category"],
            "query": test["query"],
            "response": response,
            "expected": test["expected"]
        })
    
    return results

def main():
    results = run_test_cases()
    
    # Save test results
    with open("tests/test_results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
