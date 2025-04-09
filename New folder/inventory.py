import json
from datetime import datetime,timedelta

import json
from datetime import datetime, timedelta

class FoodInventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity, expiry_date):
        #adds food items to the inventry.
        if name in self.inventory:
            self.inventory[name]['quantity'] += quantity  # Update quantity if item exists
        else:
            self.inventory[name] = {'quantity': quantity, 'expiry_date': expiry_date}

    def remove_item(self, name, quantity):
        #Removes a specified quantity of an item from inventory
        if name in self.inventory:
            self.inventory[name]['quantity'] -= quantity
            if self.inventory[name]['quantity'] <= 0:
                del self.inventory[name]

    def check_near_expiry(self, days=3):
        #Returns items that are near expiry within the given number of days
        today = datetime.today().date()
        return {name: details for name, details in self.inventory.items()
                if datetime.strptime(details['expiry_date'], '%Y-%m-%d').date() <= today + timedelta(days=days)}

    def inventory_summary(self):
        #Returns the current state of the inventory.
        return self.inventory

    def import_inventory(self, file_path):
        #Imports inventory data from a JSON file.
        with open(file_path, 'r') as f:
            self.inventory = json.load(f)

    def export_inventory(self, file_path):
        #Exports inventory data to a JSON file.
        with open(file_path, 'w') as f:
            json.dump(self.inventory, f, indent=4)
             
    def suggest_storage(self):
            storage_tips = {
                "fridge": "Keep dairy, cooked meals, and perishables in the fridge.",
                "freezer": "Freeze meats, bread, and frozen vegetables.",
                "pantry": "Store dry goods like rice, pasta, and canned foods in a cool, dry place."
            }
            return storage_tips

    # Example Usage
    if __name__ == "__main__":
        manager = FoodInventoryManager()

        # Adding sample food items
        manager.add_item("Apples", 10, "2025-04-30")
        manager.add_item("Milk", 2, "2025-04-04")
        manager.add_item("Bread", 5, "2025-04-27")
        manager.add_item("Cheese", 1, "2025-04-05") 

        # Printing inventory summary
        print("Inventory Summary:", manager.inventory_summary())

        # Checking near expiry items
        print("Near Expiry Items:", manager.check_near_expiry(5))
