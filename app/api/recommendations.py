from fastapi import APIRouter

from app.schemas.recommendation import (
    HomeRecommendationRequest,
    HomeRecommendationResponse,
    Recommendation
)

router = APIRouter()

# dummy logic for now

@router.post(
    "/recommendations/home",
    response_model=HomeRecommendationResponse
)
def get_home_recommendations(
    request: HomeRecommendationRequest
):
    recommendations = []

    for product_id in request.available_products[:request.recommendation_limit]:
        recommendations.append(
            Recommendation(
                product_id=product_id,
                reason="A suitable grocery option for your family."
            )
        )

    return HomeRecommendationResponse(
        recommendations=recommendations,
        total_recommendations=len(recommendations)
    )