from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from schemas import (
    UserCreate, UserOut, PlayCreate, PlayUpdate, PlayOut,
    ActorCreate, ActorOut,
    DirectorCreate, DirectorOut,
    ShowTimeCreate, ShowTimeOut,
    CustomerCreate, CustomerOut,
    TicketCreate, TicketOut,
)
from crud import (
    create_user, get_user_by_id, get_all_users, update_user_role, delete_user,
    create_play, get_play, get_plays, update_play, delete_play,
    create_actor, get_actor, get_actors, update_actor, delete_actor,
    create_director, get_director, get_directors, update_director, delete_director,
    create_showtime, get_showtime, get_showtimes, update_showtime, delete_showtime,
    create_customer, get_customer, get_customers, update_customer, delete_customer,
    create_ticket, get_ticket, get_tickets, update_ticket, delete_ticket,
)
from hashing import hash_password  # assuming you have auth.py with this func

router = APIRouter()

#Users

@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    # Normally password hashing happens before calling this.
    # For demo, let's assume user.password is plain and hash it here or outside.

    hashed_pw = hash_password(user.password)
    return create_user(db, user, hashed_pw)

@router.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@router.get("/users/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_users(db, skip=skip, limit=limit)

@router.put("/users/{user_id}/role", response_model=UserOut)
def update_role(user_id: int, role: str, db: Session = Depends(get_db)):
    return update_user_role(db, user_id, role)

@router.delete("/users/{user_id}", response_model=UserOut)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)

#  Plays

@router.post("/plays/", response_model=PlayOut, status_code=status.HTTP_201_CREATED)
def create_new_play(play: PlayCreate, db: Session = Depends(get_db)):
    return create_play(db, play)

@router.get("/plays/{play_id}", response_model=PlayOut)
def read_play(play_id: int, db: Session = Depends(get_db)):
    return get_play(db, play_id)

@router.get("/plays/", response_model=List[PlayOut])
def read_plays(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_plays(db, skip=skip, limit=limit)

@router.put("/plays/{play_id}", response_model=PlayOut)
def update_existing_play(play_id: int, play: PlayUpdate, db: Session = Depends(get_db)):
    return update_play(db, play_id, play)

@router.delete("/plays/{play_id}", response_model=PlayOut)
def delete_play_by_id(play_id: int, db: Session = Depends(get_db)):
    return delete_play(db, play_id)

# Actors
@router.post("/actors/", response_model=ActorOut, status_code=status.HTTP_201_CREATED)
def create_new_actor(actor: ActorCreate, db: Session = Depends(get_db)):
    return create_actor(db, actor)

@router.get("/actors/{actor_id}", response_model=ActorOut)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    return get_actor(db, actor_id)

@router.get("/actors/", response_model=List[ActorOut])
def read_actors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_actors(db, skip=skip, limit=limit)

@router.put("/actors/{actor_id}", response_model=ActorOut)
def update_existing_actor(actor_id: int, actor_data: dict, db: Session = Depends(get_db)):
    return update_actor(db, actor_id, actor_data)

@router.delete("/actors/{actor_id}", response_model=ActorOut)
def delete_actor_by_id(actor_id: int, db: Session = Depends(get_db)):
    return delete_actor(db, actor_id)

# Directors

@router.post("/directors/", response_model=DirectorOut, status_code=status.HTTP_201_CREATED)
def create_new_director(director: DirectorCreate, db: Session = Depends(get_db)):
    return create_director(db, director)

@router.get("/directors/{director_id}", response_model=DirectorOut)
def read_director(director_id: int, db: Session = Depends(get_db)):
    return get_director(db, director_id)

@router.get("/directors/", response_model=List[DirectorOut])
def read_directors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_directors(db, skip=skip, limit=limit)

@router.put("/directors/{director_id}", response_model=DirectorOut)
def update_existing_director(director_id: int, director_data: dict, db: Session = Depends(get_db)):
    return update_director(db, director_id, director_data)

@router.delete("/directors/{director_id}", response_model=DirectorOut)
def delete_director_by_id(director_id: int, db: Session = Depends(get_db)):
    return delete_director(db, director_id)

# ShowTimes

@router.post("/showtimes/", response_model=ShowTimeOut, status_code=status.HTTP_201_CREATED)
def create_new_showtime(showtime: ShowTimeCreate, db: Session = Depends(get_db)):
    return create_showtime(db, showtime)

@router.get("/showtimes/{showtime_id}", response_model=ShowTimeOut)
def read_showtime(showtime_id: int, db: Session = Depends(get_db)):
    return get_showtime(db, showtime_id)

@router.get("/showtimes/", response_model=List[ShowTimeOut])
def read_showtimes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_showtimes(db, skip=skip, limit=limit)

@router.put("/showtimes/{showtime_id}", response_model=ShowTimeOut)
def update_existing_showtime(showtime_id: int, showtime_data: dict, db: Session = Depends(get_db)):
    return update_showtime(db, showtime_id, showtime_data)

@router.delete("/showtimes/{showtime_id}", response_model=ShowTimeOut)
def delete_showtime_by_id(showtime_id: int, db: Session = Depends(get_db)):
    return delete_showtime(db, showtime_id)

#  Customers

@router.post("/customers/", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_new_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.get("/customers/{customer_id}", response_model=CustomerOut)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(db, customer_id)

@router.get("/customers/", response_model=List[CustomerOut])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_customers(db, skip=skip, limit=limit)

@router.put("/customers/{customer_id}", response_model=CustomerOut)
def update_existing_customer(customer_id: int, customer_data: dict, db: Session = Depends(get_db)):
    return update_customer(db, customer_id, customer_data)

@router.delete("/customers/{customer_id}", response_model=CustomerOut)
def delete_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    return delete_customer(db, customer_id)

# Tickets

@router.post("/tickets/", response_model=TicketOut, status_code=status.HTTP_201_CREATED)
def create_new_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db, ticket)

@router.get("/tickets/{ticket_id}", response_model=TicketOut)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return get_ticket(db, ticket_id)

@router.get("/tickets/", response_model=List[TicketOut])
def read_tickets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tickets(db, skip=skip, limit=limit)

@router.put("/tickets/{ticket_id}", response_model=TicketOut)
def update_existing_ticket(ticket_id: int, ticket_data: dict, db: Session = Depends(get_db)):
    return update_ticket(db, ticket_id, ticket_data)

@router.delete("/tickets/{ticket_id}", response_model=TicketOut)
def delete_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    return delete_ticket(db, ticket_id)