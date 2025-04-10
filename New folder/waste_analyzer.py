import statistics
from collections import defaultdict

class WasteAnalyzer:
    def __init__(self):
        self.waste_log = []  # Stores records like {'item': 'carrot', 'quantity': 2, 'date': '2025-04-01'}

    def log_waste(self, item, quantity, date):
        """Log a new waste event."""
        self.waste_log.append({'item': item, 'quantity': quantity, 'date': date})

    def total_waste(self):
        """Total quantity of all wasted items."""
        return sum(entry['quantity'] for entry in self.waste_log)

    def waste_by_item(self):
        """Total waste grouped by item."""
        result = defaultdict(int)
        for entry in self.waste_log:
            result[entry['item']] += entry['quantity']
        return dict(result)

    def most_wasted_item(self):
        """Find the item with the highest waste quantity."""
        waste_data = self.waste_by_item()
        return max(waste_data.items(), key=lambda x: x[1], default=(None, 0))

    def waste_on_date(self, target_date):
        """Total waste on a specific date."""
        return sum(entry['quantity'] for entry in self.waste_log if entry['date'] == target_date)

    def average_daily_waste(self):
        """Average waste per day."""
        daily = defaultdict(int)
        for entry in self.waste_log:
            daily[entry['date']] += entry['quantity']
        return round(statistics.mean(daily.values()), 2) if daily else 0.0

    def waste_trend(self):
        """Show daily waste trend (date -> total)."""
        trend = defaultdict(int)
        for entry in self.waste_log:
            trend[entry['date']] += entry['quantity']
        return dict(sorted(trend.items()))

    def item_waste_percentage(self):
        """Percentage of total waste by item."""
        total = self.total_waste()
        item_data = self.waste_by_item()
        return {item: round((qty / total) * 100, 2) for item, qty in item_data.items()} if total else {}

    def filter_waste_by_item(self, item_name):
        """Filter waste logs by item."""
        return [entry for entry in self.waste_log if entry['item'] == item_name]

    def clear_waste_data(self):
        """Clear all logged waste data."""
        self.waste_log.clear()

# ---------------------------
# 🔍 Example Usage
# ---------------------------

analyzer = WasteAnalyzer()

# Log waste entries
analyzer.log_waste('carrot', 2, '2025-04-01')
analyzer.log_waste('potato', 1, '2025-04-01')
analyzer.log_waste('milk', 3, '2025-04-02')
analyzer.log_waste('carrot', 1, '2025-04-03')

# Use functions
print("Total Waste:", analyzer.total_waste())
print("Waste by Item:", analyzer.waste_by_item())
print("\Most Wasted Item:", analyzer.most_wasted_item())
print("Waste on 2025-04-01:", analyzer.waste_on_date('2025-04-01'))
print("Average Daily Waste:", analyzer.average_daily_waste())
print("Waste Trend:", analyzer.waste_trend())
print("Waste Percentage by Item:", analyzer.item_waste_percentage())
print("Filter by Item 'carrot':", analyzer.filter_waste_by_item('carrot'))

analyzer.clear_waste_data()
print("🧹 Waste Log After Clear:", analyzer.waste_log)
\
