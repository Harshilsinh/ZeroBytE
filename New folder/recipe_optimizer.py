class RecipyOptimizer:
    def __init__(self, inventory):
        # inventory: dict of item -> quantity
        self.inventory = inventory

    def suggest_recipes(self, recipe_db):
        """Suggest recipes that can be fully made with current inventory."""
        suggestions = []
        for recipe, ingredients in recipe_db.items():
            if all(item in self.inventory and self.inventory[item] >= qty for item, qty in ingredients.items()):
                suggestions.append(recipe)
        return suggestions

    def optimize_serving_size(self, recipe):
        """Optimize servings based on current inventory."""
        return min(self.inventory.get(ing, 0) // qty for ing, qty in recipe.items())

    def predict_wastage(self, expiry_info):
        """Predict which items will go to waste soon (within 2 days)."""
        return [item for item, days in expiry_info.items() if days < 2]

    def substitute_ingredients(self, recipe, substitutes):
        """Substitute missing ingredients using alternatives."""
        new_recipe = {}
        for ing, qty in recipe.items():
            if self.inventory.get(ing, 0) >= qty:
                new_recipe[ing] = qty
            else:
                new_recipe[substitutes.get(ing, ing)] = qty
        return new_recipe

    def get_low_stock_items(self, threshold=2):
        """Return items with stock lower than threshold."""
        return [item for item, qty in self.inventory.items() if qty < threshold]

    def generate_shopping_list(self, recipe):
        """Return ingredients missing or insufficient for the recipe."""
        return {
            item: qty - self.inventory.get(item, 0)
            for item, qty in recipe.items()
            if self.inventory.get(item, 0) < qty
        }

    def track_used_ingredients(self, recipe):
        """Deduct used ingredients from inventory."""
        for item, qty in recipe.items():
            self.inventory[item] = max(0, self.inventory.get(item, 0) - qty)

    def estimate_nutritional_value(self, recipe, nutrition_db):
        """Estimate total nutrition values from recipe and nutrition DB."""
        total = {'calories': 0, 'protein': 0}
        for item, qty in recipe.items():
            data = nutrition_db.get(item, {})
            total['calories'] += data.get('calories', 0) * qty
            total['protein'] += data.get('protein', 0) * qty
        return total

    def flag_expiring_items(self, expiry_info, days_left=3):
        """Return items expiring in `days_left` or fewer."""
        return {item: days for item, days in expiry_info.items() if days <= days_left}

    def recommend_meal_plan(self, recipe_db, expiry_info):
        """Recommend recipes that use expiring items."""
        expiring = self.flag_expiring_items(expiry_info)
        plan = []
        for recipe, ingredients in recipe_db.items():
            if any(ing in expiring for ing in ingredients):
                plan.append(recipe)
        return plan


# ---------------------------
# 🔍 Example Usage
# ---------------------------

inventory = {'carrot': 3, 'potato': 2, 'milk': 1}
expiry_info = {'carrot': 1, 'potato': 4, 'milk': 2}
recipe_db = {
    'Soup': {'carrot': 2, 'potato': 1},
    'Smoothie': {'milk': 2},
    'Fries': {'potato': 3}
}
substitutes = {'milk': 'soy milk'}
nutrition_db = {'carrot': {'calories': 25, 'protein': 1}, 'potato': {'calories': 80, 'protein': 2}}

optimizer = RecipyOptimizer(inventory)

print("Suggested Recipes:", optimizer.suggest_recipes(recipe_db))
print("Max Servings of Soup:", optimizer.optimize_serving_size(recipe_db['Soup']))
print("Predicted Wastage:", optimizer.predict_wastage(expiry_info))
print("Substitute Recipe:", optimizer.substitute_ingredients({'milk': 2}, substitutes))
print("Low Stock Items:", optimizer.get_low_stock_items())
print("Shopping List for Fries:", optimizer.generate_shopping_list(recipe_db['Fries']))
optimizer.track_used_ingredients({'carrot': 2})
print("Inventory After Use:", optimizer.inventory)
print("Nutritional Value of Soup:", optimizer.estimate_nutritional_value(recipe_db['Soup'], nutrition_db))
print("Expiring Soon:", optimizer.flag_expiring_items(expiry_info))
print("Meal Plan for Expiring Items:", optimizer.recommend_meal_plan(recipe_db, expiry_info))
