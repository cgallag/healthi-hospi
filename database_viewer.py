'''
Created on Jul 14, 2013

@author: cagallagher
'''
import couchdb
import json

server = couchdb.Server()
dbhospitals = server['health_hospitals']

print json.dumps([
    {
       'k': x.key,
       'id': x.id,
       'name': x.doc['name']
    }
    for x in dbhospitals.view(
        'queries/state_city_loc',
        startkey=['MA'],
        endkey=['MA', {}],
        include_docs=True
    )
], indent=4)


if __name__ == '__main__':
    pass