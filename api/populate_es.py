import pandas as pd
from datetime import datetime

df = pd.read_csv("../data/links_all.csv", sep=",")
for index, row in df.iterrows():
    title = row["title"]
    genres = row["genres"].split(" | ")
    subGenres = row["subGenres"].split(" | ")
    releaseDate = row["releaseDate"]
    duration = row["duration"]
    countries = row["countries"]
    mpaaRating = row["mpaaRating"]
    allmovieRating = row["allmovieRating"]
    flags = row["flags"]
    directedBy = row["directedBy"]
    producedBy = row["producedBy"]
    releasedBy = row["releasedBy"]
    moods = row["moods"]
    themes = row["themes"]
    keywords = row["keywords"]
    attributes = row["attributes"]
    synopsis = row["synopsis"]
    actors = row["actors"]
    relatedMovies = row["relatedMovies"]

    print(releaseDate)
    break