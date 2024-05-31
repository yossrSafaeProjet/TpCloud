from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from Bdd import SessionLocal, engine

# Crée les tables dans la base de données
models.Base.metadata.create_all(bind=engine)

# Crée une instance de l'application FastAPI
app = FastAPI()

# Dépendance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.get("/categories", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 10, search: str = None, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit, search=search)
    return categories

@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    return category

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product

@app.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product

@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.update_product(product_id=product_id, product_update=product,db=db)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return db_product

@app.get("/products/category/{category_id}", response_model=List[schemas.Product])
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = crud.filter_products_by_category(db, category_id)
    return products