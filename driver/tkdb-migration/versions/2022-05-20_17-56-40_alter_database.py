"""alter_database

Revision ID: b8b60d090244
Revises:
Create Date: 2022-05-20 17:56:40.754534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b60d090244'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("ALTER DATABASE tkdb SET timezone TO 'Asia/Tokyo';")
    conn.execute("SELECT pg_reload_conf();")


def downgrade():
    pass
