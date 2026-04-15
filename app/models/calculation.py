from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from datetime import datetime
import uuid
# from app.models.user import User

# -------------------------
# BASE MODEL
# -------------------------
class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False, index=True
    )

    type = Column(String(50), nullable=False, index=True)

    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)

    result = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="calculations")

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "calculation"
    }

    def validate(self):
        if self.a is None or self.b is None:
            raise ValueError("Inputs cannot be None")


class Addition(Calculation):
    __mapper_args__ = {"polymorphic_identity": "addition"}

    def compute(self):
        self.validate()
        return self.a + self.b


class Subtraction(Calculation):
    __mapper_args__ = {"polymorphic_identity": "subtraction"}

    def compute(self):
        self.validate()
        return self.a - self.b


class Multiplication(Calculation):
    __mapper_args__ = {"polymorphic_identity": "multiplication"}

    def compute(self):
        self.validate()
        return self.a * self.b


class Division(Calculation):
    __mapper_args__ = {"polymorphic_identity": "division"}

    def compute(self):
        self.validate()
        if self.b == 0:
            raise ValueError("Division by zero")
        return self.a / self.b