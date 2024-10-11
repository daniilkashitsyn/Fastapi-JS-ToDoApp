"""Migration Done

Revision ID: 2f0156b49777
Revises: ea80a64fc4b9
Create Date: 2024-10-10 18:42:49.688482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2f0156b49777'
down_revision: Union[str, None] = 'ea80a64fc4b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'priority',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('tasks', 'status',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'status',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('tasks', 'priority',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    # ### end Alembic commands ###
