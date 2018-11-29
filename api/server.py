import requests
from elasticsearch import Elasticsearch
import json
import sys



def searchDB(userInput, intList):

    conditions = [
                {
                    "match_phrase":{
                        "title":{
                            "query":userInput,
                            "boost":1000
                        }
                    }
                },
                {
                    "multi_match":{
                        "query":userInput,
                        "type":"phrase",
                        "fields":["genres","subGenres"],
                        "boost":10
                    }
                },
                {
                    "match":{
                        "title":{
                            "query":userInput,
                            "boost":7
                        }
                    }
                },
                {
                    "match_phrase":{
                        "actors":{
                            "query":userInput,
                            "boost":10
                        }
                    }
                },
                {
                    "match":{
                        "synopsis":{
                            "query":userInput,
                            "boost":1
                        }
                    }
                },
                {
                    "multi_match":{
                        "query":userInput,
                        "fields":["countries","directedBy","producedBy","releasedBy"],
                        "boost":10
                    }
                },
                {
                    "multi_match":{
                        "query":userInput,
                        "fields":["moods","themes","keywords","attributes","mpaaRating"],
                        "boost":10
                    }
                },
                {
                    "range":{
                        "releaseDate":{
                            "lte":"2010",
                            "gte":"2010",
                            "format":"yyyy",
                            "boost":10
                        }
                    }
                },
                {
                    "multi_match":{
                        "query":5,
                        "fields":["duration","allmovieRating"],
                        "boost":10
                    }
                },
                {
                    "wildcard":{
                        "title":{
                            "wildcard":"*"+userInput+"*",
                            "boost":10
                        }
                    }
                },
                {
                    "match":{
                        "relatedMovies":{
                            "query":userInput,
                            "boost":10
                        }
                    }
                }
            ]

    appendConditions = list()
    for number in intList:
        appendConditions.append({"range":{
            "releaseDate":{
                "lte":number,
                "gte":number,
                "format":"yyyy",
                "boost":10
                }}})

        appendConditions.append({"multi_match":{
            "query":number,
            "fields":["duration","allmovieRating"],
            "boost":10
            }})

    conditions.append(appendConditions)

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    docs = es.search(index = "movie", doc_type = "movie", body = {
    "query":{
        "bool":{
            "should": conditions
        }
    }
}, size = 10)

    for doc in docs['hits']['hits']:
        print(doc['_score'])
        print(doc['_source']['title'])
    
    #results = es.count(index=index, doc_type=index, body={ "query": {"match" : {parameter : string}}})
    #print("count",results,'\n')
    #for i in range(0, length):
        #hits = resultHits[i]
        #id = hits.get("_id")
        #print("index:", hits.get("_index"), "  id:" , id, "  ",parameter, ":" , hits.get("_source").get(parameter))
        #results = es.mtermvectors(index=index, doc_type=index, field_statistics='true',  fields=parameter, ids=id)
        #for j in tokens:
            #term_freq= results.get('docs')[0].get('term_vectors').get(parameter).get('terms').get(j.lower())
            #if term_freq != None:
                #print(j.lower(),term_freq,'\n')



userInput = ""
while userInput != "q":
    try:
        userInput = input('Search the database ("q" to quit):')
        intList = [int(s) for s in userInput.split() if s.isdigit()]
        searchDB(userInput,intList)
    except KeyboardInterrupt:
        sys.exit()
    

                             


