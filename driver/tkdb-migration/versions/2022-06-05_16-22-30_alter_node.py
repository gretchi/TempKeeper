"""alter_node

Revision ID: 8e07987f6703
Revises: af2b893367af
Create Date: 2022-06-05 16:22:30.089690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e07987f6703'
down_revision = 'af2b893367af'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE node ALTER COLUMN sensor_mac DROP NOT NULL")
    conn.execute("ALTER TABLE node ALTER COLUMN plug_mac DROP NOT NULL")


def downgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE node ALTER COLUMN sensor_mac SET NOT NULL")
    conn.execute("ALTER TABLE node ALTER COLUMN plug_mac SET NOT NULL")
