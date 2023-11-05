"""Rename ota_code to otp_code

Revision ID: 390ec8cc94c6
Revises: 88087244d853
Create Date: 2023-11-05 15:48:08.843065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '390ec8cc94c6'
down_revision = '88087244d853'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_2fa', sa.Column('otp_code', sa.Integer(), nullable=True))
    op.drop_column('users_2fa', 'ota_code')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_2fa', sa.Column('ota_code', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('users_2fa', 'otp_code')
    # ### end Alembic commands ###