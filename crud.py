from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import User, Play, Actor, Director, ShowTime, Customer, Ticket
from schemas import (
    UserCreate, PlayCreate, ActorCreate, DirectorCreate,
    ShowTimeCreate, CustomerCreate, TicketCreate,
    PlayUpdate
)


# Play CRUD


def create_play(db: Session, play: PlayCreate):
    new_play = Play(**play.dict())
    db.add(new_play)
    db.commit()
    db.refresh(new_play)
    return new_play

def get_play(db: Session, play_id: int):
    play = db.query(Play).filter(Play.id == play_id).first()
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play

def get_plays(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Play).offset(skip).limit(limit).all()

def update_play(db: Session, play_id: int, play_data: PlayUpdate):
    play = db.query(Play).filter(Play.id == play_id).first()
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    update_data = play_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(play, key, value)
    db.commit()
    db.refresh(play)
    return play

def delete_play(db: Session, play_id: int):
    play = db.query(Play).filter(Play.id == play_id).first()
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    db.delete(play)
    db.commit()
    return play


# Actor CRUD


def create_actor(db: Session, actor: ActorCreate):
    new_actor = Actor(**actor.dict())
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return new_actor

def get_actor(db: Session, actor_id: int):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

def get_actors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Actor).offset(skip).limit(limit).all()

def update_actor(db: Session, actor_id: int, actor_data: dict):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    for key, value in actor_data.items():
        setattr(actor, key, value)
    db.commit()
    db.refresh(actor)
    return actor

def delete_actor(db: Session, actor_id: int):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    db.delete(actor)
    db.commit()
    return actor


# Director CRUD


def create_director(db: Session, director: DirectorCreate):
    new_director = Director(**director.dict())
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director

def get_director(db: Session, director_id: int):
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

def get_directors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Director).offset(skip).limit(limit).all()

def update_director(db: Session, director_id: int, director_data: dict):
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    for key, value in director_data.items():
        setattr(director, key, value)
    db.commit()
    db.refresh(director)
    return director

def delete_director(db: Session, director_id: int):
    director = db.query(Director).filter(Director.id == director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    db.delete(director)
    db.commit()
    return director


# ShowTime CRUD


def create_showtime(db: Session, showtime: ShowTimeCreate):
    new_showtime = ShowTime(**showtime.dict())
    db.add(new_showtime)
    db.commit()
    db.refresh(new_showtime)
    return new_showtime

def get_showtime(db: Session, showtime_id: int):
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="ShowTime not found")
    return showtime

def get_showtimes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ShowTime).offset(skip).limit(limit).all()

def update_showtime(db: Session, showtime_id: int, showtime_data: dict):
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="ShowTime not found")
    for key, value in showtime_data.items():
        setattr(showtime, key, value)
    db.commit()
    db.refresh(showtime)
    return showtime

def delete_showtime(db: Session, showtime_id: int):
    showtime = db.query(ShowTime).filter(ShowTime.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="ShowTime not found")
    db.delete(showtime)
    db.commit()
    return showtime


# Customer CRUD


def create_customer(db: Session, customer: CustomerCreate):
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Customer).offset(skip).limit(limit).all()

def update_customer(db: Session, customer_id: int, customer_data: dict):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer_data.items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return customer


# Ticket CRUD


def create_ticket(db: Session, ticket: TicketCreate):
    new_ticket = Ticket(**ticket.dict())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

def get_tickets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ticket).offset(skip).limit(limit).all()

def update_ticket(db: Session, ticket_id: int, ticket_data: dict):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    for key, value in ticket_data.items():
        setattr(ticket, key, value)
    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(ticket)
    db.commit()
    return ticket


# User CRUD


def create_user(db: Session, user: UserCreate, hashed_password: str):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(
        username=user.username,
        hash_password=hashed_password,
        role=user.role or "customer"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user_role(db: Session, user_id: int, new_role: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role = new_role
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user
