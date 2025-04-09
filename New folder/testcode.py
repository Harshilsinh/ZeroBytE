from datetime import datetime
from inventory import FoodInventoryManager
from recipe_optimizer import RecipeOptimizer
from waste_analyzer import FoodWasteAnalyzer
from donation import DonationManager
from educator import FoodWasteEducator

# ----- Food Inventory Test -----
print("📦 Testing FoodInventoryManager")
inventory = FoodInventoryManager()
inventory.add_item("Milk", 2, "2025-04-10")
inventory.add_item("Bread", 3, "2025-04-12")
inventory.add_item("Eggs", 12, "2025-04-15")
inventory.remove_item("Bread", 1)
print("Inventory Summary:", inventory.inventory_summary())
print("Near Expiry (3 days):", inventory.check_near_expiry(3))
print("Storage Tips:", inventory.suggest_storage())

# ----- Recipe Optimizer Test -----
print("\n🍲 Testing RecipeOptimizer")
recipes = RecipeOptimizer()
recipes.recipes = {
    "French Toast": ["Eggs", "Milk", "Bread"],
    "Omelette": ["Eggs", "Cheese"],
    "Smoothie": ["Milk", "Banana"]
}
available_ingredients = ["Milk", "Eggs", "Bread"]
print("Possible Recipes:", recipes.generate_recipes(available_ingredients))
print("Substitute for 'eggs':", recipes.suggest_substitutions("eggs"))

# ----- Food Waste Analyzer Test -----
print("\n♻ Testing FoodWasteAnalyzer")
waste_analyzer = FoodWasteAnalyzer()
waste_analyzer.log_waste("Milk", 1, "Expired")
waste_analyzer.log_waste("Bread", 2, "Spoiled")
print("Waste Patterns:", waste_analyzer.analyze_waste_patterns())

# ----- Donation Manager Test -----
print("\n🎁 Testing DonationManager")
donation_manager = DonationManager()
donation_manager.schedule_donation(
    items={"Eggs": 6, "Milk": 1},
    center="Food Bank A",
    date="2025-04-15"
)
print("Donation History:", donation_manager.track_donation_history())
print("Donatable Items:", donation_manager.list_donatable_items(inventory.inventory_summary()))

# ----- Food Waste Educator Test -----
print("\n📚 Testing FoodWasteEducator")
tips = FoodWasteEducator.fetch_tips()
print("Education Tips:")
for tip in tips:
    print("-", tip)