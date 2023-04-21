"""Create business_cards_users table

Revision ID: 417c56ff2677
Revises: 8ab77bc96db7
Create Date: 2023-04-21 15:51:29.909940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '417c56ff2677'
down_revision = '8ab77bc96db7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('business_cards_users',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    op.add_column('business_cards_users', sa.Column('user_id', sa.Integer, nullable=False))
    op.create_foreign_key('business_cards_users_users_fk', source_table='business_cards_users',
                          referent_table='users', local_cols=['user_id'], remote_cols=['id'],
                          ondelete='CASCADE')
    op.add_column('business_cards_users', sa.Column('business_card_id', sa.Integer, nullable=False))
    op.create_foreign_key('business_cards_users_business_card_fk', source_table='business_cards_users',
                          referent_table='business_card', local_cols=['business_card_id'], remote_cols=['id'],
                          ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('business_cards_users_business_card_fk', table_name='business_cards_users')
    op.drop_column('business_cards_users', 'business_card_id')
    op.drop_constraint('business_cards_users_users_fk', table_name='business_cards_users')
    op.drop_column('business_cards_users', 'user_id')
    op.drop_table('business_cards_users')
    pass
