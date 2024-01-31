class RetailItem:
    def __init__(self, item, units, price):
        self.item = item
        self.units = units
        self.price = price

    def get_info(self):
        print(self.item, self.units, self.price)

if __name__ == "__main__":
    Items = [
        RetailItem("Jacket", 12, 59.95),
        RetailItem("Designer Jeans", 40, 34.95),
        RetailItem("Shirt", 20, 24.95)
    ]

    for i in range(0,3):
        Items[i].get_info()
