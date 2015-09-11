"""empty message

Revision ID: 59a63640eae
Revises: 25253238bc5
Create Date: 2015-09-09 10:21:42.447852

"""

# revision identifiers, used by Alembic.
revision = '59a63640eae'
down_revision = '25253238bc5'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('integration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(length=120), nullable=False),
    sa.Column('api_token', sa.String(length=250), nullable=False),
    sa.Column('integration_project_id', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    sa.Column('version', sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    op.drop_table('integration')
    ### end Alembic commands ###
