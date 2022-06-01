"""create_table

Revision ID: 673c458801cd
Revises: b8b60d090244
Create Date: 2022-05-20 21:45:34.786372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '673c458801cd'
down_revision = 'b8b60d090244'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()

    conn.execute("CREATE SEQUENCE temperature_id_seq;")

    conn.execute(
        """CREATE TABLE temperature (
        id INTEGER NOT NULL DEFAULT nextval('temperature_id_seq'),
        mac VARCHAR(32) NOT NULL,
        temp FLOAT NOT NULL,
        humidity FLOAT NOT NULL,
        battery INTEGER NOT NULL,
        sent_at TIMESTAMP WITH TIME ZONE NOT NULL,
        create_at TIMESTAMP NULL DEFAULT now(),
        PRIMARY KEY (id));
    """
    )

    # ノードマスタ
    conn.execute("CREATE SEQUENCE node_id_seq;")

    conn.execute(
        """CREATE TABLE node (
            id INTEGER NOT NULL DEFAULT nextval('node_id_seq'),
            sensor_mac VARCHAR(32) UNIQUE NOT NULL,
            plug_mac VARCHAR(32) UNIQUE NOT NULL,
            plug_ip VARCHAR(32) DEFAULT NULL,
            preset_temp INTEGER NOT NULL DEFAULT 24,
            location_name VARCHAR(64) NOT NULL,
            PRIMARY KEY (id));
    """
    )

    conn.execute("CREATE SEQUENCE plug_state_id_seq;")

    conn.execute(
        """CREATE TABLE plug_state (
        id INTEGER NOT NULL DEFAULT nextval('plug_state_id_seq'),
        mac VARCHAR(32) NOT NULL,
        status INTEGER NOT NULL,
        sent_at TIMESTAMP WITH TIME ZONE NOT NULL,
        create_at TIMESTAMP NULL DEFAULT now(),
        PRIMARY KEY (id));
    """
    )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE temperature;")
    conn.execute("DROP SEQUENCE temperature_id_seq;")
    conn.execute("DROP TABLE node;")
    conn.execute("DROP SEQUENCE node_id_seq;")
    conn.execute("DROP TABLE plug_state;")
    conn.execute("DROP SEQUENCE plug_state_id_seq;")
