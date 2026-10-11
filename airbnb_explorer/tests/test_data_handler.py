#test data_handler.py
def test_get_summary():
    # Create a sample DataFrame
    import pandas as pd
    from src.data_handler import DataHandler

    #sample data
    data = {
        'id': [1, 62, 35],
        'name': ['Rainbow Lane', 'Sunset Boulevard', 'Ocean View'],
        'price': [1000, 89898, 4000]
    }
    #create DataFrame from the sample data
    df = pd.DataFrame(data)

    # Initialize the DataHandler instance
    # Create a new instance of DataHandler without calling __init__
    #not calling because we want to manually set the DataFrame attribute before initialization
    dh = DataHandler.__new__(DataHandler)  

    # Set the DataFrame attribute for the DataHandler instance
    dh.df = df
    # Get the summary of the DataFrame
    summary = dh.get_summary()

    # assertions to check the summary
    #assert means the test will fail if the condition is not met
    assert summary['num_rows'] == 3
    assert summary['num_columns'] == 3
    assert summary['column_names'] == ['id', 'name', 'price']

