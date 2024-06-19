class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        # Simulate cash payment processing
        print(f"Processing cash payment of ${self.amount:.2f}")
        return True
