"""initial

Revision ID: b5802f793e9d
Revises:
Create Date: 2021-05-23 00:14:06.363871

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b5802f793e9d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "homework",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("text", sa.Text(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("deadline", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "student",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=30), nullable=True),
        sa.Column("last_name", sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "teacher",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=30), nullable=True),
        sa.Column("last_name", sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "homework_result",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("solution", sa.Text(), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("teacher_id", sa.Integer(), nullable=True),
        sa.Column("homework_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["author_id"], ["student.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["homework_id"],
            ["homework.id"],
        ),
        sa.ForeignKeyConstraint(["teacher_id"], ["teacher.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("homework_result")
    op.drop_table("teacher")
    op.drop_table("student")
    op.drop_table("homework")
    # ### end Alembic commands ###
