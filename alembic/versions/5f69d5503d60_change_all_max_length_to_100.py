"""Change all max_length to 100

Revision ID: 5f69d5503d60
Revises: a78d53f93e16
Create Date: 2023-10-06 09:17:37.413077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f69d5503d60'
down_revision = 'a78d53f93e16'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users_class', 'user_pond_size_range', type_=sa.String(255))
    op.alter_column('users_class', 'user_fish_type', type_=sa.String(255))
    op.alter_column('users_class', 'user_fish_size_preference', type_=sa.String(255))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users_class', 'user_pond_size_range', type_=sa.String(50))
    op.alter_column('users_class', 'user_fish_type', type_=sa.String(50))
    op.alter_column('users_class', 'user_fish_size_preference', type_=sa.String(50))
    # ### end Alembic commands ###