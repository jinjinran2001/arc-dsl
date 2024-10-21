import ast
import re

def simple_unparse(node):
    if isinstance(node, ast.Call):
        args = ', '.join(simple_unparse(arg) for arg in node.args)
        return f"{node.func.id}({args})"
    elif isinstance(node, ast.Name):
        return node.id
    else:
        raise ValueError(f"Unexpected node type: {type(node)}")

def generate_subprograms(node):
    if isinstance(node, ast.Call):
        subprograms = [simple_unparse(node)]
        
        # Recursively generate subprograms for each argument
        for arg in node.args:
            subprograms.extend(generate_subprograms(arg))
        
        return subprograms
    elif isinstance(node, ast.Name):
        return []
    else:
        raise ValueError(f"Unexpected node type: {type(node)}")

def parse_function(func_str):
    # Remove the function definition and return statement
    func_body = re.search(r'return (.+)', func_str).group(1)
    
    # Parse the function body
    parsed_body = ast.parse(func_body).body[0].value
    
    return parsed_body

def sanitize_function_newlines(func_str):
    func_str = func_str.replace("\n", "")
    func_str = func_str.replace("):", "):\n")
    return func_str

def encase_funct(s):
    return f"def main(I):\n\treturn {s}"

# Example usage
func_str = """
def solve_2013d3e2(I):
    return tophalf(lefthalf(subgrid(first(objects(I, F, T, T)), I)))
"""

parsed_body = parse_function(func_str)
subprograms = generate_subprograms(parsed_body)

print("Sub-programs:")
for subprogram in subprograms:
    print(subprogram)

