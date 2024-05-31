#crud.py
from sqlalchemy.orm import Session
import models, schemas
#Fonction pour obtenir un produit par ID
def get_product (db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id==product_id).first()
#Fonction pour obtenir tous les produits avec pagination 
def get_products (db: Session, skip: int, limit: int = 10):
    return db.query (models.Product).offset(skip).limit(limit).all()
#Fonction pour créer un nouveau produit
def create_product(db: Session, product: schemas. ProductCreate):
    db_product = models. Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
#Fonction pour supprimer un produit par ID
def delete_product(db: Session, product_id: int):
    db_product =db.query(models.Product).filter(models.Product.id ==product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return db_product

#Fonction pour modifier un produit par ID
def update_product(product_id: int, product_update: schemas.ProductCreate, db: Session):
    db_product=db.query(models.Product).filter(models.Product.id ==product_id).first()
    if db_product:
        db_product.name = product_update.name
        db_product.description = product_update.description
        db_product.price = product_update.price
        
        # Commit les changements à la base de données
        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        # Si le produit n'existe pas, retourner None ou lever une exception
        return None