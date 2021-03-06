"""Create table

Revision ID: e5ea837b3e0e
Revises: 
Create Date: 2018-08-30 18:55:29.844709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5ea837b3e0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=8), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_code'), 'item', ['code'], unique=False)
    op.create_index(op.f('ix_item_name'), 'item', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_name'), table_name='item')
    op.drop_index(op.f('ix_item_code'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###
