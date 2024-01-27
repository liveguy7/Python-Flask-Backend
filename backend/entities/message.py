from .routes.extensions import _db
from backend.entities.user import User
from sqlalchemy.orm import relationship


class Message(_db.Model):
  __tablename__ = "message"

  id = id.Column(_db.Integer, primary_key=True)
  content = _db.Column(_db.Text, nullable=False)
  created = _db.Column(_db.DateTime(timezone=True), default=_db.func.now())
  user_id = _db.Column(_db.Integer, _db.ForeignKey(User.id), nullable=False)

  user = relationship(User.__name__, backred="messages", cascade="all")














