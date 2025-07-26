from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL ="postgresql://username:password@localhost:5432/yourdb"
engine =create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey
from sqlalchemy.orm import relationship,declarative_base

Base =declarative_base()

class User(Base): 
    __tablename__="distribution_centers"
    id = Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender = Column(String)
    state = Column(String)
    street_address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude =Column(Float)
    traffic_source = Column(String)
    creayed_at =Column(DateTime)

    class Product(Base):
        __tablename__ ="products"
        id=Column(Integer,primary_key =True,autoincrement=True)
        cost =Column(Float)
        category = Column(String)
        name =Column(String)
        brand =Column(String)
        retail_price = Column(Float)
        department = Column(String)
        sku = Column(String)
        distribution_center_id= Column(Integer,ForeignKey('distribution_centers.id'))

        from database import engine,Base
        Base.metadata.craete_all(bind=engine)
