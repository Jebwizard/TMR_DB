import web
import collections
from pymongo import MongoClient
import json
import ast
import pprint

urls = ('/','index')
app = web.application(urls,globals())

client = MongoClient()

DATA = {'results': [{'TMR': {'HUMAN-1': {'GENDER': 'MALE', 'from-sense': 'HE-N1', 'token': 'He', 'concept': 'HUMAN', 'is-in-subtree': 'OBJECT', 'sent-word-ind': (0, 0), 'CONSCIOUS': 'YES'}}, 'words': {0: 'HE-N1', 2: 'CONSCIOUS-ADJ1'}, 'concept_counts': {'HUMAN': {'word-info': [[0, 'top']], 'count': 1}}}, {'TMR': {'ANIMAL-1': {'GENDER': 'MALE', 'from-sense': 'HE-N2', 'token': 'He', 'concept': 'ANIMAL', 'is-in-subtree': 'OBJECT', 'sent-word-ind': (0, 0), 'CONSCIOUS': 'YES'}}, 'words': {0: 'HE-N2', 2: 'CONSCIOUS-ADJ1'}, 'concept_counts': {'ANIMAL': {'word-info': [[0, 'top']], 'count': 1}}}], 'timestamp': '2016-Jul-21 19:57:04', 'sentence': 'He is conscious.', 'sent-num': 0}

class index():

    #def POST(self):
    #    form = web.input(goldTmr)
    #    greeting = "%s" %(form.goldTmr)
    #    print(greeting)
    
    def POST(self):
        
        print('Recieving data from POST request - Converting from bytestring to String')
        sdata = (web.data()).decode()

        print('Recieving data from POST request - Converting from String to Dictionary')
        try:
            dict = ast.literal_eval(sdata)
            print(type(dict))
        except:
            print('fail')

        print('Reciving data from POST request - Converting keys to correct formats')
        try:
            con_dict = convert_keys_to_string(dict)
            addDict(con_dict)
        except:
            print('fail')

        print()
        print("==================== Entire collection =====================")
        pp = pprint.PrettyPrinter(indent=4)
        
        curser = getAll()
        for post in curser:
            print()
            pp.pprint(post)

if __name__ == '__main__':
    app.run()


def convert_keys_to_string(dictionary):
    # Recursively converts dictionary keys to strings.
    if isinstance(dictionary, dict):
        return dict((str(k), convert_keys_to_string(v)) 
        for k, v in dictionary.items())
    elif isinstance(dictionary, list):
        return [ convert_keys_to_string(x) for x in dictionary ]
    else:
        return dictionary

def addDict(dictionary:dict , database = 'DB', collection = 'TMRs'):
    client[database][collection].insert(dictionary)

# returns a curser object of all documents in the given database and collection
def getAll(database = 'DB', collection = 'TMRs', lim = 0):
    return client[database][collection].find( limit = lim )

def getSel( condition:dict = None , database = 'DB', collection = 'TMRs', lim =0):
    return client[database][collection].find(filter = condition, limit = lim) 