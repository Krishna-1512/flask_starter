"""empty message

Revision ID: cd4832893054
Revises: 
Create Date: 2021-03-20 00:49:37.530715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4832893054'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('bedroom_num', sa.String(length=80), nullable=True),
    sa.Column('bathroom_num', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('types', sa.String(length=80), nullable=True),
    sa.Column('desciption', sa.String(length=80), nullable=True),
    sa.Column('filename', sa.String(length=500), nullable=True),
    sa.Column('photo', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bathroom_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_property')
    # ### end Alembic commands ###
