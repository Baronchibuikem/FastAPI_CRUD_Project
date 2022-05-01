"""add remaining columns on posts table

Revision ID: 6dd7210d791a
Revises: 7a45b0c28b19
Create Date: 2022-05-01 11:25:21.310017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dd7210d791a'
down_revision = '7a45b0c28b19'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                    server_default=sa.text('now()'), nullable=False),)
    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    pass
