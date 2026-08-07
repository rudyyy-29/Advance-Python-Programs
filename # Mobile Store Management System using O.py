# Mobile Store Management System using Object-Oriented Programming

class Mobile:
    def __init__(self, mobile_id, brand, model, price):
        self.mobile_id = mobile_id
        self.brand = brand
        self.model = model
        self.price = price

    # Categorize mobile based on price
    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display_mobile(self):
        print(f"Mobile ID : {self.mobile_id}")
        print(f"Brand     : {self.brand}")
        print(f"Model     : {self.model}")
        print(f"Price     : ₹{self.price}")
        print(f"Category  : {self.category()}")
        print("-" * 30)


class Store:
    def __init__(self):
        self.mobiles = []

    # Add a new mobile
    def add_mobile(self, mobile):
        self.mobiles.append(mobile)
        print("Mobile added successfully!")

    # Display all mobiles
    def display_mobiles(self):
        if len(self.mobiles) == 0:
            print("No mobiles available.")
        else:
            print("\n------ Mobile List ------")
            for mobile in self.mobiles:
                mobile.display_mobile()

    # Search mobile by ID
    def search_mobile(self, mobile_id):
        for mobile in self.mobiles:
            if mobile.mobile_id == mobile_id:
                return mobile
        return None


# ---------------- Main Program ---------------- #

store = Store()

while True:
    print("\n====== Mobile Store Management System ======")
    print("1. Add Mobile")
    print("2. Display Mobiles")
    print("3. Search Mobile")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mobile_id = int(input("Enter Mobile ID: "))
        brand = input("Enter Brand: ")
        model = input("Enter Model: ")
        price = float(input("Enter Price: "))

        mobile = Mobile(mobile_id, brand, model, price)
        store.add_mobile(mobile)

    elif choice == "2":
        store.display_mobiles()

    elif choice == "3":
        mobile_id = int(input("Enter Mobile ID to search: "))
        mobile = store.search_mobile(mobile_id)

        if mobile:
            print("\nMobile Found")
            mobile.display_mobile()
        else:
            print("Mobile not found.")

    elif choice == "4":
        print("Thank you for using Mobile Store Management System.")
        break

    else:
        print("Invalid choice! Please try again.")