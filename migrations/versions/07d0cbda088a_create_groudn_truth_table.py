"""create groudn truth table

Revision ID: 07d0cbda088a
Revises: f4922826075b
Create Date: 2023-04-15 00:35:01.793216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d0cbda088a'
down_revision = 'f4922826075b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'ground_truth',
        sa.Column('id',sa.Uuid),
        sa.Column('value', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('ground_truth')