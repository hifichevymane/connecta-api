"""Add foreign key in business_card table

Revision ID: 8ab77bc96db7
Revises: 3bb043ecd357
Create Date: 2023-04-21 15:32:00.707178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ab77bc96db7'
down_revision = '3bb043ecd357'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('business_card', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('business_card_users_fk', source_table='business_card', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('business_card_users_fk', table_name='business_card')
    op.drop_column('business_card', 'owner_id')
    pass
