from analyzer import SalesAnalyzer

def main():
    analyzer = SalesAnalyzer()
    analyzer.load_data("data/sales_data.csv")
    analyzer.handle_missing_values()
    analyzer.export_clean_data("data/sales_clean.csv")

    
    print("Missing Values Summary:", analyzer.missing_values_sum())
    print("\nData loaded and cleaned successfully.")
    print("\nTotal Revenue:", analyzer.total_revenue())
    print("\nAverage Order Value:", analyzer.average_order_value())
    print("\nCustomer Count:", analyzer.customer_count())
    print("\nMost Profitable Category:", analyzer.most_profitable_category())
    print("\nTop Customers by Lifetime Value:", analyzer.top_customers_by_lifetime_value())
    print("\nRepeat Customer Rate:", analyzer.repeat_customer_rate())
    print("\nAverage Order Size by Category:")
    print(analyzer.average_order_size_by_category())
    print("\nCancellation Rate:", analyzer.cancellation_rate(), "\n")

# beispiel für benutzerdefinierte Algorithmen
    sorted_amounts = analyzer.sort_orders_by_amount_custom()
    print("Sorted amounts (custom):", sorted_amounts[:10])

    # Suche nach einem bestimmten Bestellbetrag
    idx = analyzer.search_order_custom(500)
    print("Index of order with amount 500:", idx)

    print("\nSorting performance (bubble, sorted, numpy):")
    print(analyzer.compare_sorting_performance())

    print("\nSearch performance (linear, in, numpy):")
    print(analyzer.compare_search_performance(500))

if __name__ == "__main__":
    main()
