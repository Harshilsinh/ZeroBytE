import datetime

class Educator:
    def __init__(self):
        self.tips_shown = set()
        self.user_logs = []
        self.waste_history = []

    def food_storage_tips(self):
        """Provide tips on storing common foods."""
        return {
            'milk': 'Keep in the back of the fridge at or below 4°C.',
            'bread': 'Store in a cool dry place, freeze for long-term storage.',
            'carrot': 'Keep in the crisper drawer in a perforated bag.',
            'herbs': 'Wrap in damp paper towel and refrigerate.'
        }

    def daily_tip(self):
        """Return a new food-saving tip each day."""
        tips = [
            "Use leftovers within 2–3 days.",
            "Freeze extra food before it spoils.",
            "Plan meals to avoid overbuying.",
            "Check expiry dates before shopping.",
            "Store apples away from other fruits."
        ]
        today = datetime.date.today().isoformat()
        index = int(today.replace("-", "")) % len(tips)
        return tips[index]

    def track_user_behavior(self, action, details=None):
        """Log user actions (e.g. 'logged_waste', 'saved_food')."""
        entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'action': action,
            'details': details or {}
        }
        self.user_logs.append(entry)

    def log_food_waste(self, item, quantity):
        """Record instances of food waste."""
        entry = {
            'item': item,
            'quantity': quantity,
            'date': datetime.date.today().isoformat()
        }
        self.waste_history.append(entry)
        self.track_user_behavior('logged_waste', entry)

    def weekly_summary(self):
        """Provide a summary of wasted items for the past 7 days."""
        cutoff = datetime.date.today() - datetime.timedelta(days=7)
        summary = {}
        for entry in self.waste_history:
            entry_date = datetime.date.fromisoformat(entry['date'])
            if entry_date >= cutoff:
                item = entry['item']
                summary[item] = summary.get(item, 0) + entry['quantity']
        return summary

    def quiz_user(self):
        """Return a food-saving quiz question."""
        return {
            "question": "How long can you keep cooked rice in the fridge?",
            "options": ["1 day", "3–4 days", "1 week", "2 weeks"],
            "answer": "3–4 days"
        }

    def recommend_content(self, topic):
        """Recommend content or articles based on a topic."""
        library = {
            'storage': "Read: 'Best Ways to Store Fresh Produce' at example.com/storage-tips",
            'meal planning': "Watch: 'Easy Weekly Meal Prep' on example.com/meal-planning",
            'leftovers': "Guide: 'Creative Leftover Recipes' from example.com/leftovers"
        }
        return library.get(topic.lower(), "No content found for this topic.")

    def generate_pledge(self, name):
        """Generate a personal food waste reduction pledge."""
        return f"I, {name}, pledge to reduce my food waste by planning meals, storing food properly, and using up leftovers."

    def calculate_impact(self):
        """Estimate the user's food waste impact based on history."""
        total_wasted = sum(entry['quantity'] for entry in self.waste_history)
        return {
            'total_items_wasted': total_wasted,
            'estimated_kg_co2_saved': round(total_wasted * 2.5, 2)  # Estimation logic
        }

    def behavior_insights(self):
        """Analyze user behavior to suggest improvements."""
        actions = [log['action'] for log in self.user_logs]
        if actions.count('logged_waste') > actions.count('saved_food'):
            return "You're wasting more than you're saving. Try meal planning!"
        elif not actions:
            return "Start tracking your habits to get insights!"
        else:
            return "Great job! Keep saving food and reducing waste."


# ---------------------------
# 🔍 Example Usage
# ---------------------------

educator = Educator()

print("Storage Tips:", educator.food_storage_tips())
print("Daily Tip:", educator.daily_tip())
educator.track_user_behavior('saved_food', {'item': 'bread', 'method': 'froze leftovers'})
educator.log_food_waste('carrot', 2)
educator.log_food_waste('milk', 1)
print("Weekly Summary:", educator.weekly_summary())
print("Quiz Question:", educator.quiz_user())
print("Recommend Content (Storage):", educator.recommend_content('storage'))
print("Pledge:", educator.generate_pledge('Alex'))
print("Waste Impact Estimate:", educator.calculate_impact())
print("Behavior Insight:", educator.behavior_insights())
