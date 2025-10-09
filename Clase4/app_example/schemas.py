from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    unit_price_cents: int = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    description: str | None = None

class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    unit_price_cents: int | None = Field(None, gt=0)
    stock: int | None = Field(None, ge=0)
    description: str | None = None


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None

class CategoryUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
