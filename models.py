from datetime import datetime

# Base Entity class
class Entity:
    def __init__(self, id):
        if id is None:
            raise ValueError("ID cannot be None")
        self.id = id

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"


# Product class
class Product(Entity):
    def __init__(self, id, name, category, base_price):
        super().__init__(id)

        if not name:
            raise ValueError("Product name cannot be empty")
        if base_price < 0:
            raise ValueError("Base price must be non-negative")

        self.name = name
        self.category = category
        self.base_price = float(base_price)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.base_price}"


# Customer class
class Customer(Entity):
    def __init__(self, id, name, email, lifetime_value=0.0):
        super().__init__(id)

        if not name:
            raise ValueError("Customer name cannot be empty")
        if "@" not in email:
            raise ValueError("Invalid email")

        self.name = name
        self.email = email
        self.lifetime_value = float(lifetime_value)

    def __str__(self):
        return f"{self.name} ({self.email})"


# Order class
class Order(Entity):
    VALID_STATUSES = {"completed", "cancelled", "pending"}

    def __init__(self, id, date, customer, amount, status):
        super().__init__(id)

        if isinstance(date, str):
            date = datetime.fromisoformat(date)

        if amount < 0:
            raise ValueError("Order amount must be non-negative")
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid order status: {status}")

        self.date = date
        self.customer = customer
        self.amount = float(amount)
        self.status = status

    def __str__(self):
        return f"Order {self.id}: {self.amount} ({self.status})"


# Factory pattern
class OrderFactory:
    @staticmethod
    def create_order(id, date, customer, amount, status):
        return Order(id, date, customer, amount, status)
