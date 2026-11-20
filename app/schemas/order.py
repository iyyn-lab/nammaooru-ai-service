from pydantic import BaseModel
from typing import List, Optional


class OrderNutritionItem(BaseModel):
    product_id: str
    product_name: str
    quantity: float
    pack_size: str
    protein_min_g_per_100g: Optional[float] = None
    protein_max_g_per_100g: Optional[float] = None
    nutrition_status: str


class OrderNutritionRequest(BaseModel):
    items: List[OrderNutritionItem]


class OrderNutritionResponse(BaseModel):
    nutrition_summary: str