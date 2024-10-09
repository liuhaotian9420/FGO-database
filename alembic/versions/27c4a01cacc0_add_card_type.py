"""add card type

Revision ID: 27c4a01cacc0
Revises: 333b68a7ec26
Create Date: 2024-10-09 17:11:46.911393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '27c4a01cacc0'
down_revision: Union[str, None] = '333b68a7ec26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('servant_cards', sa.Column('card_name', sa.String(length=255), nullable=True, comment='指令卡的名称'))
    op.alter_column('servant_cards', 'card_type',
               existing_type=mysql.VARCHAR(length=255),
               comment='指令卡的类型',
               existing_nullable=True)
    op.create_index(op.f('ix_servant_cards_card_name'), 'servant_cards', ['card_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_servant_cards_card_name'), table_name='servant_cards')
    op.alter_column('servant_cards', 'card_type',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='指令卡的类型',
               existing_nullable=True)
    op.drop_column('servant_cards', 'card_name')
    # ### end Alembic commands ###
