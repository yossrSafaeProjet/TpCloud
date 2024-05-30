
from sqlalchemy import Column,Integer,String,create_engine

from Bdd import Base

class Product(Base):
    __tablename__="product"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),index=True)
    description=Column(String(100),index=True)
    price=Column(Integer)