"""create post table

Revision ID: f75d8d38bb96
Revises: 
Create Date: 2022-04-30 23:09:48.179987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f75d8d38bb96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('published', sa.Boolean(), default=False),
                    )
    pass


def downgrade():
    op.drop('posts')
    pass
