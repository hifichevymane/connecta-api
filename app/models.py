from .database import Base
from sqlalchemy import Column, Text, String, Integer

# Database table 'business_card'
class BusinessCardModel(Base):

    __tablename__ = 'business_card'

    id = Column(Integer, primary_key=True, nullable=False)
    company_name = Column(String(30), nullable=False)
    company_services_type = Column(String(50), nullable=False)
    company_description = Column(Text, nullable=False)
    company_phone_number = Column(String(14), nullable=False)
    company_instagram = Column(String(50), default=None)
    company_telegram = Column(String(100), default=None)
    company_address = Column(String(128), nullable=False)
    company_website = Column(String(128), default=None)
