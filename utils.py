REQUIRED_COLUMNS = {
    "order_id",
    "customer_id",
    "order_date",
    "product_category",
    "product_name",
    "quantity",
    "unit_price",
    "order_amount",
    "status"
}

def validate_columns(df):
    # überprüfen, ob alle erforderlichen Spalten vorhanden sind
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def format_currency(value):
    # formatieren einer Zahl als Währungswert
    return f"{value:,.2f} €"

def format_percentage(value):
    # formatieren einer Zahl als Prozentsatz
    return f"{value * 100:.2f}%"

def save_text_report(path, lines):
    # speichern eines Berichts als Textdatei
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
