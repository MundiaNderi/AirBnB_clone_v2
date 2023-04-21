#!/usr/bin/python3
"""Module for DBstorage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "tests":
            Base.metadata.drop.all(self.__engine)

    def all(self, cls=None):
        """returns all objects of cls
        Query on the current databse session all objects of the given class
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        class_list = [
            State,
            City,
            User,
            Place,
            Review,
            Amenity
        ]
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """add object to db"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the db"""
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ deserialize JSON object """
        self.__session.close()
