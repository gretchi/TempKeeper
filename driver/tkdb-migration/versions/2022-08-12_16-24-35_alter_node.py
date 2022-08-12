"""alter_node

Revision ID: 105c0a425f43
Revises: 711d854e8834
Create Date: 2022-08-12 16:24:35.766962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '105c0a425f43'
down_revision = '711d854e8834'
branch_labels = None
depends_on = None


def upgrade():
    pass

    conn = op.get_bind()
    conn.execute(
        "ALTER TABLE node ADD COLUMN auto_control INTEGER NOT NULL DEFAULT 0")


def downgrade():
    pass

    conn = op.get_bind()
    conn.execute("ALTER TABLE node DROP COLUMN auto_control")
