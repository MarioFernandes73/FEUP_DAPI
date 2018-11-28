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

def searchWords(parameter, index,tokens):
    string = " ".join(str(x) for x in tokens)

    docs = es.search(index=index, doc_type=index, body={ "query": {'match_all' : {}}})
    total_docs = docs.get('hits').get('total')
    print(total_docs)

    results = es.search(index=index, doc_type=index, body={ "query": {"match" : {parameter : string}}})
    resultHits = results.get('hits').get('hits')

    length = len(resultHits)
    #results = es.count(index=index, doc_type=index, body={ "query": {"match" : {parameter : string}}})
    #print("count",results,'\n')
    for i in range(0, length):
        hits = resultHits[i]
        id = hits.get("_id")
        print("index:", hits.get("_index"), "  id:" , id, "  ",parameter, ":" , hits.get("_source").get(parameter))
        results = es.mtermvectors(index=index, doc_type=index, field_statistics='true',  fields=parameter, ids=id)
        for j in tokens:
            term_freq= results.get('docs')[0].get('term_vectors').get(parameter).get('terms').get(j.lower())
            if term_freq != None:
                print(j.lower(),term_freq,'\n')



word_data = ""
while word_data != "TERMINATE":
    print('Enter your search:("TERMINATE" for exit)')
    word_data = input()
    word_data = re.sub('[^\w\s]','',word_data)
    joinArray = nltk.word_tokenize(word_data)

    #procura as palavras no indice titulo
    searchWords("title", "title", joinArray)
    print('\n')
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
      '''



                             


