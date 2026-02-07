from analyzer import SalesAnalyzer

def main():
    analyzer = SalesAnalyzer()
    analyzer.load_data("data/sales_data.csv")
    analyzer.handle_missing_values()
    analyzer.export_clean_data("data/sales_clean.csv")

if __name__ == "__main__":
    main()
