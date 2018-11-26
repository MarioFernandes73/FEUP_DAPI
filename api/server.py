import requests
from elasticsearch import Elasticsearch
import json
import nltk
nltk.download('punkt')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content)

# x = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
# print(x)
word_data = ""
while word_data != "terminate":
    print('Enter your search:')
    word_data = input()
    nltk_tokens = nltk.word_tokenize(word_data)
    print (nltk_tokens)
