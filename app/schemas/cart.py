from pydantic import BaseModel
from typing import List


class CartItem(BaseModel):
    product_id: str
    product_name: str
    category: str
    quantity: int


class CartRecommendationRequest(BaseModel):
    cart_items: List[CartItem]
    available_products: List[str]
    recommendation_limit: int = 5


class CartRecommendation(BaseModel):
    product_id: str
    reason: str


class CartRecommendationResponse(BaseModel):
    recommendations: List[CartRecommendation]
    total_recommendations: int