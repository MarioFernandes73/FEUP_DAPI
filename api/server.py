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
    print("count",results.get('count'))


word_data = ""
while word_data != "TERMINATE":
    print('Enter your search:("TERMINATE" for exit)')
    word_data = input()
    word_data = re.sub('[^\w\s]','',word_data)
    nltk_tokens = nltk.word_tokenize(word_data)
    joinArray = " ".join(str(x) for x in nltk_tokens)
    print(joinArray)

    #conta as palavras no indice titulo
    countWords("title", "title", joinArray)

    #conta as palavras no indice genero 
    print("genre")
    countWords("genre", "genre", joinArray)
    print('\n')


    #conta as palavras no indice synopsis
    print("synopsis")
    countWords("synopsis", "synopsis", joinArray)
    print('\n')

    #conta as palavras no indice details
    #"genres releaseDate duration countries mpaaRating allmovieRating flags directedBy producedBy releasedBy moods themes keywords attributes actors relatedMovies" 
    print("details")
    countWords("countries", "details", joinArray)
    countWords("directedBy", "details", joinArray)
    countWords("producedBy", "details", joinArray)
    countWords("directedBy", "details", joinArray)
    countWords("releasedBy", "details", joinArray)
    countWords("moods", "details", joinArray)
    countWords("themes", "details", joinArray)
    countWords("keywords", "details", joinArray)
    countWords("atributes", "details", joinArray)
    countWords("actors", "details", joinArray)
    countWords("relatedMovies", "details", joinArray)


    #results = es.mtermvectors(index='details', doc_type='details',field_statistics='true',  fields=['directedBy'], ids=['0'])
    #results = es.termvectors(index='title', doc_type='title',fields=['title'])
    
                             


