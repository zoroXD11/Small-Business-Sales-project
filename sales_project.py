class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class SalesManager:
    def __init__(self):
        self.products = []
        self.total_revenue = 0

    # Add a new product
    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter available stock: "))

        product = Product(name, price, stock)
        self.products.append(product)

        print("Product added successfully!")

    # Display all products
    def display_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\n--- Available Products ---")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.name} | Price: Rs.{product.price} | Stock: {product.stock}")

    # Record a sale
    def record_sale(self):
        self.display_products()

        if not self.products:
            return

        choice = int(input("Enter product number: "))

        if choice < 1 or choice > len(self.products):
            print("Invalid product number!")
            return

        product = self.products[choice - 1]

        quantity = int(input("Enter quantity sold: "))

        if quantity <= 0:
            print("Quantity must be positive.")
        elif quantity > product.stock:
            print("Insufficient stock!")
        else:
            amount = product.price * quantity
            product.stock -= quantity
            self.total_revenue += amount

            print("Sale recorded successfully!")
            print("Sale Amount: Rs.", amount)

    # Calculate total revenue
    def calculate_revenue(self):
        print("\nTotal Revenue: Rs.", self.total_revenue)


# Main Program
manager = SalesManager()

while True:
    print("\n===== SMALL BUSINESS SALES TRACKER =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Record Sale")
    print("4. Calculate Total Revenue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_product()

    elif choice == "2":
        manager.display_products()

    elif choice == "3":
        manager.record_sale()

    elif choice == "4":
        manager.calculate_revenue()

    elif choice == "5":
        print("Thank you for using Sales Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")

        