class Customer:
    def __init__(self, name, email, phone,customer_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.customer_id = customer_id

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone } \nCustomer ID: {self.customer_id}"