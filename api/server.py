import requests
from elasticsearch import Elasticsearch
import json
import re
import nltk
nltk.download('punkt')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content)

# x = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
# print(x)

def countWords(parameter, index,string):
    results = es.count(index=index, doc_type=index, body={ "query": {"match" : {parameter : string}}})
    print("count",results)

def searchWords(parameter, index,string):
    results = es.search(index=index, doc_type=index, body={ "query": {"match" : {parameter : string}}})
    resultHits = results.get('hits').get('hits')
    length = len(resultHits)
    for i in range(0,length-1):
        hits = resultHits[i]
        print("index:",hits.get("_index"), "  id:" , hits.get("_id"),  "  source:" , hits.get("_source")  )



word_data = ""
while word_data != "TERMINATE":
    print('Enter your search:("TERMINATE" for exit)')
    word_data = input()
    word_data = re.sub('[^\w\s]','',word_data)
    nltk_tokens = nltk.word_tokenize(word_data)
    joinArray = " ".join(str(x) for x in nltk_tokens)
    print(joinArray)

    #procura as palavras no indice titulo
    searchWords("title", "title", joinArray)
'''
    #procura palavras no indice genero 
    print("genre")
    searchWords("genre", "genre", joinArray)
    print('\n')


    #procura as palavras no indice synopsis
    print("synopsis")
    searchWords("synopsis", "synopsis", joinArray)
    print('\n')

    #procura as palavras no indice details
    #"genres releaseDate duration countries mpaaRating allmovieRating flags directedBy producedBy releasedBy moods themes keywords attributes actors relatedMovies" 
    print("details")
    searchWords("countries", "details", joinArray)
    searchWords("directedBy", "details", joinArray)
    searchWords("producedBy", "details", joinArray)
    searchWords("directedBy", "details", joinArray)
    searchWords("releasedBy", "details", joinArray)
    searchWords("moods", "details", joinArray)
    searchWords("themes", "details", joinArray)
    searchWords("keywords", "details", joinArray)
    searchWords("atributes", "details", joinArray)
    searchWords("actors", "details", joinArray)
    searchWords("relatedMovies", "details", joinArray)


    #results = es.mtermvectors(index='details', doc_type='details',field_statistics='true',  fields=['directedBy'], ids=['0'])
    #results = es.termvectors(index='title', doc_type='title',fields=['title'])
    '''
                             


