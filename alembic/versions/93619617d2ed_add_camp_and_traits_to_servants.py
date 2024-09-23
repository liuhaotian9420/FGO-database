"""add camp and traits to servants

Revision ID: 93619617d2ed
Revises: 1f2f290d678e
Create Date: 2024-08-22 12:08:46.546633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93619617d2ed'
down_revision: Union[str, None] = '1f2f290d678e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('servants', sa.Column('class_mod', sa.Integer(), nullable=True, comment='职介系数'))
    op.add_column('servants', sa.Column('camp', sa.String(length=255), nullable=True, comment='从者阵营'))
    op.add_column('servants', sa.Column('traits', sa.String(length=255), nullable=True, comment='从者的特性'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('servants', 'traits')
    op.drop_column('servants', 'camp')
    op.drop_column('servants', 'class_mod')
    # ### end Alembic commands ###
