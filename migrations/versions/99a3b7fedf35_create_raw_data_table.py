"""Create raw_data_table

Revision ID: 99a3b7fedf35
Revises: 07d0cbda088a
Create Date: 2023-04-15 00:38:10.945200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a3b7fedf35'
down_revision = '07d0cbda088a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'raw_data',
        sa.Column('id',sa.Uuid),
        sa.Column('sepal length (cm)', sa.Float),
        sa.Column('sepal width (cm)', sa.Float),
        sa.Column( 'petal length (cm)', sa.Float),
        sa.Column('petal width (cm)', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('raw_data')