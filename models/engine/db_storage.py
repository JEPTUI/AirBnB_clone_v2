#!/usr/bin/python3
"""Defines the class DatabaseStorage"""
from os import getenv
import models
from models.state import State
from models.city import City
from models.base_model import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Creates database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine to be linked to the MySQL database"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        db_dict = {}

        if cls != "":
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """close the current session"""
        self.__session.close()
