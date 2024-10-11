"""empty message

Revision ID: ae096a54d7c8
Revises: 59da52157b63
Create Date: 2024-10-10 18:33:19.692063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae096a54d7c8'
down_revision: Union[str, None] = '59da52157b63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
