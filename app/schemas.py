from pydantic import BaseModel

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
