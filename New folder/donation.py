class DonationManager:
    def __init__(self):
        self.donations = []

    def schedule_donation(self, items, center, date):
        self.donations.append({'items': items, 'center': center, 'date': date})

    def track_donation_history(self):
        return self.donations

    def list_donatable_items(self, inventory):
        return {item: details for item, details in inventory.items() if details['quantity'] > 0}