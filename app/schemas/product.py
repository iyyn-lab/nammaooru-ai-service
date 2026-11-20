from pydantic import BaseModel
from typing import Optional


class ProductNutrition(BaseModel):
    protein_g_per_100g: Optional[float] = None
    carbohydrates_g_per_100g: Optional[float] = None
    fat_g_per_100g: Optional[float] = None
    calories_per_100g: Optional[float] = None
    status: str


class ProductDetails(BaseModel):
    product_id: str
    product_name: str
    category: str
    pack_size: str
    description: str
    nutrition: ProductNutrition


class ProductNutritionRequest(BaseModel):
    product_details: ProductDetails


class ProductNutritionResponse(BaseModel):
    product_id: str
    nutrition_summary: str
    nutrition_status: str
    benefits: list[str]
    disclaimer: str