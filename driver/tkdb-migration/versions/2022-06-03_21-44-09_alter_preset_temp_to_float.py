"""alter_preset_temp_to_float

Revision ID: af2b893367af
Revises: 35619ef1f009
Create Date: 2022-06-03 21:44:09.274919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af2b893367af'
down_revision = '35619ef1f009'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        "ALTER TABLE node ALTER COLUMN preset_temp TYPE DOUBLE PRECISION NOT NULL DEFAULT 24.0")


def downgrade():
    conn = op.get_bind()
    conn.execute(
        "ALTER TABLE node ALTER COLUMN preset_temp TYPE INTEGER NOT NULL DEFAULT 24")
