"""empty message

Revision ID: c05b18293895
Revises: 6093d5e52b01
Create Date: 2016-10-16 14:43:25.805427

"""

# revision identifiers, used by Alembic.
revision = 'c05b18293895'
down_revision = '6093d5e52b01'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('discount_code_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'discount_codes', ['discount_code_id'], ['id'], ondelete='SET NULL')
    op.add_column('events_version', sa.Column('discount_code_id', sa.Integer(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'discount_code_id')
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'discount_code_id')
    ### end Alembic commands ###