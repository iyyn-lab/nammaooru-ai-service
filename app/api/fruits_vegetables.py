from fastapi import APIRouter

from app.schemas.fruits_vegetables import (
    FruitsVegetablesRequest,
    FruitsVegetablesResponse,
    ProductSuggestion
)

router = APIRouter()


@router.post(
    "/recommendations/fruits-vegetables",
    response_model=FruitsVegetablesResponse
)
def get_fruits_vegetables_recommendations(
    request: FruitsVegetablesRequest
):
    recommendations = [
        ProductSuggestion(
            product_id=product.product_id,
            reason=f"{product.product_name} is a good addition to your groceries."
        )
        for product in request.available_products
        if product.category.lower() in ["fruit", "vegetable"]
    ][:request.recommendation_limit]

    return FruitsVegetablesResponse(
        recommendations=recommendations,
        total_recommendations=len(recommendations)
    )