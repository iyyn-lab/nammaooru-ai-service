from fastapi import APIRouter

from app.schemas.cart import (
    CartRecommendationRequest,
    CartRecommendationResponse,
    CartRecommendation
)

router = APIRouter()


@router.post(
    "/recommendations/cart",
    response_model=CartRecommendationResponse
)
def get_cart_recommendations(request: CartRecommendationRequest):

    cart_product_ids = {
        item.product_id for item in request.cart_items
    }

    available_products = [
        product_id
        for product_id in request.available_products
        if product_id not in cart_product_ids
    ]

    recommendations = [
        CartRecommendation(
            product_id=product_id,
            reason="Complements the items already in your cart."
        )
        for product_id in available_products[:request.recommendation_limit]
    ]

    return CartRecommendationResponse(
        recommendations=recommendations,
        total_recommendations=len(recommendations)
    )