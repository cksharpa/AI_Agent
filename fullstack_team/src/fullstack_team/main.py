#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from fullstack_team.crew import FullstackTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
I want to build a simple web application that recommends health supplements based on user 
inputs such as fitness goal, age, and budget. The system should allow users to select goals 
like muscle gain, weight loss, or immunity improvement. Based on the input, the application 
should suggest relevant products such as protein powders, vitamins, or supplements with brief 
descriptions. The frontend should provide a clean form interface and display recommendations clearly. 
The backend should expose APIs to process user input and return recommendations using predefined logic 
or rules. The application should be lightweight, fast, and easy to use. It should be built using Python, 
with a simple frontend and backend setup, and be easy to extend in the future.
"""

module_name = "supplementsRecommendation.py"

def run():
    """
    Run the full stack crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
    }

    # Create and run the crew
    result = FullstackTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()