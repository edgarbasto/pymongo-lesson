from flask import Flask, render_template, request
#from pymongo import MongoClient
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/istec'
mongo = PyMongo(app)



@app.route('/')
def index():
    todos_alunos = mongo.db.alunos.find({})
    return render_template('index.html', todos_alunos = todos_alunos)

'''
@app.route('/nova')
def nova():
    festa = FormFesta(request.form)
    return render_template('novo.tml', form=festa)
'''

if __name__ == '__main__':
    app.run(debug=True)

