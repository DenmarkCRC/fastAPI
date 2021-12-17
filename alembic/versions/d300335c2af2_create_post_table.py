"""create post table

Revision ID: d300335c2af2
Revises: 
Create Date: 2021-12-16 10:07:48.252173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d300335c2af2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
