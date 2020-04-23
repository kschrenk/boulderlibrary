"""empty message

Revision ID: 735c0b43402e
Revises: 308b1cbe93dc
Create Date: 2020-04-21 15:48:40.247334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '735c0b43402e'
down_revision = '308b1cbe93dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('description', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('description')
    )
    op.create_table('gym',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('website', sa.String(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('status_description', sa.String(length=12), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['status_description'], ['status.description'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gym')
    op.drop_table('status')
    op.drop_table('category')
    # ### end Alembic commands ###
