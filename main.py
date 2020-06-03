import datetime
import os
import psycopg2
from flask import Flask, g, render_template, request, redirect
import data
# from boto.s3.connection import S3Connection

app = Flask('app')

class objekts:
    def __init__(self, izvele, teksts):
        self.izvele=izvele
        self.teksts=teksts

@app.route('/', methods=['POST', 'GET'])
def rezultati():
    if request.method == 'POST':
        ManaIzvele=int(request.form['izvele'])
        MansTeksts=request.form['teksts']
        MansObjekts=objekts(ManaIzvele,MansTeksts)
        rezultats=data.nolasit(MansObjekts)
    else:
        rezultats=data.nolasit()
    return render_template('rezultati.html', linijas=rezultats)


@app.errorhandler(500)
def servererror(pars=0):
    return redirect('/')