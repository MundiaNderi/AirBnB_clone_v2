#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlachelmy.orm import relationship, backref


class User(BaseModel):
    """This class defines a user by various attributes
    Attributes:
        email = email address
        password = password for you login
        first_name = first name
        last_name = last name
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        "Place",
        cascade="all,delete",
        backref=backref("user", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)

    reviews = relationship(
        "Review",
        cascade="all,delete",
        backref=backref("user", cascade="all, delete"),
        passive_deletes=True,
        single_parent=True
    )
