from analyzer import SalesAnalyzer

def main():
    analyzer = SalesAnalyzer()
    data = analyzer.load_data('sales_data.csv')
    print(data.head())

if __name__ == "__main__":
    main()