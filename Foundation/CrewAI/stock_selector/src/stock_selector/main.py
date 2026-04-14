#!/usr/bin/env python
import warnings
import os
from datetime import datetime

from stock_selector.crew import StockSelector

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """Run the Stock Selector crew."""

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    inputs = {
        "sector": "Technology",
        "current_date": datetime.now().isoformat()
    }

    # Execute crew
    result = StockSelector().crew().kickoff(inputs=inputs)

    # Display result
    print("\n=== FINAL STOCK SELECTION ===\n")
    print(result.raw)
