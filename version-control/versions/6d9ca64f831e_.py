"""empty message

Revision ID: 6d9ca64f831e
Revises: 4fb51bd8cf4a
Create Date: 2025-06-05 17:40:55.317532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d9ca64f831e'
down_revision: Union[str, None] = '4fb51bd8cf4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'usages',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('request_text', sa.String(), nullable=False),
        sa.Column('response_text', sa.String()),
        sa.Column('date', sa.DateTime(), default=sa.func.now())
    )

def downgrade():
    op.drop_table('usages')