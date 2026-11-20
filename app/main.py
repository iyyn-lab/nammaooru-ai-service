from fastapi import FastAPI
from app.api.recommendations import router as recommendation_router
from app.api.products import router as product_router
from app.api.cart import router as cart_router
from app.api.fruits_vegetables import router as fruits_vegetables_router
from app.api.orders import router as order_router
from app.api.recipes import router as recipe_router

app = FastAPI(
    title="Namma Ooru AI API",
    description="AI service for Namma Ooru application",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Namma Ooru AI Service is running"}


app.include_router(
    recommendation_router,
    prefix="/api/v1",
    tags=["Recommendations"]
)

app.include_router(
    product_router,
    prefix="/api/v1",
    tags=["Products"]
)

app.include_router(
    cart_router,
    prefix="/api/v1",
    tags=["Cart Recommendations"]
)

app.include_router(
    fruits_vegetables_router,
    prefix="/api/v1",
    tags=["Fruits & Vegetables"]
)

app.include_router(
    order_router,
    prefix="/api/v1",
    tags=["Order Nutrition"]
)

app.include_router(
    recipe_router,
    prefix="/api/v1",
    tags=["Recipe Ideas"]
)