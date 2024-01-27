from .routes.extensions import _db
from .entities.country import Country
from sqlalchemy.orm import relationship


class User(_db.Model):
  __tablename__ = "backend_user"

  id = _db.Column(_db.Integer, primary_key=True)
  username = _db.Column(_db.String(80), unique=True, nullable=False)
  password = _db.Column(_db.Text, nullable=False)
  email = _db.Column(_db.String(120), unique=True, nullable=False)

  country_id = _db.Column(_db.Integer, _db.ForeignKey(Country.id))
  country = relationship(Country.__name__)
  profile = relationship("Profile", uselist=False, back_populates="user")


class Profile(_db.Model):
  __tablename__ = "profile"

  id = _db.Column(_db.Integer, primary_key=True)
  birth_date = _db.Column(_db.DateTime)
  job = _db.Column(_db.String(100))
  user_id = _db.Column(_db.Integer, _db.ForeignKey(User.id))

  user = relationship(User.__name__, uselist=False, back_populates="profile")


















