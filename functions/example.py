import pandas as pd

def create_example():
    """
    Returns a data frame example
    """
    data = pd.DataFrame({
        'Product' : ['café', 'guaraná', 'água', 'chocolate', 'feijão'],
        'Price' : [6, 10, 1, 5, 8],
        'Quantity' : [20, 10, 12, 15, 35]
    })

    return data
