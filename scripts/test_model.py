import subprocess
import json
from pathlib import Path

def test_model():
    print("Testing TechGear AI Assistant...\n")
    
    # Test queries to verify different capabilities
    test_queries = [
        "What are the specifications of the TG-Phone Pro X?",
        "What's your return policy for electronics?",
        "Do you offer international shipping?",
    ]
    
    try:
        for query in test_queries:
            print(f"\n🔹 Testing query: {query}")
            print("-" * 100)
            
            # Run ollama command and capture output
            result = subprocess.run(
                ["ollama", "run", "techgear", query],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("Response:")
                print(result.stdout.strip())
            else:
                print("❌ Error running query:")
                print(result.stderr)
                return False
            
            print("-" * 50)
            
        print("\n✅ All test queries completed successfully!")
        return True
        
    except FileNotFoundError:
        print("\n❌ Error: Ollama not found. Please make sure Ollama is installed and accessible in your PATH")
        return False
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        return False

if __name__ == "__main__":
    test_model()
