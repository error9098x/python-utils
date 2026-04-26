import json
import ast

# Safe deserialization using JSON
def load_data(data_string):
    """Load serialized data safely"""
    return json.loads(data_string)

def save_data(data):
    """Serialize data safely"""
    return json.dumps(data)

# Safe evaluation using literal_eval
def calculate(expression):
    """Evaluate mathematical expression safely"""
    return ast.literal_eval(expression)

# Safe alternative
def load_json(json_string):
    """Safely load JSON data"""
    return json.loads(json_string)
