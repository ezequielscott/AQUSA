"""empty message

Revision ID: 25253238bc5
Revises: 2f1492453b2
Create Date: 2015-05-11 15:57:37.305171

"""

# revision identifiers, used by Alembic.
revision = '25253238bc5'
down_revision = '2f1492453b2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('format', sa.Text()))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'format')
    ### end Alembic commands ###
