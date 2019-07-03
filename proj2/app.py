from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
#import pymongo
from pymongo import MongoClient
import os


app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.istec #selecionar database
col = db.festas #selecionar colection


@app.route('/')
def index():
    col_list = col.find({})
    #return '<h1>Teste</h1>'
    return render_template('index.html', dados = col_list)

@app.route('/add', methods=['POST'])
def add():
    name = request.values.get('name')
    date = request.values.get('date')
    place = request.values.get('place')
    col.insert({'name': name, 'date':date, 'place':place})
    return redirect('/')

@app.route('/remove')
def remove():
    key = request.values.get('_id')
    col.remove({'_id':ObjectId(key)})
    return redirect('/')

@app.route('/edit')
def edit():
    key = request.values.get('_id')
    obj = col.find({'_id':ObjectId(key)})
    return render_template('edit.html', object = obj)


@app.route('/update', methods=['POST'])
def update():
    key = request.values.get('_id')
    name = request.values.get('name')
    date = request.values.get('date')
    place = request.values.get('place')
    col.update({'_id':ObjectId(key)}, {'$set':{'name': name, 'date':date, 'place':place}})
    return redirect('/')


if __name__ == '__main__':
    app.run(Debug=True)

