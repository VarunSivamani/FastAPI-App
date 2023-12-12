"""add content column to post table

Revision ID: 3b23970d9275
Revises: 409a2f63a29a
Create Date: 2023-12-12 11:39:07.162834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b23970d9275'
down_revision: Union[str, None] = '409a2f63a29a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
