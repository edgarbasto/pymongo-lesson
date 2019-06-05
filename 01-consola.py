import pymongo
from pprint import pprint


'''
username = 'aluno'
password = 'aluno'
client MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
'''
'''
client = MongoClient('127.0.0.1')
db = client.admin
serverStatusResult = db.command('serverStatus')
pprint(serverStatusResult)
'''

client = pymongo.MongoClient('localhost', 27017)
#pprint(dir(client))
pprint(client.list_database_names())
db = client.testar
#pprint(dir(db))
#pprint(db.command('serverStatus'))

col = db.get_collection('qqcoisa')
#pprint(dir(col))

'''
one_data = {
    'titulo':'teste1',
    'pessoas': ['Joao', 'Pedro', 'Manuela'],
    'comida': {
        'carne': 12,
        'peixe': 2,
        'morcelas': 4.2,
    },
    'localidade':'montalegre'
}

col.insert_one(one_data)
'''
'''
two_data = [
    {
    'titulo':'teste2',
    'pessoas': ['Maria', 'Tete', 'Toto'],
    'comida': {
        'carne': 2.5,
        'peixe': 40,
        'morcelas': 2.3,
        },
    'localidade':'montalegre'
    }, 
    {
    'titulo':'teste3',
    'pessoas': ['Isa', 'Ana Lee', 'Rui'],
    'comida': {
        'carne': 8,
        'peixe': 23,
        'morcelas': 15,
        },
    'localidade':'lisboa'
    }
]

col.insert_many(two_data)
'''
