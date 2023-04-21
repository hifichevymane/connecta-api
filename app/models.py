from .database import Base
from sqlalchemy import Column, Text, String, Integer, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship

# Database table 'business_card'
class BusinessCardModel(Base):

    __tablename__ = 'business_card'

    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    company_name = Column(String(30), nullable=False)
    company_services_type = Column(String(50), nullable=False)
    company_description = Column(Text, nullable=False)
    company_phone_number = Column(String(14), nullable=False)
    company_instagram = Column(String(50), default=None)
    company_telegram = Column(String(100), default=None)
    company_address = Column(String(128), nullable=False)
    company_website = Column(String(128), default=None)

    # Relationship with table 'users'(owner_id foreign key)
    users = relationship('UserModel')

# Database table 'users'
class UserModel(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    # created_at = Column(TIMESTAMP(timezone=True),
    #                     nullable=False, server_default=text('now()'))


# Database table 'business_cards_users'
class BusinessCardsUsersModel(Base):

    __tablename__ = 'business_cards_users'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    business_card_id = Column(Integer, ForeignKey('business_card.id', ondelete='CASCADE'), nullable=False)

    # Relationship with table 'business_card' and 'users'(business_card_id foreign key and user_id foreign key)
    business_card = relationship('BusinessCardModel')
    users = relationship('UserModel')


# Database table 'reports'
class ReportModel(Base):

    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    report_description = Column(Text, nullable=False)

    # Relationship with table 'users'
    users = relationship('UserModel')
