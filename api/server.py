import requests
from elasticsearch import Elasticsearch
import json
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

x = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})

print(x)