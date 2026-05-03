from app.extensions import db

VALID_STATUSES = ["Applied", "Interviewing", "Offered", "Rejected", "Withdrawn"]

class Application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Applied")
    date_applied = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Float)
    job_url = db.Column(db.String(255))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __repr__(self):
        return f"<Application {self.job_title} at {self.company.name}>"
