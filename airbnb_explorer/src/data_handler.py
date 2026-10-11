import pandas as pd
import logging
import os

# Create the data/processed directory if it doesn't exist
#os.makedirs(os.path.join("data", "processed"), exist_ok=True)

#this means we are setting up logging for the module
#logging is used to track events and errors within the module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DataHandler:
    def __init__(self, file_path):
        # Initialize the DataHandler with the path to the CSV file and load the data into a DataFrame.
        self.file_path = file_path
        self.df = None
        self.processed_dir = os.path.join("data", "processed")
        os.makedirs(self.processed_dir, exist_ok=True)
        self.load_data()

    def load_data(self):
        #cleaning time
        try:
            self.df = pd.read_csv(self.file_path)
            # Log the number of rows loaded
            logger.info(f"Loaded dataset with {len(self.df)} rows")
            if self.df['price'].dtype==object:
                #get rid of the $ and , in the price column and convert to float
                self.df['price'] = self.df['price'].str.replace('$', '').str.replace(',', '').astype(float)
                self.df['price'] = self.df['price'].str.replace('@', '').str.replace(',', '').astype(float)
            # Remove rows with missing values in the 'price' column and outliers (price <= 0)
            self.df['price'] = pd.to_numeric(self.df['price'], errors='coerce')
            self.df = self.df[self.df['price'] > 0]
            logger.info(f"Cleaned dataset with {len(self.df)} rows after removing missing values and outliers")
        #the file not found error handling
        except FileNotFoundError:
            logger.error(f"File not found: {self.file_path}")
            raise
    
    def get_summary(self):
        # Return a summary of the dataset, including number of rows, columns, column names, missing values, and data types.
        if self.df is not None:
            #creates dictionary for summary
            summary = {
                #,to_dict makes dictionary
                # number of rows length
                'num_rows': len(self.df),
                # number of columns length
                'num_columns': len(self.df.columns),
                # list of column names
                'column_names': list(self.df.columns),
                # number of missing values per column (is null means empty, sum adds all empty together)
                'missing_values': self.df.isnull().sum().to_dict(),
                # data types of each column
                'data_types': self.df.dtypes.to_dict()
            }
            return summary
        else:
            logger.warning("Dataframe is not loaded.")
            return None

    def search_entries(self, column, value):
        # Search for entries in the dataset based on a specified column and value.
        if self.df is not None:
            return self.df[self.df[column] == value]
        else:
            logger.warning("Dataframe is not loaded.")
            return None

    def filter_and_export(self, output_file, columns):
        # Filter the dataset based on specified columns and export to a CSV file in the processed directory.
        if self.df is not None:
            filtered_df = self.df[columns]
            # Log the number of rows in the filtered dataframe
            filtered_df.to_csv(os.path.join(self.processed_dir, output_file), index=False)
            logger.info(f"Filtered data exported to {os.path.join(self.processed_dir, output_file)}")
        else:
            logger.warning("Dataframe is not loaded.")

    def get_aggregate(self, column):
        # gives stats for specified column
        if self.df is not None:
            #if the column exists in the dataframe
            if column in self.df.columns:
                aggregate_stats = {
                    #average
                    'mean': self.df[column].mean(),
                    #median (middle)
                    'median': self.df[column].median(),
                    #standard deviation
                    'std_dev': self.df[column].std(),
                    #minimum value
                    'min': self.df[column].min(),
                    #maximum value
                    'max': self.df[column].max()
                }
                return aggregate_stats
            else:
                logger.warning(f"Column '{column}' does not exist in the dataframe.")
                return None
        else:
            logger.warning("Dataframe is not loaded.")
            return None