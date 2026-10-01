# ==========================================

# Restaurant Ordering System in Python

# ==========================================

# ---------- Classes ----------

class MenuItem:

    def __init__(self, item_id, name, price):

        self.item_id = item_id

        self.name = name

        self.price = price

    def __str__(self):

        return f"{self.item_id}. {self.name} - ${self.price:.2f}"


class Table:

    def __init__(self, table_number):

        self.table_number = table_number

        self.status = "Available"

    def __str__(self):

        return f"Table {self.table_number} - {self.status}"


class Order:

    tax_rate = 0.12

    def __init__(self, order_id, table_number):

        self.order_id = order_id

        self.table_number = table_number

        self.items = []

        self.status = "Pending"

        self.tip = 0

    def add_item(self, menu_item):

        self.items.append(menu_item)

    def calculate_subtotal(self):

        return sum(item.price for item in self.items)

    def calculate_tax(self):

        return self.calculate_subtotal() * Order.tax_rate

    def calculate_total(self):

        return self.calculate_subtotal() + self.calculate_tax() + self.tip

    def complete_order(self):

        self.status = "Completed"

    def print_receipt(self):

        print("\n========== RECEIPT ==========")

        print(f"Order ID: {self.order_id}")

        print(f"Table Number: {self.table_number}")

        print("-----------------------------")

        for item in self.items:

            print(f"{item.name} - ${item.price:.2f}")

        print("-----------------------------")

        print(f"Subtotal: ${self.calculate_subtotal():.2f}")

        print(f"Tax: ${self.calculate_tax():.2f}")

        print(f"Tip: ${self.tip:.2f}")

        print(f"Total: ${self.calculate_total():.2f}")

        print("=============================\n")


# ---------- Main System ----------

class RestaurantSystem:

    def __init__(self):

        self.menu = []

        self.tables = []

        self.orders = []

        self.sales = 0

    # ---------- Menu Management ----------

    def add_menu_item(self):

        item_id = len(self.menu) + 1

        name = input("Enter item name: ")

        price = float(input("Enter item price: "))

        item = MenuItem(item_id, name, price)

        self.menu.append(item)

        print("Menu item added successfully!\n")

    def display_menu(self):

        print("\n====== MENU ======")

        if not self.menu:

            print("No menu items available.")

        else:

            for item in self.menu:

                print(item)

        print()

    def update_menu_item(self):

        self.display_menu()

        item_id = int(input("Enter item ID to update: "))

        for item in self.menu:

            if item.item_id == item_id:

                item.name = input("Enter new item name: ")

                item.price = float(input("Enter new price: "))

                print("Menu item updated!\n")

                return

        print("Item not found.\n")

    def remove_menu_item(self):

        self.display_menu()

        item_id = int(input("Enter item ID to remove: "))

        for item in self.menu:

            if item.item_id == item_id:

                self.menu.remove(item)

                print("Menu item removed!\n")

                return

        print("Item not found.\n")

    # ---------- Table Management ----------

    def add_tables(self):

        count = int(input("How many tables to add? "))

        for i in range(1, count + 1):

            self.tables.append(Table(i))

        print("Tables added successfully!\n")

    def display_tables(self):

        print("\n====== TABLE STATUS ======")

        for table in self.tables:

            print(table)

        print()

    def update_table_status(self):

        self.display_tables()

        table_number = int(input("Enter table number: "))

        for table in self.tables:

            if table.table_number == table_number:

                print("1. Available")

                print("2. Occupied")

                print("3. Needs Cleaning")

                choice = input("Choose status: ")

                if choice == "1":

                    table.status = "Available"

                elif choice == "2":

                    table.status = "Occupied"

                elif choice == "3":

                    table.status = "Needs Cleaning"

                print("Table status updated!\n")

                return

        print("Table not found.\n")

    # ---------- Order Processing ---------- 

    def create_order(self):

        if not self.menu:

            print("Menu is empty.\n")

            return

        table_number = int(input("Enter table number: "))

        order_id = len(self.orders) + 1

        order = Order(order_id, table_number)

        while True:

            self.display_menu()

            item_id = int(input("Enter item ID to add (0 to finish): "))

            if item_id == 0:

                break

            found = False

            for item in self.menu:

                if item.item_id == item_id:

                    order.add_item(item)

                    found = True

                    print(f"{item.name} added to order.\n")

            if not found:

                print("Invalid item ID.\n")

        tip = float(input("Enter tip amount: "))

        order.tip = tip

        self.orders.append(order)

        # Update table status

        for table in self.tables:

            if table.table_number == table_number:

                table.status = "Occupied"

        print("Order created successfully!\n")

    # ---------- Payment Processing ----------

    def process_payment(self):

        if not self.orders:

            print("No orders available.\n")

            return

        order_id = int(input("Enter order ID to process payment: "))

        for order in self.orders:

            if order.order_id == order_id:

                order.print_receipt()

                payment = float(input("Enter payment amount: "))

                total = order.calculate_total()

                if payment >= total:

                    change = payment - total

                    print(f"Payment successful!")

                    print(f"Change: ${change:.2f}\n")

                    order.complete_order()

                    self.sales += total

                    # Update table status

                    for table in self.tables:

                        if table.table_number == order.table_number:

                            table.status = "Needs Cleaning"

                else:

                    print("Insufficient payment.\n")

                return

        print("Order not found.\n")

    # ---------- Order History ----------

    def display_orders(self):

        print("\n====== ORDER HISTORY ======")

        if not self.orders:

            print("No orders found.\n")

            return

        for order in self.orders:

            print(f"Order ID: {order.order_id}")

            print(f"Table: {order.table_number}")

            print(f"Status: {order.status}")

            print(f"Total: ${order.calculate_total():.2f}")

            print("---------------------------")

        print()

    # ---------- Sales Report ----------

    def sales_report(self):

        print("\n====== SALES REPORT ======")

        completed_orders = 0

        for order in self.orders:

            if order.status == "Completed":

                completed_orders += 1

        print(f"Completed Orders: {completed_orders}")

        print(f"Total Sales: ${self.sales:.2f}")

        print("==========================\n")

    # ---------- Main Menu ----------

    def run(self):

        while True:

            print("====== RESTAURANT ORDERING SYSTEM ======")

            print("1. Add Menu Item")

            print("2. Display Menu")

            print("3. Update Menu Item")

            print("4. Remove Menu Item")

            print("5. Add Tables")

            print("6. Display Tables")

            print("7. Update Table Status")

            print("8. Create Order")

            print("9. Process Payment")

            print("10. Display Orders")

            print("11. Sales Report")

            print("12. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                self.add_menu_item()

            elif choice == "2":

                self.display_menu()

            elif choice == "3":

                self.update_menu_item()

            elif choice == "4":

                self.remove_menu_item()

            elif choice == "5":

                self.add_tables()

            elif choice == "6":

                self.display_tables()

            elif choice == "7":

                self.update_table_status()

            elif choice == "8":

                self.create_order()

            elif choice == "9":

                self.process_payment()

            elif choice == "10":

                self.display_orders()

            elif choice == "11":

                self.sales_report()

            elif choice == "12":

                print("Exiting system...")

                break

            else:

                print("Invalid choice.\n")


# ---------- Run Program ----------

system = RestaurantSystem()

system.run()
 
# ==========================================

# Restaurant Ordering System in Python

# ==========================================

# ---------- Classes ----------

class MenuItem:

   def __init__(self, item_id, name, price):

       self.item_id = item_id

       self.name = name

       self.price = price

   def __str__(self):

       return f"{self.item_id}. {self.name} - ${self.price:.2f}"


class Table:

   def __init__(self, table_number):

       self.table_number = table_number

       self.status = "Available"

   def __str__(self):

       return f"Table {self.table_number} - {self.status}"


class Order:

   tax_rate = 0.12

   def __init__(self, order_id, table_number):

       self.order_id = order_id

       self.table_number = table_number

       self.items = []

       self.status = "Pending"

       self.tip = 0

   def add_item(self, menu_item):

       self.items.append(menu_item)

   def calculate_subtotal(self):

       return sum(item.price for item in self.items)

   def calculate_tax(self):

       return self.calculate_subtotal() * Order.tax_rate

   def calculate_total(self):

       return self.calculate_subtotal() + self.calculate_tax() + self.tip

   def complete_order(self):

       self.status = "Completed"

   def print_receipt(self):

       print("\n========== RECEIPT ==========")

       print(f"Order ID: {self.order_id}")

       print(f"Table Number: {self.table_number}")

       print("-----------------------------")

       for item in self.items:

           print(f"{item.name} - ${item.price:.2f}")

       print("-----------------------------")

       print(f"Subtotal: ${self.calculate_subtotal():.2f}")

       print(f"Tax: ${self.calculate_tax():.2f}")

       print(f"Tip: ${self.tip:.2f}")

       print(f"Total: ${self.calculate_total():.2f}")

       print("=============================\n")


# ---------- Main System ----------

class RestaurantSystem:

   def __init__(self):

       self.menu = []

       self.tables = []

       self.orders = []

       self.sales = 0

   # ---------- Menu Management ----------

   def add_menu_item(self):

       item_id = len(self.menu) + 1

       name = input("Enter item name: ")

       price = float(input("Enter item price: "))

       item = MenuItem(item_id, name, price)

       self.menu.append(item)

       print("Menu item added successfully!\n")

   def display_menu(self):

       print("\n====== MENU ======")

       if not self.menu:

           print("No menu items available.")

       else:

           for item in self.menu:

               print(item)

       print()

   def update_menu_item(self):

       self.display_menu()

       item_id = int(input("Enter item ID to update: "))

       for item in self.menu:

           if item.item_id == item_id:

               item.name = input("Enter new item name: ")

               item.price = float(input("Enter new price: "))

               print("Menu item updated!\n")

               return

       print("Item not found.\n")

   def remove_menu_item(self):

       self.display_menu()

       item_id = int(input("Enter item ID to remove: "))

       for item in self.menu:

           if item.item_id == item_id:

               self.menu.remove(item)

               print("Menu item removed!\n")

               return

       print("Item not found.\n")

   # ---------- Table Management ----------

   def add_tables(self):

       count = int(input("How many tables to add? "))

       for i in range(1, count + 1):

           self.tables.append(Table(i))

       print("Tables added successfully!\n")

   def display_tables(self):

       print("\n====== TABLE STATUS ======")

       for table in self.tables:

           print(table)

       print()

   def update_table_status(self):

       self.display_tables()

       table_number = int(input("Enter table number: "))

       for table in self.tables:

           if table.table_number == table_number:

               print("1. Available")

               print("2. Occupied")

               print("3. Needs Cleaning")

               choice = input("Choose status: ")

               if choice == "1":

                   table.status = "Available"

               elif choice == "2":

                   table.status = "Occupied"

               elif choice == "3":

                   table.status = "Needs Cleaning"

               print("Table status updated!\n")

               return

       print("Table not found.\n")

   # ---------- Order Processing ----------

   def create_order(self):

       if not self.menu:

           print("Menu is empty.\n")

           return

       table_number = int(input("Enter table number: "))

       order_id = len(self.orders) + 1

       order = Order(order_id, table_number)

       while True:

           self.display_menu()

           item_id = int(input("Enter item ID to add (0 to finish): "))

           if item_id == 0:

               break

           found = False

           for item in self.menu:

               if item.item_id == item_id:

                   order.add_item(item)

                   found = True

                   print(f"{item.name} added to order.\n")

           if not found:

               print("Invalid item ID.\n")

       tip = float(input("Enter tip amount: "))

       order.tip = tip

       self.orders.append(order)

       # Update table status

       for table in self.tables:

           if table.table_number == table_number:

               table.status = "Occupied"

       print("Order created successfully!\n")

   # ---------- Payment Processing ----------

   def process_payment(self):

       if not self.orders:

           print("No orders available.\n")

           return

       order_id = int(input("Enter order ID to process payment: "))

       for order in self.orders:

           if order.order_id == order_id:

               order.print_receipt()

               payment = float(input("Enter payment amount: "))

               total = order.calculate_total()

               if payment >= total:

                   change = payment - total

                   print(f"Payment successful!")

                   print(f"Change: ${change:.2f}\n")

                   order.complete_order()

                   self.sales += total

                   # Update table status

                   for table in self.tables:

                       if table.table_number == order.table_number:

                           table.status = "Needs Cleaning"

               else:

                   print("Insufficient payment.\n")

               return

       print("Order not found.\n")

   # ---------- Order History ----------

   def display_orders(self):

       print("\n====== ORDER HISTORY ======")

       if not self.orders:

           print("No orders found.\n")

           return

       for order in self.orders:

           print(f"Order ID: {order.order_id}")

           print(f"Table: {order.table_number}")

           print(f"Status: {order.status}")

           print(f"Total: ${order.calculate_total():.2f}")

           print("---------------------------")

       print()

   # ---------- Sales Report ----------

   def sales_report(self):

       print("\n====== SALES REPORT ======")

       completed_orders = 0

       for order in self.orders:

           if order.status == "Completed":

               completed_orders += 1

       print(f"Completed Orders: {completed_orders}")

       print(f"Total Sales: ${self.sales:.2f}")

       print("==========================\n")

   # ---------- Main Menu ----------

   def run(self):

       while True:

           print("====== RESTAURANT ORDERING SYSTEM ======")

           print("1. Add Menu Item")

           print("2. Display Menu")

           print("3. Update Menu Item")

           print("4. Remove Menu Item")

           print("5. Add Tables")

           print("6. Display Tables")

           print("7. Update Table Status")

           print("8. Create Order")

           print("9. Process Payment")

           print("10. Display Orders")

           print("11. Sales Report")

           print("12. Exit")

           choice = input("Enter choice: ")

           if choice == "1":

               self.add_menu_item()

           elif choice == "2":

               self.display_menu()

           elif choice == "3":

               self.update_menu_item()

           elif choice == "4":

               self.remove_menu_item()

           elif choice == "5":

               self.add_tables()

           elif choice == "6":

               self.display_tables()

           elif choice == "7":

               self.update_table_status()

           elif choice == "8":

               self.create_order()

           elif choice == "9":

               self.process_payment()

           elif choice == "10":

               self.display_orders()

           elif choice == "11":

               self.sales_report()

           elif choice == "12":

               print("Exiting system...")

               break

           else:

               print("Invalid choice.\n")


# ---------- Run Program ---------- 

system = RestaurantSystem()

system.run()
 