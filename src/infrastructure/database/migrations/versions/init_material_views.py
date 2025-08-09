"""init_material_views

Revision ID: 436d2162cf69
Revises: fe7b962e978d
Create Date: 2025-08-09 12:04:59.438622

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "436d2162cf69"
down_revision: Union[str, None] = "fe7b962e978d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE MATERIALIZED VIEW artist_album_count AS
        SELECT
            artist_uuid,
            COUNT(*) AS album_count
        FROM albums
        GROUP BY artist_uuid;
        """
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS artist_album_count_idx "
        "ON artist_album_count (artist_uuid);"
    )

    op.execute(
        """
        CREATE MATERIALIZED VIEW album_track_count AS
        SELECT
            album_uuid,
            COUNT(*) AS track_count
        FROM tracks
        GROUP BY album_uuid;
        """
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS album_track_count_idx "
        "ON album_track_count (album_uuid);"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS artist_album_count_idx;")
    op.execute("DROP INDEX IF EXISTS album_track_count_idx;")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS artist_album_count;")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS album_track_count;")
