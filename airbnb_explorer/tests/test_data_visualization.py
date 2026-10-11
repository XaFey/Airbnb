#test data_visualization.py     
import pandas as pd
from src.visualization import Visualization as v
import os
import logging


# Set up logging for the test module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_Visualization():
    # Create a sample DataFrame
    data = {
        'id': [1, 62, 35],
        'name': ['Rainbow Lane', 'Sunset Boulevard', 'Ocean View'],
        'price': [1000, 89898, 4000]
    }
    #create DataFrame from the sample data
    df = pd.DataFrame(data)

    # Initialize the Visualization instance
    vis = v.__new__(v) 
    # Set the DataFrame and output directory for the Visualization instance
    vis.df = df
    # Initialize the output directory for saving plots
    vis.output_dir = "output"
    # Ensure the output directory exists
    vis.__init__("output")

    # Test the price distribution plot
    logger.info("Testing price distribution plot...")
    result = vis.plot_price_distribution(df)

    # Check if the plot was successfully created
    assert os.path.exists(os.path.join("output", "price_distribution.png")), "Plot file not found in the output directory."

