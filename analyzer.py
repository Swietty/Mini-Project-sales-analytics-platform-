import pandas as pd
import numpy as np
from algorithms import bubble_sort, linear_search
from algorithms import compare_search, compare_sorting

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
        self.df = self.df.dropna(subset=["order_date"])
        self.df["customer_id"] = self.df["customer_id"].fillna("unknown")
        self.df["order_amount"] = self.df["order_amount"].fillna(0)
        self.df["product_category"] = self.df["product_category"].fillna("unknown")

        # Standardize column names
        self.df = self.df.rename(columns={
            "order_date": "date",
            "order_amount": "amount",
            "product_category": "category"
        })

        return self.df
       

    def export_clean_data(self, path):
        self.df.to_csv(path, index=False)


        ###  Business Insights
        # Total revenue 
    def total_revenue(self):
        return self.df["amount"].sum()
        # Average order value (AOV)
    def average_order_value(self):
        return self.df["amount"].mean()
        #Customer count
    def customer_count(self):
        return self.df["customer_id"].nunique()

        # Which product category is most profitable?
    def most_profitable_category(self):
        category_revenue = self.df.groupby("category")["amount"].sum()
        return category_revenue.idxmax()

        # Who are the top 10 customers by lifetime value?
    def top_customers_by_lifetime_value(self):
        customer_ltv = self.df.groupby("customer_id")["amount"].sum()
        return customer_ltv.sort_values(ascending=False).head(10)
        # What is the repeat customer rate?
    def repeat_customer_rate(self):
        customer_order_counts = self.df.groupby("customer_id").size()
        repeat_customers = customer_order_counts[customer_order_counts > 1].count()
        total_customers = customer_order_counts.count()
        return repeat_customers / total_customers if total_customers > 0 else 0

        # Are there seasonal or monthly trends in sales?
    def seasonal_trends(self):
        self.df["date"] = pd.to_datetime(self.df["date"])


        # What is the average order size by category?
    def average_order_size_by_category(self):
        category_order_size = self.df.groupby("category")["amount"].mean()
        return category_order_size
        # What percentage of orders are cancelled vs. completed?
    def cancellation_rate(self):
        total_orders = len(self.df)
        cancelled_orders = len(self.df[self.df["status"] == "cancelled"])
        return cancelled_orders / total_orders if total_orders > 0 else 0

        # Which orders are outliers (unusually large/small)?    
    def identify_outliers(self):
        q1 = self.df["amount"].quantile(0.25)
        q3 = self.df["amount"].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = self.df[(self.df["amount"] < lower_bound) | (self.df["amount"] > upper_bound)]
        return outliers

        # Customer segmentation by spending tier
    def customer_segmentation(self):
        spending_tiers = pd.qcut(self.df["amount"], q=4, labels=["Low", "Medium", "High", "VIP"])
        self.df["spending_tier"] = spending_tiers
        return self.df[["customer_id", "spending_tier"]].drop_duplicates()
        # Revenue trends over time (monthly growth)
    def revenue_trends_over_time(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        monthly_revenue = self.df.groupby(self.df["date"].dt.to_period("M"))["amount"].sum()
        return monthly_revenue
    
    #  Custom algorithm implementations for sorting and searching
    def sort_orders_by_amount_custom(self):
        arr = self.df["amount"].tolist()
        sorted_arr = bubble_sort(arr)
        return sorted_arr

    def search_order_custom(self, amount):
        arr = self.df["amount"].tolist()
        index = linear_search(arr, amount)
        return index

    def compare_sorting_performance(self):
        arr = self.df["amount"].tolist()
        return compare_sorting(arr)

    def compare_search_performance(self, value):
        arr = self.df["amount"].tolist()
        return compare_search(arr, value)

