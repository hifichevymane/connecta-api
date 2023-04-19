from pydantic import BaseModel, EmailStr

# Business card schema
class BusinessCardBase(BaseModel):

    company_name: str
    company_services_type: str
    company_description: str
    company_phone_number: str
    company_instagram: str | None = None
    company_telegram: str | None = None
    company_address: str
    company_website: str | None = None


# Create a business card schema
class CreateBusinessCard(BusinessCardBase):
    pass


# Update schema of business card
class UpdateBusinessCard(BusinessCardBase):

    company_name: str | None = None
    company_services_type: str | None = None
    company_description: str | None = None
    company_phone_number: str | None = None
    company_address: str | None = None


# Response schema
class BusinessCard(BusinessCardBase):

    id: int
    owner_id: int

    class Config:
        orm_mode = True


# A User schema
class UserCreate(BaseModel):

    first_name: str
    last_name: str
    email: EmailStr
    password: str


# User response schema
class User(BaseModel):

    id: int
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True


# User Login schema
class UserLogin(BaseModel):

    email: EmailStr
    password: str


# Token schema
class Token(BaseModel):

    access_token: str
    token_type: str


# Token Data schema
class TokenData(BaseModel):

    # Optional value
    id: str | None = None


# Response schema for getting user's posts
class BusinessCardsUsers(BaseModel):

    user_id: int
    business_card: BusinessCard

    class Config:
        orm_mode = True
