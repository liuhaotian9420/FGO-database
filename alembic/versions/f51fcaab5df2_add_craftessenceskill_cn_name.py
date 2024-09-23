"""add CraftEssenceSkill cn name

Revision ID: f51fcaab5df2
Revises: b033d5c37482
Create Date: 2024-09-11 11:05:10.508042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f51fcaab5df2'
down_revision: Union[str, None] = 'b033d5c37482'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('craft_essence_skills', sa.Column('ce_name_cn', sa.String(length=255), nullable=True, comment='中文名'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('craft_essence_skills', 'ce_name_cn')
    # ### end Alembic commands ###
