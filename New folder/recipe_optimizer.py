class RecipeOptimizer:
    def _init_(self):
        self.recipes = {}

    def generate_recipes(self, ingredients):
        return [recipe for recipe, ing in self.recipes.items() if all(i in ingredients for i in ing)]

    def suggest_substitutions(self, missing_item):
        substitutions = {
            "milk": "almond milk",
            "eggs": "flax seeds + water",
            "butter": "olive oil"
        }
        return substitutions.get(missing_item, "No suggestion available")