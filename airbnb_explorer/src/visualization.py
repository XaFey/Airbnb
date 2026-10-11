import plotly.express as px
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Visualization:
    def __init__(self, output_dir = os.path.join("data", "plots")):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def plot_price_distribution(self, df):
        try:
            if 'price' not in df.columns:
                raise ValueError("The dataframe does not contain a 'price' column.")
            plot_df = df.dropna(subset=['price'])
            plot_df = plot_df[plot_df['price'] > 0]
            fig = px.histogram(plot_df, x='price', nbins=50, title='Price Distribution')
            output_file = os.path.join(self.output_dir, "price_distribution.png")
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            fig.write_image(output_file, format='png', width=800, height=600)
            logger.info(f"Price distribution plot saved to {output_file}")
            return True
        except Exception as e:
            # Log the error and return False if an exception occurs
            logger.error(f"Error in plot_price_distribution: {e}")
            return False
    def plot_neighborhood_distribution(self, df):
        try:
            if 'neighborhood' not in df.columns:
                raise ValueError("The dataframe does not contain a 'neighborhood' column.")
            plot_df = df.dropna(subset=['neighborhood'])
            fig = px.histogram(plot_df, x='neighborhood', title='Neighborhood Distribution')
            output_file = os.path.join(self.output_dir, "neighborhood_distribution.png")
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            fig.write_image(output_file, format='png', width=800, height=600)
            logger.info(f"Neighborhood distribution plot saved to {output_file}")
            return True
        except Exception as e:
            logger.error(f"Error in plot_neighborhood_distribution: {e}")
            return False