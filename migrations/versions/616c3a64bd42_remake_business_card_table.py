"""Remake business_card table

Revision ID: 616c3a64bd42
Revises: 80d7b0b2ca33
Create Date: 2023-04-24 16:17:21.249208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '616c3a64bd42'
down_revision = '80d7b0b2ca33'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business_card', sa.Column('company_name', sa.String(), nullable=False))
    op.add_column('business_card', sa.Column('company_services_type', sa.String(), nullable=False))
    op.add_column('business_card', sa.Column('company_description', sa.Text(), nullable=False))
    op.add_column('business_card', sa.Column('company_phone_number', sa.String(), nullable=False))
    op.add_column('business_card', sa.Column('company_instagram', sa.String(), nullable=True))
    op.add_column('business_card', sa.Column('company_telegram', sa.String(), nullable=True))
    op.add_column('business_card', sa.Column('company_address', sa.String(), nullable=False))
    op.add_column('business_card', sa.Column('company_website', sa.String(), nullable=True))
    op.drop_column('business_card', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business_card', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('business_card', 'company_website')
    op.drop_column('business_card', 'company_address')
    op.drop_column('business_card', 'company_telegram')
    op.drop_column('business_card', 'company_instagram')
    op.drop_column('business_card', 'company_phone_number')
    op.drop_column('business_card', 'company_description')
    op.drop_column('business_card', 'company_services_type')
    op.drop_column('business_card', 'company_name')
    # ### end Alembic commands ###
