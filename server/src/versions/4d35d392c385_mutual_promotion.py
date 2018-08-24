"""mutual_promotion

Revision ID: 4d35d392c385
Revises: 070b230b4b45
Create Date: 2018-08-24 20:52:35.529038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d35d392c385'
down_revision = '070b230b4b45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channel', sa.Column('mutual_promotion', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('channel', 'mutual_promotion')
    # ### end Alembic commands ###