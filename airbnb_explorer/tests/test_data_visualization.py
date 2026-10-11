#test data_visualization.py     
import pandas as pd
from src.visualization import Visualization as v
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def test_Visualization():
    # Create a sample DataFrame
    data = {
        'id': [1, 62, 35],
        'name': ['Rainbow Lane', 'Sunset Boulevard', 'Ocean View'],
        'price': [1000, 89898, 4000]
    }
    df = pd.DataFrame(data)

    vis = v.__new__(v) 
    vis.df = df
    vis.output_dir = "output"  
    vis.__init__("output")

    logger.info("Testing price distribution plot...")
    result = vis.plot_price_distribution(df)

    assert os.path.exists(os.path.join("output", "price_distribution.png")), "Plot file not found in the output directory."

    assert result == True, "Visualization method failed to generate the plot."

