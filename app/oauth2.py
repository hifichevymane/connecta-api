from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, models
from .database import get_db
from fastapi import Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session
# Config file that conects .env file
from .config import settings

# Config of JWT token function 
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

# Creating JWT token function
def create_access_token(data: dict):

    to_encode = data.copy()

    # Expire date of token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



# Veryfying JWT tokens
def verify_access_token(token: str, login_exception):

    try:
        # Decoding JWT token and getting user id
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        # If id doesn't exists -> raise exception
        if id is None:
            raise login_exception
        
        # Store fata from JWT token
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise login_exception
    
    return token_data


# Getting user id from JWT token
def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):

    login_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail='Could not validate login',
                                    headers={'WWW-Authenticate': "Bearer"})

    token = verify_access_token(token, login_exception)
    # Finding row with id == token.id
    user = db.query(models.UserModel).filter(models.UserModel.id == token.id).first()

    return user
