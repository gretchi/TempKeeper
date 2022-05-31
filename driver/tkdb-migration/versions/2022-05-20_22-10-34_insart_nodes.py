"""insart_nodes

Revision ID: 35619ef1f009
Revises: 673c458801cd
Create Date: 2022-05-20 22:10:34.139341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35619ef1f009'
down_revision = '673c458801cd'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        "INSERT INTO node(sensor_mac, plug_mac, location_name) VALUES ('EB:EA:8A:94:5C:D8', '10:27:F5:22:07:C9', 'ぴー');"
    )
    conn.execute(
        "INSERT INTO node(sensor_mac, plug_mac, location_name) VALUES ('C4:43:D5:0d:4D:F4', 'AC:84:C6:51:14:91', 'そら');"
    )
    conn.execute(
        "INSERT INTO node(sensor_mac, plug_mac, location_name) VALUES ('FD:6B:1D:D9:15:56', '10:27:F5:22:08:E7', 'じん');"
    )
    conn.execute(
        "INSERT INTO node(sensor_mac, plug_mac, location_name) VALUES ('DC:08:9A:D2:9B:8A', '0C:80:63:04:FD:0B', 'きなこ');"
    )
    conn.execute(
        "INSERT INTO node(sensor_mac, plug_mac, location_name) VALUES ('C3:FF:42:9F:D2:0A', '10:27:F5:22:08:12', 'ゆき');"
    )

def downgrade():
    pass
