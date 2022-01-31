"""add dataset fields

Revision ID: 70bcddc9fffa
Revises: b0ec74f6d899
Create Date: 2022-01-27 13:38:25.991699

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "70bcddc9fffa"
down_revision = "b0ec74f6d899"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("reciperun", sa.Column("is_test", sa.Boolean(), nullable=False))
    op.add_column(
        "reciperun", sa.Column("dataset_type", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
    )
    op.add_column(
        "reciperun",
        sa.Column("dataset_public_url", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("reciperun", "dataset_public_url")
    op.drop_column("reciperun", "dataset_type")
    op.drop_column("reciperun", "is_test")
    # ### end Alembic commands ###