from datetime import datetime, timedelta
class FoodWasteAnalyzer:
    def __init__(self):
        self.waste_log = []

    def log_waste(self, item, quantity, reason):
        self.waste_log.append({'item': item, 'quantity': quantity, 'reason': reason, 'date': str(datetime.today().date())})

    def analyze_waste_patterns(self):
        waste_counts = {}
        for entry in self.waste_log:
            waste_counts[entry['item']] = waste_counts.get(entry['item'], 0) + entry['quantity']
        return waste_counts