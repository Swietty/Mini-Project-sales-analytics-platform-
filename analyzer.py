import pandas as pd
from algorithms import bubble_sort, linear_search, compare_sorting, compare_search
from utils import validate_columns

class SalesAnalyzer:
    def __init__(self):
        self.df = None

    def load_data(self, path):
        self.df = pd.read_csv(path)
        validate_columns(self.df)
        return self.df

    def missing_values_sum(self):
        return self.df.isnull().sum()

    def handle_missing_values(self):
        self.df = self.df.dropna(subset=["order_date"])
        self.df["customer_id"] = self.df["customer_id"].fillna("unknown")
        self.df["order_amount"] = self.df["order_amount"].fillna(0)
        self.df["product_category"] = self.df["product_category"].fillna("unknown")

        # Spalten umbenennen für Konsistenz
        self.df = self.df.rename(columns={
            "order_date": "date",
            "order_amount": "amount",
            "product_category": "category"
        })
        return self.df

    def export_clean_data(self, path):
        self.df.to_csv(path, index=False)

    # Business Insights
    def total_revenue(self):
        return self.df["amount"].sum()

    def average_order_value(self):
        return self.df["amount"].mean()

    def customer_count(self):
        return self.df["customer_id"].nunique()

    def most_profitable_category(self):
        return self.df.groupby("category")["amount"].sum().idxmax()

    def top_customers_by_lifetime_value(self):
        return self.df.groupby("customer_id")["amount"].sum().sort_values(ascending=False).head(10)

    def repeat_customer_rate(self):
        counts = self.df.groupby("customer_id").size()
        repeat = counts[counts > 1].count()
        total = counts.count()
        return repeat / total if total > 0 else 0

    def average_order_size_by_category(self):
        return self.df.groupby("category")["amount"].mean()

    def cancellation_rate(self):
        total = len(self.df)
        cancelled = len(self.df[self.df["status"] == "cancelled"])
        return cancelled / total if total > 0 else 0

    def identify_outliers(self):
        q1 = self.df["amount"].quantile(0.25)
        q3 = self.df["amount"].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return self.df[(self.df["amount"] < lower) | (self.df["amount"] > upper)]

    def customer_segmentation(self):
        tiers = pd.qcut(self.df["amount"], 4, labels=["Low", "Medium", "High", "VIP"])
        self.df["spending_tier"] = tiers
        return self.df[["customer_id", "spending_tier"]].drop_duplicates()

    def revenue_trends_over_time(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        return self.df.groupby(self.df["date"].dt.to_period("M"))["amount"].sum()

    # Custom algorithms
    def sort_orders_by_amount_custom(self):
        return bubble_sort(self.df["amount"].tolist())

    def search_order_custom(self, amount):
        return linear_search(self.df["amount"].tolist(), amount)

    def compare_sorting_performance(self):
        return compare_sorting(self.df["amount"].tolist())

    def compare_search_performance(self, value):
        return compare_search(self.df["amount"].tolist(), value)
