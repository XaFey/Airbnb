#test data_handler.py
def test_get_summary():
    # Create a sample DataFrame
    import pandas as pd
    from src.data_handler import DataHandler


    data = {
        'id': [1, 62, 35],
        'name': ['Rainbow Lane', 'Sunset Boulevard', 'Ocean View'],
        'price': [1000, 89898, 4000]
    }
    df = pd.DataFrame(data)


    dh = DataHandler.__new__(DataHandler)  
    dh.df = df
    summary = dh.get_summary()

    assert summary['num_rows'] == 3
    assert summary['num_columns'] == 3
    assert summary['column_names'] == ['id', 'name', 'price']

