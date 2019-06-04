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
db = client.temp
pprint(dir())
pprint(db.command('serverStatus'))

