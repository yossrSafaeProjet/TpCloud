from typing import Optional
from pydantic import BaseModel
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
class ProductBase(BaseModel):
    name:str
    description:str
    price: int
    category_id: int  # Ajouter la relation avec la catégorie
class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id:int

    class Config:
        orm_mode = True 

