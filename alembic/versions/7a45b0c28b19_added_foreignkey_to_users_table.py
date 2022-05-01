"""added foreignkey to users table

Revision ID: 7a45b0c28b19
Revises: 408f864fcc01
Create Date: 2022-05-01 11:16:12.747205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a45b0c28b19'
down_revision = '408f864fcc01'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
