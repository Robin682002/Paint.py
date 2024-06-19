from product import Product
from customer import Customer
from order import Order
from payment import CashPayment

def main():
    products = []
    customers = []
    orders = []
    order_id = 1

    while True:
        print("\n===== E-commerce Platform Menu =====")
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. Display Orders")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            product_stock = int(input("Enter product stock: "))
            

            product = Product(len(products) + 1, product_name, product_price, product_stock)
            products.append(product)
            print(f"Product '{product_name}' added.")

        elif choice == "2":
            customer_name = input("Enter customer name: ")
            customer_email = input("Enter customer email: ")
            customer_id = input("Enter customer ID: ")
            customer = Customer(len(customers) + 1, customer_name, customer_email,customer_id)
            customers.append(customer)
            print(f"Customer '{customer_name}' added.")

        elif choice == "3":
            try:
                customer_id = int(input("Enter customer ID: "))
                customer = None
                for c in customers:
                    if customer_id == customer_id:
                        customer = customer_id
                        break
                if not customer:
                    print("Customer not found.")
                    continue
            except ValueError:
                print("Invalid input for customer ID. Please enter a valid number.")
                continue

            order = Order(order_id, customer)
            order_id += 1

            while True:
                product_id = input("Enter product ID (or 'done' to finish): ")
                if product_id.lower() == 'done':
                    break

                try:
                    product_id = int(product_id)
                    product = None
                    for p in products:
                        if p.product_id == product_id:
                            product = p
                            break

                    if not product:
                        print("Product not found.")
                        continue

                    quantity = int(input(f"Enter quantity for {product.name}: "))
                    if order.add_item(product, quantity):
                        print(f"Added {quantity} x {product.name} to order.")
                    else:
                        print(f"Failed to add {quantity} x {product.name} to order. Not enough stock.")
                except ValueError:
                    print("Invalid input for product ID or quantity. Please enter a valid number.")

            total_amount = order.get_total()
            print(f"Total amount to pay: ${total_amount:.2f}")

            payment = CashPayment(total_amount)
            if payment.process_payment():
                order.mark_as_paid()
                orders.append(order)
                order.record_transaction()
                print("Order placed and payment processed successfully!")
            else:
                print("Payment failed. Order not placed.")

        elif choice == "4":
            print("\n===== Orders Placed =====")
            for order in orders:
                print(order)

        elif choice == "5":
            print("Exiting E-commerce Platform. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
