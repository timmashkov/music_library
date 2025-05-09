from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models import Base


class Template(Base):
    login: Mapped[str] = mapped_column(comment="Login")
