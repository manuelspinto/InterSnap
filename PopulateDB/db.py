from flask.ext.sqlalchemy import SQLAlchemy as db
from sqlalchemy.dialects.postgresql import ARRAY

class AddStruct(db.Model):
    __tablename__ = 'addstruct'

    date = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)

    total = db.Column(db.Integer)
    discarded = db.Column(db.Integer)
    totalv6 = db.Column(db.Integer)
    discardedv6 = db.Column(db.Integer)


    filev4 = db.Column(db.String(80), unique=True)
    filev6 = db.Column(db.String(80), unique=True)
    spacev4 = db.Column(ARRAY(db.Integer))
    spacev6 = db.Column(ARRAY(db.Integer))


    def __init__(self, date, year, month, day):
        self.date = date
        self.year = year
        self.month = month
        self.day = day


    def __repr__(self):
        return self.date