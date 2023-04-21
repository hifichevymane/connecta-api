"""Add new columns

Revision ID: f8b5b5b806d6
Revises: eedb420ca857
Create Date: 2023-04-20 20:16:49.694353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b5b5b806d6'
down_revision = 'eedb420ca857'
branch_labels = None
depends_on = None


def upgrade() -> None:

    pass


def downgrade() -> None:
    op.drop_column('business_card', 'title')
    op.drop_table('business_card')
    pass
