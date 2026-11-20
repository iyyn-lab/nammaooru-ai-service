from pydantic import BaseModel
from typing import List


class AvailableProduct(BaseModel):
    product_id: str
    product_name: str
    category: str


class FruitsVegetablesRequest(BaseModel):
    available_products: List[AvailableProduct]
    recommendation_limit: int = 5


class ProductSuggestion(BaseModel):
    product_id: str
    reason: str


class FruitsVegetablesResponse(BaseModel):
    recommendations: List[ProductSuggestion]
    total_recommendations: int