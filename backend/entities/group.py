from sqlalchemy.orm import relationship
from backend.extensions import _db
from backend.entities.user import User

users_to_groups_association = _db.Table (
  "users_to_groups_association",
  _db.Column("user_id", _db.Integer, _db.ForeignKey(User.id), primary_key=True),
  _db.Column("group_id", _db.Integer, _db.ForeignKEy("group.id"), primary_key=True)
  
)

class Group(_db.Model):
  __tablename__ = "group"
  id = _db.Column(_db.Integer, primary_key=True)
  name = _db.Column(_db.String(50), unique=True, nullable=False)

  users = relationship(User.__name__, secondary=users_to_groups_association, backref="groups")

