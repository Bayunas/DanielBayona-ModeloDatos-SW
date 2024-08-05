import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class genderEnum(enum.Enum):
    male = 'male'
    female = 'female'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum(genderEnum), nullable=False)
    password = Column(String(10), nullable=False)
    email = Column(String(40), nullable=False, unique=True)

    favorite = relationship('Favorites', back_populates='user')

class FavoriteType(enum.Enum):
    planet = 'planet'
    character = 'character'

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key = True, nullable=False)
    item_type = Column(Enum(FavoriteType), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='favorites')
    planet = relationship('Planets', back_populates='favorites')
    character = relationship('Characters', back_populates='favorites')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(30), nullable=False)
    weather = Column(String(30), nullable=False)
    population = Column(Integer, nullable=False)
    size =  Column(Integer, nullable=False)

    favorites = relationship('Favorites', back_populates='planet')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    age = Column(Date, nullable=False)
    faction = Column(String(30), nullable=True)

    favorites = relationship('Favorites', back_populates='character')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
