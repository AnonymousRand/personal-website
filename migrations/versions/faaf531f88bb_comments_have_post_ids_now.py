"""comments have post_ids now

Revision ID: faaf531f88bb
Revises: 7590805c41e8
Create Date: 2024-03-09 13:35:43.888008

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'faaf531f88bb'
down_revision = '7590805c41e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               type_=sa.Text(length=100000),
               existing_nullable=False)
        batch_op.drop_constraint('post_ibfk_1', type_='foreignkey')
        batch_op.drop_column('comment_ids')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_ids', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('post_ibfk_1', 'comment', ['comment_ids'], ['id'])
        batch_op.alter_column('content',
               existing_type=sa.Text(length=100000),
               type_=mysql.MEDIUMTEXT(collation='utf8mb3_bin'),
               existing_nullable=False)

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###