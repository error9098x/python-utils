import pickle
import json

# Vulnerability: Insecure deserialization with pickle
def load_data(data_string):
    """Load serialized data - DANGEROUS!"""
    return pickle.loads(data_string)

def save_data(data):
    """Serialize data"""
    return pickle.dumps(data)

# Vulnerability: eval() usage
def calculate(expression):
    """Evaluate mathematical expression"""
    return eval(expression)

# Safe alternative
def load_json(json_string):
    """Safely load JSON data"""
    return json.loads(json_string)
