from pydantic import BaseModel
from typing import List


class RecipeRequest(BaseModel):
    cart_items: List[str]
    available_products: List[str]
    recommendation_limit: int = 3


class RecipeSuggestion(BaseModel):
    recipe_name: str
    ingredients: List[str]
    description: str


class RecipeResponse(BaseModel):
    recipes: List[RecipeSuggestion]
    total_recipes: int