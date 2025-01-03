"""changed uniqueness check

Revision ID: c9f6566b30be
Revises: b7183dac0f63
Create Date: 2024-06-06 11:28:08.646796

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c9f6566b30be'
down_revision = 'b7183dac0f63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               type_=sa.Text(length=100000),
               existing_nullable=False)
        batch_op.drop_index('sanitized_title')
        batch_op.drop_index('title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index('title', ['title'], unique=True)
        batch_op.create_index('sanitized_title', ['sanitized_title'], unique=True)
        batch_op.alter_column('content',
               existing_type=sa.Text(length=100000),
               type_=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               existing_nullable=False)

    # ### end Alembic commands ###
