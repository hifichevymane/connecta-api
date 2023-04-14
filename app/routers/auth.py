from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, models, utils, oauth2

router = APIRouter(tags=['Login'])


# Login
@router.post('/login')
def login(user_login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    # Find user by email
    user = db.query(models.UserModel).filter(models.UserModel.email == user_login_data.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid login data")

    # If user entered a wrong password
    if not utils.verify(user_login_data.password ,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid password')
    
    # Creating an access token for login
    access_token = oauth2.create_access_token(data={'user_id': user.id})

    # Returning JWT Token
    return {'access_token': access_token, 'token_type': 'bearer'}
