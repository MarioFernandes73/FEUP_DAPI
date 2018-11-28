import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

countries_with_space = ["Hong Kong",  "South Korea", "New Zealand", "South Africa", "Ivory Coast" , "Burkina Faso", "Czech Republic", "Chad France", "Puerto Rico",
"West Germany", "Sri Lanka","Costa Rica","Dominican Republic", "Serbia and Montenegro", "United Arab Emirates", "Congo (Brazzaville)","Saudi Arabia","Georgia (Republic)",
"North Korea (Korean People's Democratic Republic)","Arab Emirates"]

def checkForNaN(obj):
    if str(obj) == "nan":
        return ""
    return obj

def printIndexes(es):
    print(es.indices.get_alias().keys())

def printDocsInIndexes(es, docName):
    res = es.search(index= docName, doc_type=docName, body = {'size' : 10000,'query': { 'match_all' : {}}})
    printResult(res)

def printResult(res):
    for item in res['hits']['hits']:
        print(item['_id'], item['_source'])

def deleteAllIndexes(es):
    es.indices.delete("*")


actions = list()
df = pd.read_csv("../data/links_all.csv", sep=",")
for index, row in df.iterrows():
    title = row["title"]
    genresArray = list()
    if str(row["genres"]) != "nan":
        genresArray = row["genres"].split(" | ")
    subGenresArray = list()
    if str(row["subGenres"]) != "nan":
        subGenresArray = row["subGenres"].split(" | ")
    releaseDate = datetime.strptime(row["releaseDate"], "%Y-%m-%d %H:%M:%S")
    duration = row["duration"]
    if str(duration) == "nan":
        duration = int(60)
    elif str(duration) != "nan":
        duration = int(duration)
    countriesArray = list()
    countries = row["countries"]
    if str(countries) != "nan":
        for country in countries_with_space:
            if country in countries:
                countries = countries.replace(country + " ", "")
                countriesArray.append(country)
        countriesArray.extend(countries.split(" "))
    mpaaRating = checkForNaN(row["mpaaRating"])
    allmovieRating = row["allmovieRating"]
    if str(allmovieRating) == "nan":
        allmovieRating = int(5)
    elif str(allmovieRating) != "nan":
        allmovieRating = int(allmovieRating)
    flags = checkForNaN(row["flags"])
    directedBy = checkForNaN(row["directedBy"])
    producedBy = checkForNaN(row["producedBy"])
    releasedBy = checkForNaN(row["releasedBy"])
    moodsArray = list()
    if str(row["moods"]) != "nan":
        moodsArray = row["moods"].split(" | ")
    themesArray = list()
    if str(row["themes"]) != "nan":
        themesArray = row["themes"].split(" | ")
    keywords = checkForNaN(row["keywords"])
    attributes = checkForNaN(row["attributes"])
    synopsis = checkForNaN(row["synopsis"])
    actorsArray = list()
    if str(row["actors"]) != "nan":
        actorsArray = row["actors"].split(" | ")
    relatedMoviesArray = list()
    if str(row["relatedMovies"]) != "nan":
        relatedMoviesArray = row["relatedMovies"].split(" | ")


    doc_details = {"title": title, "genres": genresArray, "subGenres": subGenresArray, "releaseDate":releaseDate, "duration": duration, "countries":countriesArray, "mpaaRating":mpaaRating, "allmovieRating": allmovieRating, "flags":flags, "directedBy":directedBy, "producedBy": producedBy, "releasedBy":releasedBy, "moods":moodsArray, "themes":themesArray, "keywords":keywords, "attributes":attributes, "actors":actorsArray, "relatedMovies":relatedMoviesArray, "synopsis": synopsis}

    actions.append({"_index": "movie","_type": "movie","_id": index,"_source": doc_details })


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
deleteAllIndexes(es)
helpers.bulk(es, actions)

