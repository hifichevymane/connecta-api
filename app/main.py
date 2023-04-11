from fastapi import FastAPI, status, HTTPException, Response, Depends
from . import schemas, models, utils
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

# Creating all tables in database if not exists
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all business Cards
@app.get('/business_cards', response_model=List[schemas.BusinessCard])
def get_business_cards(db: Session = Depends(get_db)):

    # Получение списка всех обьектов бд
    all_business_cards = db.query(models.BusinessCardModel).all()
    
    return all_business_cards


# Create business card
@app.post('/business_cards', status_code=status.HTTP_201_CREATED, response_model=schemas.BusinessCard)
def create_business_card(business_card: schemas.CreateBusinessCard, db: Session = Depends(get_db)):

    # Creating an object of BusinessCardModel
    new_business_card = models.BusinessCardModel(**business_card.dict())
    # Add a business card in a DB
    db.add(new_business_card)
    db.commit()
    db.refresh(new_business_card)
    
    return new_business_card


# Get business card by id
@app.get('/business_cards/{id}', response_model=schemas.BusinessCard)
def get_business_card_by_id(id: int, db: Session = Depends(get_db)):

    # SELECT ... WHERE query
    business_card = db.query(models.BusinessCardModel).filter(models.BusinessCardModel.id == id).first()

    # If we didn't found a business card with that id -> 404 HTTP
    if not business_card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")

    return business_card


# Delete a business card
@app.delete('/business_cards/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_business_card(id: int, db: Session = Depends(get_db)):

    # Find a business card by id
    business_card = db.query(models.BusinessCardModel).filter(models.BusinessCardModel.id == id)

    # If this card doesn't exists -> 404 HTTP RESPONSE
    if not business_card.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")
    
    # Delete a business card and save changes
    business_card.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update a business card
@app.patch('/business_cards/{id}', response_model=schemas.BusinessCard)
def update_business_card(id: int, updated_business_card: schemas.UpdateBusinessCard, db: Session = Depends(get_db)):

    # Find query and saving business_card_query.first() in business_card
    business_card_query = db.query(models.BusinessCardModel).filter(models.BusinessCardModel.id == id)
    business_card = business_card_query.first()

    # If this card doesn't exists -> 404 HTTP RESPONSE
    if not business_card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")
    
    # Update business card with id and saving results
    business_card_query.update(updated_business_card.dict(exclude_unset=True), synchronize_session=False)
    db.commit()

    return business_card_query.first()


# Creating a new user
@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Creating a hash of a password
    user.password = utils.hash(user.password)

    # Creating an object of a User model
    new_user = models.UserModel(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
