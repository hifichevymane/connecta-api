"""Create business_card table

Revision ID: eedb420ca857
Revises: 
Create Date: 2023-04-20 19:55:08.407181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eedb420ca857'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('business_card', sa.Column('id', sa.Integer, nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('business_card')
    pass
