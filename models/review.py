#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlachmey.sql.schema import ForeignKey
from sqlalchemy impoort Column, String, foreignKey
from models import storage_type


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if storage_type == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(58), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
