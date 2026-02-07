import pandas as pd

class SalesAnalyzer:
    def __init__(self):
        self.df = None

    def load_data(self, path):
        try:
            self.df = pd.read_csv(path)
            return self.df
        except FileNotFoundError:
            raise ValueError("CSV file not found")

    def missing_values_sum(self):
        return self.df.isnull().sum()

    def handle_missing_values(self):
        self.df = self.df.dropna(subset=["date"])
        self.df["customer_id"] = self.df["customer_id"].fillna("unknown")
        self.df["amount"] = self.df["amount"].fillna(0)
        self.df["category"] = self.df["category"].fillna("unknown")
        return self.df

    def export_clean_data(self, path):
        self.df.to_csv(path, index=False)
