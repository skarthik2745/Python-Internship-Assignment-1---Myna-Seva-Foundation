# SUPERMARKET MANAGEMENT SYSTEM

class Product:
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, qty):
        self.stock += qty

    def sell(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            print(f"Sold {qty} {self.name}(s).")
        else:
            print("Not enough stock to sell!")

    def display_info(self):
        print("\n--- Product Information ---")
        print("Product Name:", self.name)
        print("Price: ₹", self.price)
        print("Stock Available:", self.stock)
        print("-" * 30)

# Main program
products = []

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: ₹"))
    stock = int(input("Enter stock quantity: "))
    p = Product(name, price, stock)
    products.append(p)
    print("Product added successfully!\n")

def sell_product():
    name = input("Enter product name to sell: ")
    for product in products:
        if product.name.lower() == name.lower():
            qty = int(input("Enter quantity to sell: "))
            product.sell(qty)
            return
    print("Product not found!\n")

def restock_product():
    name = input("Enter product name to restock: ")
    for product in products:
        if product.name.lower() == name.lower():
            qty = int(input("Enter quantity to add: "))
            product.restock(qty)
            print("Stock updated!\n")
            return
    print("Product not found!\n")

def show_all_products():
    if not products:
        print("No products available.")
        return
    for product in products:
        product.display_info()

# Menu
while True:
    print("\n====== Supermarket Management Menu ======")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. View All Products")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        sell_product()
    elif choice == "3":
        restock_product()
    elif choice == "4":
        show_all_products()
    elif choice == "5":
        print("Exiting Supermarket Management System.")
        break
    else:
        print("Invalid choice. Try again.")