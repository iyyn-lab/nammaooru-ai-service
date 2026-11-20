from fastapi import APIRouter

from app.schemas.product import (
    ProductNutritionRequest,
    ProductNutritionResponse
)

router = APIRouter()


@router.post(
    "/products/nutrition",
    response_model=ProductNutritionResponse
)
def get_product_nutrition(request: ProductNutritionRequest):

    product = request.product_details

    return ProductNutritionResponse(
        product_id=product.product_id,
        nutrition_summary="Good source of protein.",
        nutrition_status=product.nutrition.status,
        benefits=[
            "Provides protein",
            "Supports muscle maintenance"
        ],
        disclaimer="Nutritional values may vary depending on preparation."
    )