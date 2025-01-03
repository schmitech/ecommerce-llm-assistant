#!/bin/bash

# Function to print colored output
print_step() {
    echo -e "\n\033[1;36m=== $1 ===\033[0m\n"
}

print_success() {
    echo -e "\033[1;32m✓ $1\033[0m"
}

print_command() {
    echo -e "\033[1;33m$ $1\033[0m"
}

# Clear screen for demo
clear

print_step "Cleaning up existing models"
print_command "ollama list"
ollama list
print_command "ollama rm techgear"
ollama rm techgear

print_step "Creating TechGear Assistant"
print_command "ollama create techgear -f models/modelfiles/techgear.ollama"
ollama create techgear -f models/modelfiles/techgear.ollama
print_success "Model created successfully"

print_step "Preparing Data"
print_command "python scripts/prepare_data.py"
python scripts/prepare_data.py

print_step "Running Test Queries"
print_command "python scripts/test_model.py"
python scripts/test_model.py

print_step "Demo Complete!"
echo -e "\nYou can now:"
echo "1. Try additional queries manually"
echo "2. Run 'jupyter notebook notebooks/demo.ipynb' for interactive demo"
echo "3. Run 'ollama rm techgear' to clean up" 