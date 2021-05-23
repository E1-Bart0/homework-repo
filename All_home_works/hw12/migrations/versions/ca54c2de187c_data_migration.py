"""Data migration


Revision ID: ca54c2de187c
Revises: b5802f793e9d
Create Date: 2021-05-23 00:14:54.679469

"""

from core.db import engine

# revision identifiers, used by Alembic.
from sqlalchemy.orm import sessionmaker
from task_models import Homework, HomeworkResult, Student, Teacher

revision = "ca54c2de187c"
down_revision = "b5802f793e9d"
branch_labels = None
depends_on = None


def upgrade():
    session_class = sessionmaker(bind=engine)
    session = session_class()

    user = Student(id=1, first_name="Jon", last_name="Doe")
    teacher = Teacher(id=1, first_name="Jane", last_name="Doe")
    homework1 = Homework(id=1, text="First", deadline=2)
    homework_result = HomeworkResult(
        id=1, solution="SOLUTION", author=user, homework=homework1, teacher_id=1
    )
    session.add_all([user, teacher, homework1, homework_result])

    session.commit()
    session.close()


def downgrade():
    session_class = sessionmaker(bind=engine)
    session = session_class()

    session.query(Student).filter(Student.id == 1).delete()
    session.query(Teacher).filter(Teacher.id == 1).delete()
    session.query(Homework).filter(Homework.id == 1).delete()
    session.query(HomeworkResult).filter(HomeworkResult.id == 1).delete()

    session.commit()
    session.close()
