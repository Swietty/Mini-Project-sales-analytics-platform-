# main.py
from analyzer import SalesAnalyzer
from visualization import SalesVisualizer
from utils import format_currency, format_percentage, save_text_report

def main():
    analyzer = SalesAnalyzer()
    analyzer.load_data("data/sales_data.csv")
    analyzer.handle_missing_values()
    analyzer.export_clean_data("data/sales_clean.csv")

    print("Missing Values Summary:\n", analyzer.missing_values_sum())
    print("\nTotal Revenue:", format_currency(analyzer.total_revenue()))
    print("Average Order Value:", format_currency(analyzer.average_order_value()))
    print("Customer Count:", analyzer.customer_count())
    print("Most Profitable Category:", analyzer.most_profitable_category())
    print("Top Customers by Lifetime Value:\n", analyzer.top_customers_by_lifetime_value())
    print("Repeat Customer Rate:", format_percentage(analyzer.repeat_customer_rate()))
    print("Average Order Size by Category:\n", analyzer.average_order_size_by_category())
    print("Cancellation Rate:", format_percentage(analyzer.cancellation_rate()))

    # Custom algorithms
    print("\nSorted amounts (custom):", analyzer.sort_orders_by_amount_custom()[:10])
    idx = analyzer.search_order_custom(500)
    print("Index of order with amount 500:", idx)
    print("\nSorting performance (bubble, sorted, numpy):", analyzer.compare_sorting_performance())
    print("Search performance (linear, in, numpy):", analyzer.compare_search_performance(500))

    # Visualizations
    visualizer = SalesVisualizer(analyzer.df)
    visualizer.revenue_by_category()
    visualizer.monthly_revenue_trend()
    visualizer.order_amount_distribution()
    print("\nVisualizations saved to 'figures/' folder.")

if __name__ == "__main__":
    main()
