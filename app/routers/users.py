from fastapi import status, HTTPException, Depends, APIRouter
from .. import schemas, models, utils
from ..database import get_db
from sqlalchemy.orm import Session

# Create an object of APIRouter. prefix parameter with '/users' is shortcut for our paths
router = APIRouter(
    prefix='/users'
)

# Insted of '/' we could use '/users' without prefix parameter in router object

# Creating a new user
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Creating a hash of a password
    user.password = utils.hash(user.password)

    # Creating an object of a User model
    new_user = models.UserModel(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get user by id
@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} wasn't found!")
    
    return user
