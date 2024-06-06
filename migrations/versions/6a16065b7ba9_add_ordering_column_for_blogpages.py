"""add ordering column for blogpages

Revision ID: 6a16065b7ba9
Revises: 3034565ad1a6
Create Date: 2024-06-06 08:02:19.764793

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6a16065b7ba9'
down_revision = '3034565ad1a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogpage', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_blogpage_order'), ['order'], unique=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               type_=sa.Text(length=100000),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'blogpage', ['blogpage_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('content',
               existing_type=sa.Text(length=100000),
               type_=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               existing_nullable=False)

    with op.batch_alter_table('blogpage', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_blogpage_order'))
        batch_op.drop_column('order')

    # ### end Alembic commands ###