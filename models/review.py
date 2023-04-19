#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information
    place_id = place id
    user_id = user id
    text = review description
    """

    __tablename__ = "reviews"
    text = Column(String(1024),
                  nullable=False)
    place_id = Column(String(60),
                      ForeignKey("places.id", ondelete="CASCADE"),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
