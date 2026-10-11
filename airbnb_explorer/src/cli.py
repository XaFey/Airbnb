import argparse
import os
from src.data_handler import DataHandler
from src.visualization import Visualization

#####create cli using argparse#####
#####
parser = argparse.ArgumentParser(description = 'Airbnb Listings Explorer')
#the raw file
parser.add_argument('--file', type = str, default='data/raw/listings.csv', help = 'Path to Airbnb CSV file')
#summary
parser.add_argument('--summary', action= 'store_true', help='Display data summary')
#search data set. Metavar specifies the names of the arguments in the help message, nargs specifies the number of arguments to expect
parser.add_argument('--search', nargs=2, metavar=('COLUMN', 'VALUE'), help='Search entries by column and value')
#filtered data exported to csv
parser.add_argument('--export', type=str, help='Export filtered data to CSV (specify output file)')
#columns to include in export
parser.add_argument('-c', '--columns', nargs='*', help='Columns to include in export')
#aggregate data by column. aggregate means computing summary statistics like mean, median, std_dev, min, and max for the specified column
parser.add_argument('--aggregate', type=str, choices=['neighborhood', 'room_type'], help='Display aggregate data by column')
#plot data visualization (THIS DOESN"T WORK FOR SOME REASON)
parser.add_argument('--plot', type=str, choices=['price_dist', 'neighborhood'], help='Export plot as JPG/PNG')
####
class CLI:
        def __init__(self):
            # Initialize the CLI with parsed arguments, data handler, and visualization object
            self.args = parser.parse_args()
            self.file_path = self.args.file
            # Initialize the data handler with the file path
            self.data_handler = DataHandler(self.file_path)
            self.visualization = Visualization(output_dir="processed")

        def summary(self):
            summary = self.data_handler.get_summary()
            if summary:
                #just the summary and types
                print("Dataset Summary:")
                print(f"Number of Rows: {summary['num_rows']}")
                print(f"Number of Columns: {summary['num_columns']}")
                print(f"Column Names: {summary['column_names']}")
                print(f"Missing Values: {summary['missing_values']}")
                print(f"Data Types: {summary['data_types']}")

        def search_entries(self, column, value):
            results = self.data_handler.search_entries(column, value)
            #there has to be results for if
            if results is not None and not results.empty:
                print(f"Search Results for {column} = {value}:")
                print(results)
            else:
                print(f"No entries found for {column} = {value}.")

        def export_data(self, output_file, columns):
            #exports the chosen data to the processed folder
            self.data_handler.filter_and_export(output_file, columns)
            print(f"Filtered data exported to {os.path.join('processed', output_file)}")

        def display_aggregate(self, column):
            aggregate_stats = self.data_handler.get_aggregate(column)
            #if there are aggregate stats, print them
            if aggregate_stats:
                print(f"Aggregate Statistics for {column}:")
                # for loop through each statistic and its value
                for stat, value in aggregate_stats.items():
                    print(f"{stat}: {value}")

        def export_plot(self, plot_type):
            #if the plot type is price distribution, call the plot_price_distribution method
            if plot_type == 'price_dist':
                # call the plot_price_distribution method from the visualization object
                result = self.visualization.plot_price_distribution(self.data_handler.df)
                if result:
                    print("Price distribution plot exported successfully.")
                else:
                    print("Failed to export price distribution plot.")