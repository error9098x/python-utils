import os
import subprocess
import pickle

# Vulnerability 1: Command injection via os.system
def run_command(user_input):
    """Execute a system command - DANGEROUS!"""
    command = f"ls {user_input}"
    os.system(command)

# Vulnerability 2: Command injection via subprocess
def execute_script(script_name):
    """Run a script file"""
    subprocess.call(f"python {script_name}", shell=True)

# Safe function for comparison
def list_directory(path):
    """Safely list directory contents"""
    return os.listdir(path)
