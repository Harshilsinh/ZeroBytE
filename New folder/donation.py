from datetime import datetime, timedelta


class Donation:
    def __init__(self):
        self.donations = []  # List of donation entries

    def add_donation(self, donor_name, items, expiry_date):
        """Add a new donation record."""
        self.donations.append({
            'donor': donor_name,
            'items': items,
            'expiry': expiry_date,
            'received': False
        })

    def list_pending_donations(self):
        """List donations that haven't been received yet."""
        return [d for d in self.donations if not d['received']]

    def mark_received(self, donor_name):
        """Mark donation as received based on donor name."""
        for d in self.donations:
            if d['donor'] == donor_name and not d['received']:
                d['received'] = True

    def filter_expired_donations(self):
        """Return donations with expired items."""
        today = datetime.today().date()
        return [d for d in self.donations if datetime.strptime(d['expiry'], '%Y-%m-%d').date() < today]

    def upcoming_expiry_donations(self, days=3):
        """List donations that will expire in the next `days` days."""
        today = datetime.today().date()
        upcoming = today + timedelta(days=days)
        return [d for d in self.donations if today <= datetime.strptime(d['expiry'], '%Y-%m-%d').date() <= upcoming]

    def match_donations_to_needs(self, needs):
        """Match available donations to food bank needs."""
        matched = []
        for d in self.donations:
            if not d['received']:
                for item in d['items']:
                    if item in needs:
                        matched.append(d)
                        break
        return matched

    def get_donation_summary(self):
        """Return a summary count of donated items."""
        summary = {}
        for d in self.donations:
            for item, qty in d['items'].items():
                summary[item] = summary.get(item, 0) + qty
        return summary

    def remove_expired_donations(self):
        """Remove expired donations from records."""
        today = datetime.today().date()
        self.donations = [
            d for d in self.donations if datetime.strptime(d['expiry'], '%Y-%m-%d').date() >= today
        ]

    def get_donors(self):
        """Get a list of unique donor names."""
        return list(set(d['donor'] for d in self.donations))

    def schedule_pickups(self):
        """Auto-schedule pickups for donations not yet received."""
        schedule = {}
        for d in self.list_pending_donations():
            pickup_day = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
            schedule[d['donor']] = pickup_day
        return schedule


# ---------------------------
# 🔍 Example Usage
# ---------------------------

donate = Donation()

# Add sample donations
donate.add_donation("Alice", {"bread": 5, "milk": 2}, "2025-04-10")
donate.add_donation("Bob", {"rice": 10}, "2025-04-12")
donate.add_donation("Charlie", {"milk": 1, "apples": 4}, "2025-04-08")

# Use the functions
print("Pending Donations:", donate.list_pending_donations())
donate.mark_received("Alice")
print("After Marking Alice Received:", donate.list_pending_donations())
print("Expired Donations:", donate.filter_expired_donations())
print("Expiring Soon:", donate.upcoming_expiry_donations())
print("Matched to Needs:", donate.match_donations_to_needs(["milk", "bread"]))
print("Donation Summary:", donate.get_donation_summary())
donate.remove_expired_donations()
print("After Removing Expired:", donate.donations)
print("Donors:", donate.get_donors())
print("Pickup Schedule:", donate.schedule_pickups())
