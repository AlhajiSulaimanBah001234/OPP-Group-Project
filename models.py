from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from database import Base


# User Authentication Table

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    role = Column(String, default="customer")


# Play Table

class Play(Base):
    __tablename__ = "plays"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    synopsis = Column(Text)
    duration = Column(String)

    showtimes = relationship("ShowTime", back_populates="play")
    tickets = relationship("Ticket", back_populates="play")
    actors = relationship("Actor", back_populates="play")
    directors = relationship("Director", back_populates="play")


#  Table For Actor

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    date_of_birth = Column(DateTime)
    play_id = Column(Integer, ForeignKey("plays.id"))

#(One-to-Many with Play)
    play = relationship("Play", back_populates="actors")


# Table for Director

class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    play_id = Column(Integer, ForeignKey("plays.id"))

# One-to-Many with Play
    play = relationship("Play", back_populates="directors")


#  Table For ShowTime

class ShowTime(Base):
    __tablename__ = "showtimes"
    id = Column(Integer, primary_key=True, index=True)
    date_and_time = Column(DateTime)
    play_id = Column(Integer, ForeignKey("plays.id"))

    play = relationship("Play", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime")


# Table for Customer

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    address = Column(String)

    tickets = relationship("Ticket", back_populates="customer")


#  Table Ticket
class Ticket(Base):
    __tablename__ = "tickets"

    seat_row_no = Column(Integer, primary_key=True)
    seat_no = Column(Integer, primary_key=True)
    showtime_id = Column(Integer, ForeignKey("showtimes.id"), primary_key=True)
    play_id = Column(Integer, ForeignKey("plays.id"), primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), primary_key=True)

    ticket_no = Column(String(10), unique=True, nullable=True)
    price = Column(Numeric(10, 2))

#(Composite PK)

    showtime = relationship("ShowTime", back_populates="tickets")
    play = relationship("Play", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")