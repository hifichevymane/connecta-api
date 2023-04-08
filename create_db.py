from sqlalchemy import create_engine, Column, Text, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///business_cards.db', echo=True)
Base = declarative_base()

Session = sessionmaker(engine)
session = Session()


class BusinessCardsModel(Base):

    __tablename__ = 'business_cards'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(30))
    company_services_type = Column(String(50))
    company_description = Column(Text)
    company_phone_number = Column(String(14))
    company_instagram = Column(String(50))
    company_telegram = Column(String(100))
    company_address = Column(String(128))
    company_website = Column(String(128))

    def __init__(self, company_name, company_services_type, company_description, company_phone_number,
                 company_instagram, company_telegram, company_address, company_website):

        self.company_name = company_name
        self.company_services_type = company_services_type
        self.company_description = company_description
        self.company_phone_number = company_phone_number
        self.company_instagram = company_instagram
        self.company_telegram = company_telegram
        self.company_address = company_address
        self.company_website = company_website


Base.metadata.create_all(engine)
