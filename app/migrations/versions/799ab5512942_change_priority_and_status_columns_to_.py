"""Change priority and status columns to String

Revision ID: 799ab5512942
Revises: 27c36be70f5e
Create Date: 2024-10-14 15:26:39.810550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '799ab5512942'
down_revision: Union[str, None] = '27c36be70f5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'priority',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('tasks', 'status',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'status',
               existing_type=sa.String(),
               type_=postgresql.JSON(astext_type=sa.Text()),
               existing_nullable=True)
    op.alter_column('tasks', 'priority',
               existing_type=sa.String(),
               type_=postgresql.JSON(astext_type=sa.Text()),
               existing_nullable=True)
    # ### end Alembic commands ###