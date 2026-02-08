import matplotlib.pyplot as plt
import pandas as pd
import os

class SalesVisualizer:
    def __init__(self, df):
        self.df = df
        os.makedirs("figures", exist_ok=True)

    def revenue_by_category(self):
        data = self.df.groupby("category")["amount"].sum()
        plt.figure()
        data.plot(kind="bar")
        plt.title("Revenue by Category")
        plt.xlabel("Category")
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.savefig("figures/revenue_by_category.png")
        plt.close()

    def monthly_revenue_trend(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        monthly = self.df.groupby(self.df["date"].dt.to_period("M"))["amount"].sum()
        monthly.index = monthly.index.astype(str)
        plt.figure()
        monthly.plot()
        plt.title("Monthly Revenue Trend")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("figures/monthly_revenue_trend.png")
        plt.close()

    def order_amount_distribution(self):
        plt.figure()
        plt.hist(self.df["amount"], bins=20)
        plt.title("Order Amount Distribution")
        plt.xlabel("Order Amount")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig("figures/order_amount_distribution.png")
        plt.close()
