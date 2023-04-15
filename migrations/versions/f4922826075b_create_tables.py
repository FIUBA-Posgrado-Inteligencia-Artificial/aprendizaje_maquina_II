"""create tables

Revision ID: f4922826075b
Revises: 
Create Date: 2023-04-13 23:57:41.039350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4922826075b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'inference',
        sa.Column('id',sa.Uuid),
        sa.Column('value', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('inference')
