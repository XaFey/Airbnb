import plotly.express as px
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Visualization:
    # data/plots directory for saving plots
    def __init__(self, output_dir = os.path.join("data", "plots")):
        # Initialize the Visualization class with the output directory for saving plots.
        self.output_dir = output_dir
        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def plot_price_distribution(self, df):
        try:
            if 'price' not in df.columns:
                raise ValueError("The dataframe does not contain a 'price' column.")
            #no empties
            plot_df = df.dropna(subset=['price'])
            #greater than 0
            plot_df = plot_df[plot_df['price'] > 0]
            #create the histogram plot
            fig = px.histogram(plot_df, x='price', nbins=50, title='Price Distribution')
            #save the plot to a file
            output_file = os.path.join(self.output_dir, "price_distribution.png")
            #ensure the output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            #write the plot to the output file
            fig.write_image(output_file, format='png', width=800, height=600)
            #log the successful creation of the plot
            logger.info(f"Price distribution plot saved to {output_file}")

            return True
        except Exception as e:
            # Log the error and return False if an exception occurs
            logger.error(f"Error in plot_price_distribution: {e}")
            return False


    #neighbourhood distribution plot. The U for consistency
    #Basically copy of the first except about neighborhood column instead
    def plot_neighbourhood_distribution(self, df):
        try:
            if 'neighbourhood' not in df.columns:
                raise ValueError("The dataframe does not contain a 'neighbourhood' column.")
            plot_df = df.dropna(subset=['neighbourhood'])
            #neighborhoods aren't numbers (so that line is gone)
            fig = px.histogram(plot_df, x='neighbourhood', title='Neighbourhood Distribution')
            output_file = os.path.join(self.output_dir, "neighbourhood_distribution.png")
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            fig.write_image(output_file, format='png', width=800, height=600)
            logger.info(f"Neighbourhood distribution plot saved to {output_file}")
            return True
        except Exception as e:
            logger.error(f"Error in plot_neighborhood_distribution: {e}")
            return False