"""add_sensor

Revision ID: 711d854e8834
Revises: 8e07987f6703
Create Date: 2022-06-05 16:29:38.695103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711d854e8834'
down_revision = '8e07987f6703'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    # conn.execute(
    #     "INSERT INTO node(sensor_mac, plug_mac, preset_temp, location_name) VALUES ('C3:FF:42:9F:D2:0A', NULL, 0, 'リビング');"
    # )


def downgrade():
    pass
