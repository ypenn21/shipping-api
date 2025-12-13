from sqlalchemy import Column, Integer, String, Float
from connect_connector import Base

class Package(Base):
    __tablename__ = 'packages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String, nullable=False)
    height = Column(Float)
    width = Column(Float)
    depth = Column(Float)
    weight = Column(Float)
    special_handling_instructions = Column(String)
