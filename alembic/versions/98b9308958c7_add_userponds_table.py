"""Add UserPonds table

Revision ID: 98b9308958c7
Revises: 5f69d5503d60
Create Date: 2023-11-02 04:20:45.592528

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '98b9308958c7'
down_revision = '5f69d5503d60'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users_ponds',
        sa.Column('pond_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users_auth.user_id'), nullable=True),
        sa.Column('user_ponds_pond_name', sa.String(length=255), nullable=True),
        sa.Column('user_ponds_fish_type', sa.String(length=255), nullable=True),
        sa.Column('user_ponds_start_date', sa.Date(), nullable=True),
        sa.Column('user_ponds_pond_diameter', sa.Integer(), nullable=True),
        sa.Column('user_ponds_pond_density', sa.String(length=255), nullable=True),
        sa.Column('user_ponds_target_size', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('pond_id')
    )

def downgrade():
    op.drop_table('users_ponds')
