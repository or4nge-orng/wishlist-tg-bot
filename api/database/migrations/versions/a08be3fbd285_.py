"""empty message

Revision ID: a08be3fbd285
Revises: c0360ff49226
Create Date: 2026-02-01 23:53:17.901258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a08be3fbd285'
down_revision: Union[str, Sequence[str], None] = 'c0360ff49226'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
