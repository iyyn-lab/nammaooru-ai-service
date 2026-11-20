from pydantic import BaseModel
from typing import List


class FamilyDetails(BaseModel):
    adults: int
    children: int
    children_age_groups: List[str]
    food_preference: str
    allergies: List[str]
    goals: List[str]


class RecentOrder(BaseModel):
    product_id: str
    product_name: str
    quantity: int


class HomeRecommendationRequest(BaseModel):
    user_id: str
    family_details: FamilyDetails
    recent_orders: List[RecentOrder]
    available_products: List[str]
    recommendation_limit: int = 10


class Recommendation(BaseModel):
    product_id: str
    reason: str


class HomeRecommendationResponse(BaseModel):
    recommendations: List[Recommendation]
    total_recommendations: int