from __future__ import division
import threading
import atexit
import gc, os

from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap, WebCDN
from fetch.fetch import fetch
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from flask import request
from fetch.query import addQuery

import psycopg2

DATABASE_URL = "postgres:*************"

app = Flask(__name__)
Bootstrap(app)

app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
    'https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/'
)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
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




#db.session.add(User('joao', 'joao@example.com'))
#users = User.query.all()

#for user in users:
#    print user






#POOL_TIME = 60

###out = ""
#dataLock = threading.Lock()
#fetch_th = threading.Thread()

@app.route('/')
def index():
    #stats = fetch.fetch_link()

    return render_template('index.html')

@app.route('/addspace/query')
def addsquery():
    #stats = fetch.fetch_link()

    return render_template('addsquery.html')

@app.route('/pxtype/evolution')
def pxtypevo():

    return render_template('pxtypevo.html')

@app.route('/addspace')
def addspace():

    all = AddStruct.query.all()
    years = []
    for entry in all:
        years.append(entry.year)
    years.reverse()

    return render_template('addspace.html', years=years)

@app.route('/pxtype')
def pxtype():

    all = AddStruct.query.all()
    years = []
    for entry in all:
        years.append(entry.year)
    years.reverse()

    return render_template('pxtype.html', years=years);

@app.route('/_chart_type', methods=['GET'])
def chart_type():

    year = request.args.get('year', 0, type=int)
    ipver = request.args.get('ipver')

    struct = AddStruct.query.filter_by(year=year).first()

    if ipver == 'ipv4':
        dea = struct.dea_v4
        top = struct.top_v4
        lon = struct.lon_v4
        dele = struct.dele_v4
        tot = struct.total_type_v4
    else:
        dea = struct.dea_v6
        top = struct.top_v6
        lon = struct.lon_v6
        dele = struct.dele_v6
        tot = struct.total_type_v6

    data= []
    data.append((0, top*100/tot))
    data.append((1, lon*100/tot))
    data.append((2, dele*100/tot))
    data.append((3, dea*100/tot))


    return jsonify(pdata=data)

@app.route('/_space', methods=['GET'])
def space():

    year = request.args.get('year', 0, type=int)
    ipver = request.args.get('ipver')

    struct = AddStruct.query.filter_by(year=year).first()

    if ipver == 'ipv4':
        space = struct.space_v4
        tot = struct.total_v4
        limits = range(8,25,1)
    else:
        space = struct.space_v6
        tot = struct.total_v6
        limits = range(24,49,1)

    data = []
    for i in limits:
        #data.append((i,(space[i-1]/tot) * 100))
        data.append((i,space[i-1]))

    return jsonify(pdata=data)

@app.route('/_source', methods=['GET'])
def source():

    year = request.args.get('year', 0, type=int)
    ipver = request.args.get('ipver')

    struct = AddStruct.query.filter_by(year=year).first()

    if ipver == 'ipv4':
        file = struct.file_v4
        link = struct.link_v4
    else:
        file = struct.file_v6
        link = struct.link_v6

    return jsonify(file=file, link= link)

@app.route('/_data', methods=['GET'])
def data():

    year = request.args.get('year', 0, type=int)
    ipver = request.args.get('ipver')

    struct = AddStruct.query.filter_by(year=year).first()

    if ipver == 'ipv4':
        counts = struct.space_v4
        tot = struct.total_v4
        dis = struct.discarded_v4
    else:
        counts= struct.space_v6
        tot = struct.total_v6
        dis = struct.discarded_v6

    return jsonify(counts=counts, tot=tot, dis=dis)

@app.route('/_data_type', methods=['GET'])
def data_type():

    year = request.args.get('year', 0, type=int)
    ipver = request.args.get('ipver')

    struct = AddStruct.query.filter_by(year=year).first()

    if ipver == 'ipv4':
        dea = struct.dea_v4
        top = struct.dea_v4
        lon = struct.lon_v4
        dele = struct.dele_v4
        tot = struct.total_v4
        dis = struct.discarded_v4
    else:
        dea = struct.dea_v6
        top = struct.dea_v6
        lon = struct.lon_v6
        dele = struct.dele_v6
        tot = struct.total_v6
        dis = struct.discarded_v6

    return jsonify(dea = dea, top = top, lon=lon, dele = dele, tot=tot, dis=dis)

@app.route('/_addspaceq', methods=['GET'])
def spaceq():

    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('month')
    ipver = request.args.get('ipver')

    q = addQuery.run_query(day,month,year,ipver)

    if ipver == 'ipv4':
        limits = range(8,25,1)
    else:
        limits = range(24,49,1)

    space = q.mask_count
    data = []
    for i in limits:
        data.append((i,space[i-1]))

    return jsonify(pdata = data, day=day, month=month, year=year, tot=q.tot, dis=q.dis, fname=q.zipfname , dir=q.fullfile)

@app.route('/_pxtypevo', methods=['GET'])
def chartevo():

    ipver = request.args.get('ipver')

    all = AddStruct.query.all()
    dea = []
    top = []
    lon = []
    dele = []
    for entry in all:
        year = entry.year
        if ipver == 'ipv4':
            tot = entry.total_v4/100

            dea.append((year, entry.dea_v4/tot))
            top.append((year, entry.top_v4/tot))
            lon.append((year, entry.lon_v4/tot))
            dele.append((year, entry.dele_v4/tot))
        else:
            tot = entry.total_v6/100

            dea.append((year, entry.dea_v6/tot))
            top.append((year, entry.top_v6/tot))
            lon.append((year, entry.lon_v6/tot))
            dele.append((year, entry.dele_v6/tot))

    return jsonify(dea = dea, top = top, lon = lon, dele = dele)





# def create_thread():
#
#     def interrupt():
#         global fetch_th
#         fetch_th.cancel()
#
#     def doStuff():
#         global out
#
#         global fetch_th
#         with dataLock:
#             fetch_th = threading.Timer(POOL_TIME, doStuff, ())
#             fetch_th.start()
#
#     def doStuffStart():
#         global fetch_th
#         # Create your thread
#         fetch_th = threading.Timer(0, doStuff, ())
#         fetch_th.start()
#
#     # Initiate
#     doStuffStart()
#     # When you kill Flask (SIGTERM), clear the trigger for the next thread
#     atexit.register(interrupt)


if __name__ == '__main__':
    #create_thread()

    app.run()

