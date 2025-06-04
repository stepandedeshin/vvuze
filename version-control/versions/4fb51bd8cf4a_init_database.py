"""init database

Revision ID: 4fb51bd8cf4a
Revises: 
Create Date: 2025-06-05 00:40:55.734427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fb51bd8cf4a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'admins',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('login', sa.String(), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('registration_date', sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('login', sa.String(), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('registration_date', sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'groups',
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), default=None),
        sa.Column("creator_id", sa.Integer(), sa.ForeignKey("users.id")),
        sa.Column("creation_date", sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'profiles',
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('picture_url', sa.String(), default=None),
        sa.Column('bio', sa.String(), default=None),
        sa.Column('gender', sa.String(), default=None),
        sa.Column('phone', sa.String(), default=None),
        sa.Column('email', sa.String(), default=None)
    )

    op.create_table(
        'posts',
        sa.Column('id',sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id',sa.Integer(),sa.ForeignKey('users.id')),
        sa.Column('content',sa.String(), default=None),
        sa.Column("media", sa.String(), default=None),
        sa.Column("creation_date", sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'comments',
        sa.Column("id",sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id",sa.Integer(),sa.ForeignKey("users.id")),
        sa.Column("post_id",sa.Integer(),sa.ForeignKey("posts.id")),
        sa.Column("text",sa.String(), default=None),
        sa.Column("media_url",sa.String(), default=None),
        sa.Column("date",sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'friends',
        sa.Column("id",sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_from",sa.Integer(),sa.ForeignKey("users.id")),
        sa.Column("user_to",sa.Integer(),sa.ForeignKey("users.id")),
        sa.Column("accepted",sa.Boolean(), default=False),
        sa.Column("date",sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'group_members',
        sa.Column("user_id",sa.Integer(),sa.ForeignKey("users.id"), primary_key=True),
        sa.Column("group_id",sa.Integer(),sa.ForeignKey("groups.id"), primary_key=True),
        sa.Column("join_date",sa.DateTime(), nullable=False, server_default=sa.func.now())
    )

    op.create_table(
        'likes',
        sa.Column("user_id",sa.Integer() ,sa.ForeignKey("users.id"), primary_key=True ),
        sa.Column("post_id",sa.Integer() ,sa.ForeignKey( "posts.id" ), primary_key=True ),
        sa.Column("date", sa.DateTime() ,nullable=False , server_default=sa.func.now() )
    )

    op.create_table(
        'messages',
        sa.Column( "id" ,sa.Integer() ,primary_key=True , autoincrement=True ),
        sa.Column( "user_from" ,sa.Integer() ,sa.ForeignKey( "users.id" ) ),
        sa.Column( "user_to" ,sa.Integer() ,sa.ForeignKey( "users.id" ) ),
        sa.Column( "text" ,sa.String() ,default=None ),
        sa.Column( "media_url" ,sa.String() ,default=None ),
        sa.Column( "date" ,sa.DateTime() ,nullable=False , server_default=sa.func.now() )
    )

    op.create_table(
        'bans',
        sa.Column( "id" ,sa.Integer() ,primary_key=True, autoincrement=True ),
        sa.Column( "user_id" ,sa.Integer() ,sa.ForeignKey( "users.id" ) ),
        sa.Column( "ban_date" ,sa.DateTime() ,nullable=False, server_default=sa.func.now() ),
        sa.Column( "unbanned" ,sa.Boolean() ,default=False )
    )


def downgrade():
    op.drop_table('bans')
    op.drop_table('messages')
    op.drop_table('likes')
    op.drop_table('group_members')
    op.drop_table('friends')
    op.drop_table('comments')
    op.drop_table('posts')
    op.drop_table('profiles')
    op.drop_table('groups')
    op.drop_table('users')
    op.drop_table('admins')
