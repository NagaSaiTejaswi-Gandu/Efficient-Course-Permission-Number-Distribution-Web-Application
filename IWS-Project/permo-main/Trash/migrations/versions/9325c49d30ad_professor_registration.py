"""Professor registration

Revision ID: 9325c49d30ad
Revises: d6b5ffcdefa7
Create Date: 2022-10-21 21:29:23.226447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9325c49d30ad'
down_revision = 'd6b5ffcdefa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstName', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('lastName', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('is_professor', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_user_firstName'), 'user', ['firstName'], unique=False)
    op.create_index(op.f('ix_user_lastName'), 'user', ['lastName'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_lastName'), table_name='user')
    op.drop_index(op.f('ix_user_firstName'), table_name='user')
    op.drop_column('user', 'is_professor')
    op.drop_column('user', 'lastName')
    op.drop_column('user', 'firstName')
    # ### end Alembic commands ###