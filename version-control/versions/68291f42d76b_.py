"""empty message

Revision ID: 68291f42d76b
Revises: fee1ab5b252e
Create Date: 2025-06-06 01:58:48.450162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68291f42d76b'
down_revision: Union[str, None] = '6d9ca64f831e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_table('messages')
    op.drop_table('chats')
    op.drop_table('usages')
    op.create_table(
        'chats',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_from', sa.Integer(), nullable=True),
        sa.Column('user_to', sa.Integer(), nullable=True),
        sa.Column('creation_date', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_from'], ['users.id']),
        sa.ForeignKeyConstraint(['user_to'], ['users.id'])
    )
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('chat_id', sa.Integer(), nullable=True),
        sa.Column('text', sa.String(), nullable=True),
        sa.Column('media_url', sa.String(), nullable=True),
        sa.Column('date', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['chat_id'], ['chats.id'])
    )
    op.create_table(
        'usages',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('request_text', sa.String(), nullable=False),
        sa.Column('response_text', sa.String()),
        sa.Column('date', sa.DateTime(), server_default=sa.func.now())
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('messages')
    op.drop_table('chats')
    op.drop_table('usages')
