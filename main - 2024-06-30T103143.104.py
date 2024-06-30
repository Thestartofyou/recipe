import json

# Sample database of recipes
recipes = {
    "Pasta Carbonara": ["pasta", "eggs", "parmesan", "bacon", "black pepper"],
    "Tomato Soup": ["tomatoes", "onions", "garlic", "vegetable broth", "olive oil"],
    "Grilled Cheese Sandwich": ["bread", "cheese", "butter"],
    "Pancakes": ["flour", "milk", "eggs", "sugar", "baking powder"],
}

def get_user_ingredients():
    ingredients = input("Enter the ingredients you have, separated by commas: ")
    return [item.strip().lower() for item in ingredients.split(",")]

def find_matching_recipes(user_ingredients):
    matching_recipes = {}
    for recipe, ingredients in recipes.items():
        if all(item in user_ingredients for item in ingredients):
            matching_recipes[recipe] = ingredients
        else:
            missing = [item for item in ingredients if item not in user_ingredients]
            matching_recipes[recipe] = {"ingredients": ingredients, "missing": missing}
    return matching_recipes

def print_recipe_suggestions(matching_recipes):
    for recipe, details in matching_recipes.items():
        if isinstance(details, list):
            print(f"You can make: {recipe}")
        else:
            print(f"{recipe}:")
            print(f"  You have: {', '.join([item for item in details['ingredients'] if item not in details['missing']])}")
            print(f"  You need: {', '.join(details['missing'])}")

def main():
    user_ingredients = get_user_ingredients()
    matching_recipes = find_matching_recipes(user_ingredients)
    print_recipe_suggestions(matching_recipes)

if __name__ == "__main__":
    main()
