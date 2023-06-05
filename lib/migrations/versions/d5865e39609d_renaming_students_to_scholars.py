"""Renaming students to scholars

Revision ID: d5865e39609d
Revises: 791279dd0760
Create Date: 2023-06-05 10:36:04.576529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5865e39609d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
