#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from coding_assistant.crew import Coding_Assistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

assignment = 'Write a Python program to compute the nth Fibonacci number using matrix exponentiation.'

def run():
    """
    Run the crew.
    """
    inputs = {
        'assignment': assignment,
    }
    
    result = Coding_Assistant().crew().kickoff(inputs=inputs)
    print(result.raw)
