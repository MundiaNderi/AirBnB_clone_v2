#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel):
    """ The city class, contains state ID and name 
    Attributes:
        state_id = The state id
        name = input name
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(string(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)

    places = relationship(
        "Place"
        cascade="all"
        backref=backref("cities", cascade="all"),
        passive_deletes=True
    )
