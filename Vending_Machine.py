class VendingMachine:
    def __init__(self, num_items, item_price):
        """Initialize vending machine with the number of items and item price."""
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        """Handles a purchase request."""
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")

        total_cost = req_items * self.item_price

        if money < total_cost:
            raise ValueError("Not enough coins")

        # Reduce the number of items
        self.num_items -= req_items

        # Return change
        return money - total_cost

# Read initial values
num_items, item_price = map(int, input().split())
machine = VendingMachine(num_items, item_price)

# Read number of transactions
n = int(input())

# Process transactions
for _ in range(n):
    req_items, money = map(int, input().split())
    try:
        print(machine.buy(req_items, money))
    except ValueError as e:
        print(e)
