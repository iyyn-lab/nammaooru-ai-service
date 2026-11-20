from fastapi import APIRouter

from app.schemas.recipe import (
    RecipeRequest,
    RecipeResponse,
    RecipeSuggestion
)

router = APIRouter()


@router.post(
    "/recommendations/recipes",
    response_model=RecipeResponse
)
def get_recipe_ideas(request: RecipeRequest):

    recipes = [
        RecipeSuggestion(
            recipe_name="Chicken Vegetable Stir Fry",
            ingredients=[
                "Fresh Chicken",
                "Carrot",
                "Capsicum"
            ],
            description="A simple meal using chicken and fresh vegetables."
        ),
        RecipeSuggestion(
            recipe_name="Vegetable Rice",
            ingredients=[
                "Rice",
                "Carrot",
                "Beans"
            ],
            description="A simple rice dish with fresh vegetables."
        )
    ]

    recipes = recipes[:request.recommendation_limit]

    return RecipeResponse(
        recipes=recipes,
        total_recipes=len(recipes)
    )