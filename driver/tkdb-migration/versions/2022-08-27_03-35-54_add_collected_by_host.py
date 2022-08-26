"""add_collected_by_host

Revision ID: 5d06329af877
Revises: 105c0a425f43
Create Date: 2022-08-27 03:35:54.711362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d06329af877'
down_revision = '105c0a425f43'
branch_labels = None
depends_on = None


def upgrade():
    pass

    conn = op.get_bind()
    conn.execute(
        "ALTER TABLE temperature ADD COLUMN collected_by VARCHAR(64)")
    conn.execute(
        "UPDATE temperature SET collected_by = 'gn-sv-11'")
    conn.execute(
        "ALTER TABLE temperature ALTER COLUMN collected_by SET NOT NULL;")

    conn.execute(
        "ALTER TABLE plug_state ADD COLUMN collected_by VARCHAR(64)")
    conn.execute(
        "UPDATE plug_state SET collected_by = 'gn-sv-11'")
    conn.execute(
        "ALTER TABLE plug_state ALTER COLUMN collected_by SET NOT NULL;")


def downgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE temperature DROP COLUMN collected_by")
    conn.execute("ALTER TABLE plug_state DROP COLUMN collected_by")
