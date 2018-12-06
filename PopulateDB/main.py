from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
import fetch

DATABASE_URL = "postgres://*************************"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

class AddStruct(db.Model):
    __tablename__ = 'addstruct'

    date = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)

    link_v4 = db.Column(db.String(80), unique=True)
    file_v4 = db.Column(db.String(80), unique=True)
    total_v4 = db.Column(db.Integer)
    discarded_v4 = db.Column(db.Integer)
    space_v4 = db.Column(ARRAY(db.Integer))

    link_v6 = db.Column(db.String(80), unique=True)
    file_v6 = db.Column(db.String(80), unique=True)
    total_v6 = db.Column(db.Integer)
    discarded_v6 = db.Column(db.Integer)
    space_v6 = db.Column(ARRAY(db.Integer))

    total_type_v4 = db.Column(db.Integer)
    dea_v4 = db.Column(db.Integer)
    top_v4 = db.Column(db.Integer)
    lon_v4 = db.Column(db.Integer)
    dele_v4 = db.Column(db.Integer)

    total_type_v6 = db.Column(db.Integer)
    dea_v6 = db.Column(db.Integer)
    top_v6 = db.Column(db.Integer)
    lon_v6 = db.Column(db.Integer)
    dele_v6 = db.Column(db.Integer)


    def __init__(self, date, year, month, day, total_v4, discarded_v4, link_v4, file_v4, space_v4, total_v6, discarded_v6, link_v6, file_v6, space_v6, dea_v4, top_v4, lon_v4, dele_v4, dea_v6, top_v6, lon_v6, dele_v6, total_type4, total_type6):
        self.date = date
        self.year = year
        self.month = month
        self.day = day

        self.total_v4 = total_v4
        self.discarded_v4 = discarded_v4
        self.link_v4 = link_v4
        self.file_v4 = file_v4
        self.space_v4 = space_v4

        self.total_v6 = total_v6
        self.discarded_v6 = discarded_v6
        self.link_v6 = link_v6
        self.file_v6 = file_v6
        self.space_v6 = space_v6

        self.dea_v4 = dea_v4
        self.top_v4 = top_v4
        self.lon_v4 = lon_v4
        self.dele_v4 = dele_v4

        self.dea_v6 = dea_v6
        self.top_v6 = top_v6
        self.lon_v6 = lon_v6
        self.dele_v6 = dele_v6

        self.total_type_v4 = total_type4
        self.total_type_v6 = total_type6

    def __repr__(self):
        return self.date




if __name__ == '__main__':
    fetch.fetch.disp_links(db)
    app.run()



