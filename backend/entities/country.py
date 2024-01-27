from .routes.extensions import _db

class Country(_db.Model):
  __tablename__ = "country"
  id = _db.Column(_db.Integer, primary_key=True)
  code = _db.Column(_db.String(2), unique=True, nullable=False)
  name = _db.Column(_db.String(50), unique=True, nullable=False)

