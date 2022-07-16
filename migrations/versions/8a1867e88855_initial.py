"""initial

Revision ID: 8a1867e88855
Revises: 
Create Date: 2022-04-11 14:27:06.480747

"""
from alembic import op
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8a1867e88855'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stats',
    sa.Column('id', postgresql.UUID(as_uuid=True), default=uuid.uuid4, nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('stats', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    # ### end Alembic commands ###