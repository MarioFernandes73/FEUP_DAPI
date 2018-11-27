import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
import json

countries_with_space = ["Hong Kong",  "South Korea", "New Zealand", "South Africa", "Ivory Coast" , "Burkina Faso", "Czech Republic", "Chad France", "Puerto Rico",
"West Germany", "Sri Lanka","Costa Rica","Dominican Republic", "Serbia and Montenegro", "United Arab Emirates", "Congo (Brazzaville)","Saudi Arabia","Georgia (Republic)",
"North Korea (Korean People's Democratic Republic)","Arab Emirates"]

allmovie_genres = ["Action","Adult","Adventure","Avant-garde / Experimental","Business","Children's/Family","Comedy","Comedy Drama","Crime","Culture & Society","Dance","Drama","Education","Epic","Family & Personal Relationships","Fantasy","Health & Fitness","Historical Film","Language & Literature","Leisure Arts","Music","Musical","Horror","Mystery","Nature","News","Reality Show","Romance","Science Fiction","Spirituality & Philosophy","Sports & Recreation","Spy Film","Theater","Thriller","Travel","Visual Arts","War","Western"]
allmovie_subgenres = ["Action Comedy","Action Thriller","Biker Film","Blaxploitation","Chase Movie","Chase/Road Show","Disaster Film","Escape Film","Martial Arts","Road Movie","Romantic Adventure","Samurai Film","Superhero Film","Superhero Show","Swashbuckler","Adult Entertainment","Hardcore Sex Film","Hentai","Sexploitation","Softcore Pay-Cable Show","Softcore Sex Film","Adventure Comedy","Adventure Drama","Costume Adventure","Jungle Film","Sea Adventure","Abstract Film","Essay Film","Surrealist Film","Computers","Finance & Investing","Sales & Marketing","Small Business","Workplace Issues","Animal Picture","Children's Entertainment","Children's Fantasy","Fairy Tales & Legends","Family-Oriented Adventure","Family-Oriented Comedy","Absurd Comedy","Americana","Beach Film","Black Comedy","Bloopers & Candid Camera","Comedy of Errors","Comedy of Manners","Comedy Thriller","Courtroom Comedy","Domestic Comedy","Fantasy Comedy","Farce","Gross-Out Comedy","Heavenly Comedy","Media Satire","Medical Comedy","Military Comedy","Mockumentary","Musical Comedy","Parody/Spoof","Police Comedy","Prank/Candid-Camera","Religious Comedy","Romantic Comedy","Satire","Screwball Comedy","Sex Comedy","Showbiz Comedy","Sitcom","Sketch Comedy","Sketch Comedy/Skit Show","Slapstick","Sophisticated Comedy","Sports Comedy","Standup Comedy","Stoner Comedy","Urban Comedy","Workplace Comedy","Buddy Film","Buddy Show","Coming-of-Age","Early Black Cinema","Ensemble Film","Feminist Film","Gay & Lesbian Films","Gay & Lesbian Show","Holiday Film","Odd Couple Film","Political Satire","Pop-Culture Show","Reunion Films","Slice of Life","Studio-Era Black Cinema","Teen Movie","Teen Show","Tragi-comedy","Trash Film","Caper","Cop Show","Crime Comedy","Crime Drama","Crime Thriller","Detective Film","Detective Show","Film Noir","Gangster Film","Gangster Show","Juvenile Delinquency Film","Master Criminal Films","Post-Noir (Modern Noir)","Prison Film","Prison Show","Procedural Show","True Crime","True-Crime Show","Anthropology","Architecture & Design","Art History","Beauty & Fashion","Biography","Cooking & Food","Film & Television History","Gender Issues","Hobbies & Games","Interpersonal Relationships","Inventions & Innovations","Journalism","Law & Crime","Marriage & Commitment","Media Studies","Mythology","Parenting","Performance Art","Politics & Government","Psychology","Race & Ethnicity","Sexuality","Shockumentary","Social History","Social Issues","Sociology","Sports","Tragedies & Catastrophes","Trivia/Quiz Show","Variety Show","World History","Ballroom Dance","Jazz & Modern Dance","Addiction Drama","Animal Show","Anthology Series","Anti-War Film","Biopic [feature]","Childhood Drama","Courtroom Drama","Docudrama","Erotic Drama","Family Drama","Film a Clef","Heavenly Drama","Inspirational Drama","Marriage Drama","Medical Drama","Medical Show","Melodrama","Message Movie","Musical Drama","Period Show","Political Drama","Political Thriller","Prime-Time Drama","Propaganda Film","Psychological Drama","Religious Drama","Romantic Drama","Rural Drama","Showbiz Drama","Soap Opera","Social Problem Film","Sports Drama","Supernatural Drama","Telenovela","Tragedy","Urban Drama","Adult Education","Careers","Children's Educational","Children's Issues","College & Test Prep","Special Education","Teaching","Vehicles & Transportation","British Empire Film","Epic Western","Historical Epic","Religious Epic","Romantic Epic","War Epic","Gardening","Home Decoration & Improvement","Home Entertaining","Weddings","Anime","Fantasy Adventure","Fantasy Drama","Harem Anime [Anime]","Heaven-Can-Wait Fantasies","Mythological Fantasy","Prehistoric Fantasy","Sword-and-Sandal","Sword-and-Sorcery","Aerobic Exercise","Alternative Health","Ambiance","Cooking Show","Diet & Nutrition","Illnesses & Disabilities","Martial Arts","Medicine","Morality & Values","Personal Safety","Self-Help","Toning & Strength Training","Women's Health","Yoga","Hagiography","Period Film","Costume Horror","Creature Film","Haunted House Film","Horror Comedy","Natural Horror","Sadistic Horror","Sci-Fi Horror","Sex Horror","Slasher Film","Supernatural Horror","Linguistics","Literary Studies","Holidays","Lifestyle Show","Makeover Show","Concerts","Instrumental Music","Music History","Music Show","Vocal Music","Animated Musical","Backstage Musical","Ballet","Dance Film","Film-Opera","Musical Fantasy","Musical Romance","Operetta","Rock Musical","Giallo","Gothic Film","Police Detective Film","Police Drama","Poliziotteschi","Whodunit","Adventure Travel","Animals","Biological Sciences","Environmental Science","Natural Environments","Nature Show","Physical Sciences","Unexplained Phenomena","Weather","News Magazine","Panel Show","Talk Show","Awards Show","Beauty/Talent Show","Candid Reality Show","Celebrity Reality Show","Competitive Reality Show","Dating Show","Game Show","Romantic Fantasy","Romantic Mystery","War Romance","Alien Film","Psychological Sci-Fi","Sci-Fi Action","Sci-Fi Adventure","Sci-Fi Comedy","Sci-Fi Disaster Film","Space Adventure","Tech Noir","New Age & Metaphysics","Philosophy","Religions & Belief Systems","Extreme Sports","Game Broadcast","Motor Sports","Sports Show","Glamorized Spy Film","Spy Comedy","Spy Show","Unglamorized Spy Film","War Spy Film","Filmed Play","Opera","Erotic Thriller","Law Show","Paranoid Thriller","Psychological Thriller","Supernatural Thriller","Armchair Travel","Guided Travel","Outdoor Recreation","Travel Show","Audio-Visual","Graphic & Applied Arts","Sculpture","Video Art","Cavalry Film","Combat Films","Military & War","POW Drama","Resistance Film","War Adventure","War Drama","B-Western","Comedy Western","Eurowestern","Hybrid Western","Indian Western","Modern Western","Musical Western","Outlaw (Gunfighter) Film","Psychological Western","Revisionist Western","Spaghetti Western","Traditional Western"]
allGenres = allmovie_genres + allmovie_subgenres


def checkForNaN(obj):
    if str(obj) == "nan":
        return ""
    return obj

def printResult(res):
    for item in res['hits']['hits']:
        print(item['_id'], item['_source'])

def deleteAllIndexes(es):
    es.indices.delete("*")

def indexGenres(es):
    for i, genre in enumerate(allGenres):
        indexGenre = {'genre':genre, 'moviesIds':[]}
        es.index(index='genre', doc_type='genre', id=i, body=indexGenre)


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

deleteAllIndexes(es)
indexGenres(es)


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
    if str(duration) != "nan":
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
    if str(allmovieRating) != "nan":
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

    genresRef = list()
    movieGenreList = genresArray + subGenresArray
    for genre in movieGenreList:
        res = es.search(index="genre", doc_type="genre", body = {'query': { 'match' : {"genre":genre} } } )
        for item in res['hits']['hits']:
            genresRef.append(item['_id'])
            newList = item['_source']['moviesIds'] + [index]
            item['_source']['moviesIds'] = newList
            j = {'doc' : item['_source'] }
            es.update(index="genre", doc_type="genre", id=item['_id'], body=j )

    doc_movie = {}
    doc_synopsis = {"synopsis": synopsis}
    doc_title = {"title": title}

    es.index(index='title', doc_type='title', id=index, body=doc_title)
    es.index(index='synopsis', doc_type='synopsis', id=index, body=doc_synopsis)

    break


#print( es.indices.get_alias().keys())

#m2 = {'name': 'mario'}
#v = json.dumps(m1)
#j = json.loads(v)
#print(j)


#es.index(index='sw', doc_type='people', id=3, body=j)

res = es.search(index="genre", doc_type="genre", body = {'size' : 10000,'query': { 'match_all' : {}}})
printResult(res)

res = es.search(index="title", doc_type="title", body = {'size' : 10000,'query': { 'match_all' : {}}})
printResult(res)