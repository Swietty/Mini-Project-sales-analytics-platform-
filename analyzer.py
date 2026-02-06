import pandas as pd

class SalesAnalyzer:
    def __init__(self):
        self.df = None

    def load_data(self, path):
        try:
            self.df = pd.read_csv(path)
        except FileNotFoundError:
            raise ValueError("CSV file not found")
    
   