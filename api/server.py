import requests
from elasticsearch import Elasticsearch
import json
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content)

# x = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
# print(x)

