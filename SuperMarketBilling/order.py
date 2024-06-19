import csv
from datetime import datetime
from customer import Customer

class Order:
    def __init__(self, order_id, customer ):
        self.order_id = order_id
        self.customer= customer
        self.items = []
        self.is_paid = False
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer}, Items: {[item['product'].name for item in self.items]}, Total: ${self.get_total():.2f}, Paid: {self.is_paid}, Timestamp: {self.timestamp}"

    def add_item(self, product, quantity):
        if product.reduce_stock(quantity):
            self.items.append({"product": product, "quantity": quantity})
            return True
        return False

    def get_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def mark_as_paid(self):
        self.is_paid = True

    def record_transaction(self):
        with open('Super_Market_transactions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for item in self.items:
                writer.writerow([
                    self.timestamp,
                    self.order_id,
                    self.customer,
                    item["product"].name,
                    item["quantity"],
                    item["product"].price,
                    self.get_total()
                ])

