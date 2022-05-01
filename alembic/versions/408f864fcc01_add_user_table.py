"""add user table

Revision ID: 408f864fcc01
Revises: c3c1b2b1f088
Create Date: 2022-05-01 07:02:19.798871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '408f864fcc01'
down_revision = 'f75d8d38bb96'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
