import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(40), nullable=False)
    
class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    vehicules_id = Column(Integer, ForeignKey('vehicules.id'))
   

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    especies = Column(String(250), nullable=False)
    role = Column(String(250), nullable=False)
    lifestatus = Column(String(250), nullable=False, unique=True)
    gender = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    galactic_location = Column(String(250), nullable=False)
    climate = Column(String(40), nullable=False)
    population = Column(String(40), nullable=False, unique=True)
    native_species = Column(String(40), nullable=False)
    govemment = Column(String(40), nullable=False)

class Vehicules(Base):
    __tablename__ = 'vehicules'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicule_class = Column(String(40), nullable=False)
    manufacturer = Column(String(40), nullable=False, unique=True)
    weapons = Column(String(40), nullable=False)
    passengers = Column(String(40), nullable=False)
    def to_dict(self):
        return {}
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
