from fastapi import APIRouter

from app.schemas.order import (
    OrderNutritionRequest,
    OrderNutritionResponse
)

router = APIRouter()


@router.post(
    "/orders/nutrition-snapshot",
    response_model=OrderNutritionResponse
)
def get_order_nutrition_snapshot(request: OrderNutritionRequest):

    return OrderNutritionResponse(
        nutrition_summary=(
            "Known-item protein: approximately 100–115 g in your basket. "
            "Fresh Chicken: full 500 g pack, generic estimate of "
            "20–23 g protein per 100 g raw edible portion. "
            "Actual cut, edible portion and preparation may vary. "
            "This represents purchased-grocery protein, not one person's "
            "daily intake or target. Other items have unavailable nutrition "
            "and are excluded, not counted as zero."
        )
    )