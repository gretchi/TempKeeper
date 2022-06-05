"""add_sensor

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
    conn.execute(
        "INSERT INTO node(sensor_mac, plug_mac, preset_temp, location_name) VALUES ('C3:FF:42:9F:D2:0A', NULL, 0, 'リビング');"
    )


def downgrade():
    pass
