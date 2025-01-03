import unittest
import subprocess
import json
from typing import Dict, List, Optional

class TestModelResponses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize test data and model."""
        # Load test cases
        cls.test_cases = cls.load_test_cases()
        
    def query_model(self, prompt: str) -> str:
        """Query the Ollama model with a prompt."""
        cmd = ["ollama", "run", "techgear", prompt]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    @staticmethod
    def load_test_cases() -> List[Dict]:
        """Load test cases from JSON file."""
        return [
            {
                "category": "Product Info",
                "query": "What are the specs of the TG-Phone Pro X?",
                "required_elements": ["6.7", "OLED", "256GB", "5G"],
                "forbidden_elements": ["TG-Phone Lite", "TG-Book"]
            },
            {
                "category": "Returns",
                "query": "What's your return policy for unopened items?",
                "required_elements": ["30-day", "return"],
                "forbidden_elements": ["14-day"]
            },
            {
                "category": "Shipping",
                "query": "How much is express shipping?",
                "required_elements": ["$15", "1-2 business days"],
                "forbidden_elements": ["free"]
            },
            {
                "category": "Warranty",
                "query": "What's covered under warranty?",
                "required_elements": ["1-year", "manufacturing defects"],
                "forbidden_elements": ["software issues"]
            }
        ]

    def validate_response(self, response: str, required: List[str], forbidden: Optional[List[str]] = None) -> bool:
        """
        Validate if response contains required elements and doesn't contain forbidden ones.
        """
        if forbidden is None:
            forbidden = []
            
        # Check for required elements
        for element in required:
            self.assertIn(element.lower(), response.lower(), 
                         f"Response should contain '{element}'")
            
        # Check for forbidden elements
        for element in forbidden:
            self.assertNotIn(element.lower(), response.lower(), 
                           f"Response should not contain '{element}'")
        
        return True

    def test_responses(self):
        """Test model responses for various scenarios."""
        for test_case in self.test_cases:
            with self.subTest(category=test_case["category"]):
                response = self.query_model(test_case["query"])
                self.validate_response(
                    response,
                    test_case["required_elements"],
                    test_case.get("forbidden_elements", [])
                )

    def test_response_length(self):
        """Test that responses are reasonably sized."""
        for test_case in self.test_cases:
            with self.subTest(category=test_case["category"]):
                response = self.query_model(test_case["query"])
                # Response should be between 20 and 500 characters
                self.assertTrue(20 <= len(response) <= 500,
                              "Response length should be reasonable")

    def test_unknown_queries(self):
        """Test model behavior with out-of-scope queries."""
        unknown_queries = [
            "What's the weather like today?",
            "Can you write me a poem?",
            "What's the capital of France?"
        ]
        
        for query in unknown_queries:
            with self.subTest(query=query):
                response = self.query_model(query)
                self.assertIn(
                    "cannot" or "unable" or "don't" or "only" or "specifically",
                    response.lower(),
                    "Model should acknowledge limitations for out-of-scope queries"
                )

if __name__ == '__main__':
    unittest.main(verbosity=2)
