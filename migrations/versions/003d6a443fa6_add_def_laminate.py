"""add def laminate

Revision ID: 003d6a443fa6
Revises: 417e84fadddb
Create Date: 2019-08-24 14:47:56.050366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003d6a443fa6'
down_revision = '417e84fadddb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('base_decors', sa.Column('indexname', sa.String(length=16), nullable=True))
    op.create_index(op.f('ix_base_decors_indexname'), 'base_decors', ['indexname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_base_decors_indexname'), table_name='base_decors')
    op.drop_column('base_decors', 'indexname')
    # ### end Alembic commands ###
