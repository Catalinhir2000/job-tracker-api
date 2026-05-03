from app.extensions import db

class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    website = db.Column(db.String(255))
    location = db.Column(db.String(255))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    applications = db.relationship("Application", backref="company", lazy=True)

    def __repr__(self):
        return f"<Company {self.name}>"