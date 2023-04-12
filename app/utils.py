from passlib.context import CryptContext

# Password hashing config
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


# Hashing a password function
def hash(password: str):
    return pwd_context.hash(password)


# Verifying a password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
