"""rename `meta_description` to `description`

Revision ID: f149c3b1da98
Revises: 2ef61ad2de86
Create Date: 2024-09-30 09:49:45.759936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f149c3b1da98'
down_revision = '2ef61ad2de86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogpage', schema=None) as batch_op:
        batch_op.alter_column(column_name='meta_description', new_column_name='description', existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=500), nullable=True)
        batch_op.alter_column('is_all_posts',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text('false'),
               existing_nullable=False)
        batch_op.alter_column('is_login_required',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text('true'),
               existing_nullable=False)
        batch_op.alter_column('is_published',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text('false'),
               existing_nullable=False)
        batch_op.alter_column('is_writeable',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text('false'),
               existing_nullable=False)

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('timestamp',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('NOW()'),
               existing_nullable=False)
        batch_op.alter_column('is_unread',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text('true'),
               existing_nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('timestamp',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('NOW()'),
               existing_nullable=False)
        batch_op.alter_column('is_published',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text('false'),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('is_published',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text("'0'"),
               existing_nullable=False)
        batch_op.alter_column('timestamp',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=False)

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('is_unread',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text("'1'"),
               existing_nullable=False)
        batch_op.alter_column('timestamp',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_nullable=False)

    with op.batch_alter_table('blogpage', schema=None) as batch_op:
        batch_op.alter_column(column_name='description', new_column_name='meta_description', existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=500), nullable=True)
        batch_op.alter_column('is_writeable',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text("'0'"),
               existing_nullable=False)
        batch_op.alter_column('is_published',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text("'0'"),
               existing_nullable=False)
        batch_op.alter_column('is_login_required',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text("'1'"),
               existing_nullable=False)
        batch_op.alter_column('is_all_posts',
               existing_type=mysql.TINYINT(display_width=1),
               server_default=sa.text("'0'"),
               existing_nullable=False)

    # ### end Alembic commands ###