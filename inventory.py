import json
from datetime import datetime,timedelta

class FoodInventoryManager:
    def _init_(self):
        self.inventory = {}

    def add_item(self, name, quantity, expiry_date):
        self.inventory[name] = {'quantity': quantity, 'expiry_date': expiry_date}

    def remove_item(self, name, quantity):
        if name in self.inventory:
            self.inventory[name]['quantity'] -= quantity
            if self.inventory[name]['quantity'] <= 0:
                del self.inventory[name]

    def check_near_expiry(self, days=3):
        today = datetime.today().date()
        return {name: details for name, details in self.inventory.items()
                if datetime.strptime(details['expiry_date'], '%Y-%m-%d').date() <= today + timedelta(days=days)}

    def inventory_summary(self):
        return self.inventory
#Krish patel
    def import_inventory(self, file_path):
        with open(file_path, 'r') as f:
            self.inventory = json.load(f)

    def export_inventory(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.inventory, f, indent=4)
