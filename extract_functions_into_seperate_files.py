import ast
import os

def extract_functions_from_file(filename):
    # Read the contents of the original Python file
    with open(filename, 'r') as f:
        source_code = f.read()

    # Parse the source code into an Abstract Syntax Tree (AST)
    tree = ast.parse(source_code)

    # Loop through all nodes in the AST to find function definitions
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            # Get the function name
            func_name = node.name
            
            # Generate the source code for the function
            function_code = ast.unparse(node)
            
            # Create a new file named after the function
            new_filename = f"{func_name}.py"
            with open(new_filename, 'w') as func_file:
                func_file.write(function_code)

def main():
    # Provide the filename of your giant Python file
    original_file = 'labs109.py'
    
    # Extract and store each function in separate files
    extract_functions_from_file(original_file)

if __name__ == "__main__":
    main()
