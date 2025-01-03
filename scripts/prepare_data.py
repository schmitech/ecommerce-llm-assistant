import os
import json
from pathlib import Path

def prepare_data():
    print("Starting data preparation...")
    
    # Get project root directory
    root_dir = Path(__file__).parent.parent
    data_dir = root_dir / 'data' / 'sample'
    
    # Check if required files exist
    required_files = ['products.txt', 'faq.txt', 'policies.txt']
    for file in required_files:
        file_path = data_dir / file
        if not file_path.exists():
            print(f"Error: Required file {file} not found in {data_dir}")
            return False
        print(f"✓ Found {file}")
    
    try:
        # Read and validate files
        for file in required_files:
            with open(data_dir / file, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.strip():
                    print(f"Warning: {file} appears to be empty")
                else:
                    print(f"✓ Successfully validated {file}")
        
        print("\nData preparation completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error during data preparation: {str(e)}")
        return False

if __name__ == "__main__":
    prepare_data()
