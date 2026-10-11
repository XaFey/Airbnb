import argparse
import logging
from src.data_handler import DataHandler
from src.visualization import Visualization
from src.cli import CLI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s-%(message)s')
logger = logging.getLogger(__name__)

def main():
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

    # parse the command-line arguments means that the user's input from the command line is captured and stored in the args variable
    args = parser.parse_args()

    # Initialize DataHandler and Visualization classes, and handle CLI commands
    try:
        # 34-36 means initializing the DataHandler, Visualization, and CLI instances
        dh = DataHandler(args.file)
        vis = Visualization(output_dir="processed")
        cli = CLI()
        #the conditional logic for handling CLI commands. 
        if args.summary:
            cli.summary()
        #handle the search command. search takes two arguments: column and value
        elif args.search:
            cli.search_entries(args.search[0], args.search[1])
        #handle the export command. export takes two arguments: output file and columns to include
        elif args.export and args.columns:
            cli.export_data(args.export, args.columns)
        #handle the aggregate command. aggregate takes one argument: the column to aggregate by
        elif args.aggregate:
            cli.display_aggregate(args.aggregate)
        #handle the plot command. plot takes one argument: the type of plot to generate
        elif args.plot:
            cli.export_plot(args.plot)
        #if no valid command is provided, print the help message
        else:
            parser.print_help()
    #catch any exceptions that occur during the execution of the CLI commands. Error command raised then
    except Exception as e:
        # Log the error and re-raise the exception
        logger.error(f"Error: {e}")
        raise

if __name__== "__main__":
    main()