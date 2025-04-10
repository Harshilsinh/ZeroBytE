class FoodInventory:
    def __init__(self):
        # Inventory format: { item: {'quantity': int, 'expiry_days': int} }
        self.inventory = {}

    def add_item(self, item, quantity, expiry_days):
        """Add or update an item in the inventory."""
        if item in self.inventory:
            self.inventory[item]['quantity'] += quantity
            self.inventory[item]['expiry_days'] = min(self.inventory[item]['expiry_days'], expiry_days)
        else:
            self.inventory[item] = {'quantity': quantity, 'expiry_days': expiry_days}

    def remove_item(self, item, quantity):
        """Remove a quantity of an item from inventory."""
        if item in self.inventory:
            self.inventory[item]['quantity'] -= quantity
            if self.inventory[item]['quantity'] <= 0:
                del self.inventory[item]

    def get_item(self, item):
        """Return info about a specific item."""
        return self.inventory.get(item, None)

    def list_inventory(self):
        """List all items in the inventory."""
        return self.inventory

    def check_expiring_items(self, days=2):
        """Get items expiring in or before given days."""
        return {item: info for item, info in self.inventory.items() if info['expiry_days'] <= days}

    def decrement_expiry(self):
        """Simulate passage of a day by reducing expiry days."""
        expired_items = []
        for item in list(self.inventory.keys()):
            self.inventory[item]['expiry_days'] -= 1
            if self.inventory[item]['expiry_days'] <= 0:
                expired_items.append(item)
                del self.inventory[item]
        return expired_items

    def restock_items(self, items):
        """Restock multiple items."""
        for item, details in items.items():
            self.add_item(item, details['quantity'], details['expiry_days'])

    def get_low_stock(self, threshold=2):
        """Return items with quantity below threshold."""
        return {item: info for item, info in self.inventory.items() if info['quantity'] < threshold}

    def get_total_quantity(self):
        """Return total count of all items."""
        return sum(info['quantity'] for info in self.inventory.values())

    def clear_inventory(self):
        """Clear all items (for testing or reset)."""
        self.inventory = {}
# Create the food inventory
inventory = FoodInventory()

# Add some items
inventory.add_item('carrot', 5, 3)
inventory.add_item('milk', 2, 1)
inventory.add_item('bread', 1, 2)

# Print full inventory
print("Inventory:", inventory.list_inventory())

# Remove some items
inventory.remove_item('carrot', 2)
print("After Removing Carrots:", inventory.list_inventory())

# Check a single item
print("Check Milk:", inventory.get_item('milk'))

# Check for expiring items
print("Expiring Soon:", inventory.check_expiring_items(days=2))

# Simulate a day passing
expired = inventory.decrement_expiry()
print("After a Day - Expired Items:", expired)
print("Updated Inventory:", inventory.list_inventory())

# Restock new items
inventory.restock_items({'apple': {'quantity': 4, 'expiry_days': 5}})
print("After Restocking:", inventory.list_inventory())

# Low stock warning
print("Low Stock Items:", inventory.get_low_stock())

# Total quantity in stock
print("Total Items Quantity:", inventory.get_total_quantity())

# Clear all items
inventory.clear_inventory()
print("Cleared Inventory:", inventory.list_inventory())
