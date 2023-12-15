"""Init

Revision ID: 37ff14451fe1
Revises: 
Create Date: 2023-12-14 16:32:44.412864

"""
from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision = "37ff14451fe1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("dormitories", sa.Column("description", sa.String(), nullable=False))
    op.create_index(
        op.f("ix_dormitories_description"), "dormitories", ["description"], unique=False
    )
    op.drop_constraint(
        "dormitory_photos_dormitory_id_fkey", "dormitory_photos", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "dormitory_photos",
        "dormitories",
        ["dormitory_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "dormitory_photos", type_="foreignkey")
    op.create_foreign_key(
        "dormitory_photos_dormitory_id_fkey",
        "dormitory_photos",
        "dormitories",
        ["dormitory_id"],
        ["id"],
    )
    op.drop_index(op.f("ix_dormitories_description"), table_name="dormitories")
    op.drop_column("dormitories", "description")
    # ### end Alembic commands ###
