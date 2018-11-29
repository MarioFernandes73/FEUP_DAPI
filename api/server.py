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
                            "boost":10,
                            "_name":"title - full"
                        }
                    }
                },
                {
                    "multi_match":{
                        "query":userInput,
                        "type":"phrase",
                        "fields":["genres","subGenres"],
                        "boost":10,
                        "_name":"genres and subGenres - full"
                    }
                },
                {
                    "match":{
                        "title":{
                            "query":userInput,
                            "boost":7,
                            "_name":"title - partial"
                        }
                    }
                },
                {
                    "match_phrase":{
                        "actors":{
                            "query":userInput,
                            "boost":10,
                            "_name":"actors - full"
                        }
                    }
                },
                {
                    "match":{
                        "synopsis":{
                            "query":userInput,
                            "boost":10,
                            "_name":"synopsis - partial"
                        }
                    }
                },
                {
                    "multi_match":{
                        "query":userInput,
                        "fields":["countries","directedBy","producedBy","releasedBy"],
                        "boost":4,
                        "_name":"countries and directedBy and producedBy and releasedBy - partial"
                    }
                },
                {
                    "multi_match":{
                        "query":userInput,
                        "fields":["moods","themes","keywords","attributes","mpaaRating"],
                        "boost":4,
                        "_name":"moods and themes and keywords and attributes and mpaaRating - partial"
                    }
                },
                {
                    "wildcard":{
                        "title":{
                            "wildcard":"*"+userInput+"*",
                            "boost":10,
                            "_name":"title - wildcard"
                        }
                    }
                },
                {
                    "match":{
                        "relatedMovies":{
                            "query":userInput,
                            "boost":7,
                            "_name":"relatedMovies - partial"
                        }
                    }
                }
            ]

    for number in intList:
        conditions.append({"range":{
            "releaseDate":{
                "lte":str(number)+"||/y",
                "gte":str(number)+"||/y",
                "format":"yyyy",
                "boost":100,
                "_name":"releaseDate - year: " + str(number)
                }}})

        field = ""
        if 0 <= number <= 10:
            numberParam1 = number
            numberParam2 = number
            field = "allmovieRating"
            queryName = "allmovieRating with rating of " + str(number)
        else:
            numberParam1 = number - 10
            numberParam2 = number + 10
            field = "duration"
            queryName = "movie with duration between " + str(numberParam1) + " and " + str(numberParam2)
        
        conditions.append({"range":{
            field:{
                "gte":numberParam1,
                "lte":numberParam2,
                "boost":100,
                "_name": queryName
            }
        }})

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    docs = es.search(index = "movie", doc_type = "movie", body = {
    "query":{
        "bool":{
            "should": conditions
        }
    }
}, size = 10)

    for doc in docs['hits']['hits']:
        print("id: " + doc['_id'] + " with score of " + str(doc['_score']) + " - '" + doc['_source']['title'] + "' because of " + str(doc['matched_queries']))


while True:
    try:
        userInput = input('Search the database ("q" to quit):')
        intList = [int(s) for s in userInput.split() if s.isdigit()]
        if userInput == "q":
            sys.exit()
        searchDB(userInput,intList)
    except KeyboardInterrupt:
        sys.exit()
    

                             


