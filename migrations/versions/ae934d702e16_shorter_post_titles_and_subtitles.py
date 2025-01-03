"""shorter post titles and subtitles

Revision ID: ae934d702e16
Revises: 42e1ee031008
Create Date: 2024-04-06 03:54:11.421632

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ae934d702e16'
down_revision = '42e1ee031008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=250),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('sanitized_title',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=250),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('subtitle',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=500),
               type_=sa.String(length=150),
               nullable=True)
        batch_op.alter_column('content',
               existing_type=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               type_=sa.Text(length=100000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.Text(length=100000),
               type_=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               existing_nullable=False)
        batch_op.alter_column('subtitle',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=500),
               nullable=False)
        batch_op.alter_column('sanitized_title',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=250),
               existing_nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_bin', length=250),
               existing_nullable=False)

    # ### end Alembic commands ###
