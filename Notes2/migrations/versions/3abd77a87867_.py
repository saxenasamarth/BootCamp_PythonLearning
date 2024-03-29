"""empty message

Revision ID: 3abd77a87867
Revises: 
Create Date: 2019-07-13 12:47:38.686159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3abd77a87867'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_author'))
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=1000), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name=op.f('fk_note_author_id_author')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_note'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_table('author')
    # ### end Alembic commands ###
