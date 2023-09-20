from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Your User, Employee, Late, Leave models go here
# Employee Model (Example)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    emp_name = db.Column(db.String(150), nullable=False)
    

class employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    emp_name = db.Column(db.String(150), nullable=False)

# Late Model (Example)
class late(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    emp_name = db.Column(db.String(150), nullable=False)
    reason = db.Column(db.String(150), nullable=False)
    from_time = db.Column(db.String(150), nullable=False)
    to_time = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(150), default='Pending')
    hod_approval = db.Column(db.String(150), default='Pending')
    approved_by = db.Column(db.String(150), default='Pending')
    hr_approval = db.Column(db.String(150), default='Pending')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
# Leave Model (Example)
class leave(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    emp_name = db.Column(db.String(150), nullable=False)
    reason = db.Column(db.String(150), nullable=False)
    from_date = db.Column(db.String(150), nullable=False)
    to_date = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(150), default='Pending')
    hod_approval = db.Column(db.String(150), default='Pending')
    approved_by = db.Column(db.String(150), default='Pending')
    hr_approval = db.Column(db.String(150), default='Pending')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
