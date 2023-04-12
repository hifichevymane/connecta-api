from fastapi import status, HTTPException, Response, Depends, APIRouter
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

# Create an object of APIRouter. prefix parameter with '/business_cards' is shortcut for our paths
# Tags parameter is used for structure paths in Swagger UI
router = APIRouter(
    prefix='/business_cards',
    tags=['Business Cards']
)

# Insted of '/' we could use '/business_cards' without prefix parameter in router object

# Get all business cards
@router.get('/', response_model=List[schemas.BusinessCard])
def get_business_cards(db: Session = Depends(get_db)):

    # Get all rows in a database
    all_business_cards = db.query(models.BusinessCardModel).all()
    
    return all_business_cards


# Create business card
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.BusinessCard)
def create_business_card(business_card: schemas.CreateBusinessCard, db: Session = Depends(get_db)):

    # Creating an object of BusinessCardModel
    new_business_card = models.BusinessCardModel(**business_card.dict())
    # Add a business card in a DB
    db.add(new_business_card)
    db.commit()
    db.refresh(new_business_card)
    
    return new_business_card


# Get business card by id
@router.get('/{id}', response_model=schemas.BusinessCard)
def get_business_card_by_id(id: int, db: Session = Depends(get_db)):

    # SELECT ... WHERE query
    business_card = db.query(models.BusinessCardModel).filter(models.BusinessCardModel.id == id).first()

    # If we didn't found a business card with that id -> 404 HTTP
    if not business_card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"business card with id {id} wasn't found")

    return business_card


# Delete a business card
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
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
@router.patch('/{id}', response_model=schemas.BusinessCard)
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

