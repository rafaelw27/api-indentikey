from .. import db, flask_bcrypt

class Resources(db.Model):
    """ Resource Model for storing resource related details """
    __tablename__ = "resources"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    persons_id = db.Column(db.Integer, unique=False, nullable=False)
    min_threshold = db.Column(db.Integer, unique=False, nullable=False)
    code = db.Column(db.String(100), unique=True)
    main_resource_id = db.Column(db.Integer, unique=False, nullable=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    is_deleted = db.Column(db.Integer, unique=False,default=0, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)